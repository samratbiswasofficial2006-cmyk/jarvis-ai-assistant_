"""Core assistant orchestration."""
import os
from .commands import CommandHandler


class JarvisAssistant:
    def __init__(self):
        self.commands = CommandHandler()

    def handle(self, text: str) -> str:
        text = text.strip()
        if not text:
            return "I didn't catch a command. Type 'help' to see what I can do."

        if text.lower().startswith("ai:"):
            return self._ask_ai(text[3:].strip())

        return self.commands.execute(text)

    @staticmethod
    def _ask_ai(prompt: str) -> str:
        if not prompt:
            return "Please add a question after 'ai:'."
        if not os.getenv("OPENAI_API_KEY"):
            return ("AI chat is optional. Set the OPENAI_API_KEY environment variable "
                    "and install the openai package to enable it.")
        try:
            from openai import OpenAI
            client = OpenAI()
            result = client.responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=prompt,
            )
            return result.output_text or "I couldn't generate a response."
        except ImportError:
            return "Install the optional AI package with: pip install openai"
        except Exception as exc:
            return f"AI request failed: {exc}"
