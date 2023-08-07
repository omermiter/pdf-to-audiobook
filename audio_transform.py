import gtts
import os


class To_audio:
    # This function creates and saves an audio file based on the text you sent it
    def transform(self, text):
        print("converting your file this may take some time...")
        t1 = gtts.gTTS(text)
        t1.save("Audio.mp3")

    #this functiom plays the file
    def play(self):
        os.system("Audio.mp3")
