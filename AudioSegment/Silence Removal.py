import numpy as np
import matplotlib.pyplot as plt
import audiosegment
from pydub import AudioSegment
from pydub.playback import play


print("Reading in the wave file...")
seg = audiosegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")

#Silence Removal

# ...
print("Plotting before silence...")
plt.subplot(211)
plt.title("Before Silence Removal")
plt.plot(seg.get_array_of_samples())

seg = seg.filter_silence(duration_s=0.2, threshold_percentage=5.0)
outname_silence = r"/home/kha/Documents/text-to-speech/Result-Audiobook/nosilence.wav"
seg.export(outname_silence, format="wav")

print("Plotting after silence...")
plt.subplot(212)
plt.title("After Silence Removal")

plt.tight_layout()
plt.plot(seg.get_array_of_samples())
plt.show()
# Play audio
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/nosilence.wav", format="wav")
play(playaudio)
