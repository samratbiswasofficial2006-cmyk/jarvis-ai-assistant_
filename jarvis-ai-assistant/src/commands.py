"""Built-in commands for JARVIS."""
import ast
import operator
import urllib.parse
import webbrowser
from datetime import datetime


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_calculate(expression: str):
    """Evaluate a small arithmetic expression without eval()."""
    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 8:
                raise ValueError("Exponent is too large.")
            return _ALLOWED_OPERATORS[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](visit(node.operand))
        raise ValueError("Only basic arithmetic is supported.")
    tree = ast.parse(expression, mode="eval")
    result = visit(tree)
    if abs(result) > 10**15:
        raise ValueError("Result is too large.")
    return result


class CommandHandler:
    def execute(self, text: str) -> str:
        command = text.strip()
        lower = command.lower()

        if lower in {"help", "commands"}:
            return (
                "Commands: help | time | date | open <site> | search <query> | "
                "maps <place or route> | calculate <expression> | ai: <question> | exit"
            )
        if lower == "time":
            return datetime.now().astimezone().strftime("The time is %I:%M %p.")
        if lower == "date":
            return datetime.now().astimezone().strftime("Today is %A, %d %B %Y.")
        if lower.startswith("open "):
            site = lower[5:].strip()
            known = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "github": "https://github.com",
                "gmail": "https://mail.google.com",
                "wikipedia": "https://www.wikipedia.org",
            }
            url = known.get(site)
            if not url:
                candidate = site if "://" in site else f"https://{site}"
                if "." not in candidate.split("://", 1)[-1]:
                    return "Please provide a known site or a domain, such as 'open github' or 'open example.com'."
                url = candidate
            webbrowser.open(url)
            return f"Opening {site} in your browser."
        if lower.startswith("search "):
            query = command[7:].strip()
            if not query:
                return "What would you like me to search for?"
            webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query))
            return f"Searching the web for: {query}"
        if lower.startswith("maps "):
            place = command[5:].strip()
            if not place:
                return "Tell me a place or route to find on Maps."
            webbrowser.open("https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote_plus(place))
            return f"Opening Google Maps for: {place}"
        if lower.startswith("calculate "):
            try:
                return f"The answer is {safe_calculate(command[10:].strip())}."
            except (ValueError, SyntaxError, ZeroDivisionError) as exc:
                return f"I couldn't calculate that: {exc}"
        return "I don't recognize that command. Type 'help' to see the available commands."
