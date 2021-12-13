# Import packages
from pydub import AudioSegment
from pydub.playback import play


# Play audio
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3", format="mp3")
play(playaudio)
