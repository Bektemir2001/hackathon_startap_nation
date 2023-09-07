import speech_recognition as sr
import pyaudio

recognizer = sr.Recognizer()

class SpeechRecognition:

    def recognition(self, audio_path):
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio, language="ru-RU")
                return text
            except sr.UnknownValueError:
                return "Не удалось распознать аудио"
            except sr.RequestError as e:
                return f"Произошла ошибка запроса к Google Web Speech API; {e}"
