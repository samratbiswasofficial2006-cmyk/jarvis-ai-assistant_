"""Entry point for the JARVIS AI Assistant."""
import argparse
from src.assistant import JarvisAssistant
from src.voice import VoiceInterface


def main():
    parser = argparse.ArgumentParser(description="JARVIS AI Assistant")
    parser.add_argument("--voice", action="store_true", help="Enable optional voice input/output")
    args = parser.parse_args()

    assistant = JarvisAssistant()
    voice = VoiceInterface() if args.voice else None

    print("\nJ.A.R.V.I.S. - Personal Assistant")
    print("Type 'help' to see commands. Type 'exit' to quit.\n")

    while True:
        try:
            if voice:
                spoken = voice.listen()
                if not spoken:
                    continue
                command = spoken
                print(f"You: {command}")
            else:
                command = input("You: ").strip()

            if command.lower() in {"exit", "quit", "shutdown"}:
                response = "Goodbye. JARVIS signing off."
                print(f"JARVIS: {response}")
                if voice:
                    voice.speak(response)
                break

            response = assistant.handle(command)
            print(f"JARVIS: {response}")
            if voice:
                voice.speak(response)
        except (KeyboardInterrupt, EOFError):
            print("\nJARVIS: Session ended. Goodbye.")
            break
        except Exception as exc:
            print(f"JARVIS: Something went wrong: {exc}")


if __name__ == "__main__":
    main()
