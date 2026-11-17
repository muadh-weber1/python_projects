import speech_recognition as sr
from deep_translator import MyMemoryTranslator
from pydub import AudioSegment
import time

def translate_voice_file(filepath):
    print("converting audio format...")
    sound = AudioSegment.from_file(filepath)
    wav_path = "weber.wav"
    sound.export(wav_path, format="wav")
    
    recognizer = sr.Recognizer()
    print("reading your audio-----")
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        spoken_text = recognizer.recognize_google(audio_data)
        print(spoken_text)
        
        time.sleep(5)
        
        translated_text=MyMemoryTranslator(source='english', target='arabic').translate(spoken_text)
        print(f"Translation: {translated_text}")

if __name__ == "__main__":
 filename=input("Enter audio file name ")	   
 translate_voice_file(f"/sdcard/Weber Translate/{filename}")


