"""Optional speech input and output."""
class VoiceInterface:
    def __init__(self):
        try:
            import speech_recognition as sr
            import pyttsx3
        except ImportError as exc:
            raise RuntimeError(
                "Voice packages are missing. Install requirements with "
                "'pip install -r requirements.txt', or run without --voice."
            ) from exc

        self.sr = sr
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 175)

    def listen(self) -> str:
        try:
            with self.sr.Microphone() as source:
                print("JARVIS: Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=6, phrase_time_limit=10)
            return self.recognizer.recognize_google(audio)
        except self.sr.WaitTimeoutError:
            print("JARVIS: No speech detected. Try again.")
        except self.sr.UnknownValueError:
            print("JARVIS: I couldn't understand that.")
        except self.sr.RequestError as exc:
            print(f"JARVIS: Speech service unavailable: {exc}")
        return ""

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()
