from playsound import playsound
import os

sound_file = r"resources\sine.mp3"
def play_background_sound():
    absolute_path = os.path.abspath(sound_file)
    try:
        absolute_path = os.path.abspath(sound_file)
        playsound(absolute_path)
    except:
        pass


play_background_sound()