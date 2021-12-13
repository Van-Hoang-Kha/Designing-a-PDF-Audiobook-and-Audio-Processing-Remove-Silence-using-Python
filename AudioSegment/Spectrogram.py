#Basic Information

import numpy as np
import matplotlib.pyplot as plt
import audiosegment

print("Reading in the wave file...")
seg = audiosegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")


#Spectrogram

#...
freqs, times, amplitudes = seg.spectrogram(window_length_s=0.03, overlap=0.5)
amplitudes = 10 * np.log10(amplitudes + 1e-9)

# Plot
plt.pcolormesh(times, freqs, amplitudes)
plt.xlabel("Time in Seconds")
plt.ylabel("Frequency in Hz")
plt.show()
