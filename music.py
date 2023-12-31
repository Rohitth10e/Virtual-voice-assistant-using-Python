import speech_recognition as sr
import pyttsx3
import ctypes

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_music(file_path):
    ctypes.windll.winmm.mciSendStringW(f"/Users/Dell/Music/", None, 0, None)
    ctypes.windll.winmm.mciSendStringW("play mp3", None, 0, None)

def stop_music():
    ctypes.windll.winmm.mciSendStringW("stop mp3", None, 0, None)
    ctypes.windll.winmm.mciSendStringW("close mp3", None, 0, None)

def voice_controlled_music_player():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something to control the music player:")
        speak("Say play to play music, stop to stop music, or exit to exit.")

        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                if "play" in command:
                    print("Playing music...")
                    speak("Playing music")
                    play_music(r"path\to\your\music\file.mp3")
                elif "stop" in command:
                    print("Stopping music...")
                    speak("Stopping music")
                    stop_music()
                elif "exit" in command:
                    print("Exiting the music player.")
                    speak("Exiting the music player")
                    break
                else:
                    print("Command not recognized. Try saying 'play', 'stop', or 'exit'.")
                    speak("Command not recognized. Try saying play, stop, or exit.")

            except sr.UnknownValueError:
                print("Could not understand audio. Please try again.")
                speak("Could not understand audio. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak("Error occurred. Please try again.")

if __name__ == "__main__":
    voice_controlled_music_player()
