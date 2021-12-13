
# Import packages
import numpy as np
import matplotlib.pyplot as plt
import audiosegment
from pydub import AudioSegment
from pydub.playback import play




print("Reading in the wave file...")
seg = audiosegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")
#Voice Detection
# ...
print("Detecting voice...")
seg = seg.resample(sample_rate_Hz=32000, sample_width=2, channels=1)
results = seg.detect_voice()
voiced = [tup[1] for tup in results if tup[0] == 'v']
unvoiced = [tup[1] for tup in results if tup[0] == 'u']

print("Reducing voiced segments to a single wav file 'voiced.wav'")
voiced_segment = voiced[0].reduce(voiced[1:])
voiced_segment.export(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/voiced.wav", format="WAV")

print("Reducing unvoiced segments to a single wav file 'unvoiced.wav'")
unvoiced_segment = unvoiced[0].reduce(unvoiced[1:])
unvoiced_segment.export(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/unvoiced.wav", format="WAV")


# Play audio voiced
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/voiced.wav", format="mp3")
play(playaudio)

# Play audio unvoiced
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/unvoiced.wav", format="mp3")
play(playaudio)
