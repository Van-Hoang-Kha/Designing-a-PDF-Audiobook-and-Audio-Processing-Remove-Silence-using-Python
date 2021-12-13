import numpy as np
import matplotlib.pyplot as plt
import audiosegment

print("Reading in the wave file...")
seg = audiosegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")

#FFT

#...
# Do it just for the first 3 seconds of audio
hist_bins, hist_vals = seg[1:3000].fft()
hist_vals_real_normed = np.abs(hist_vals) / len(hist_vals)
plt.plot(hist_bins / 1000, hist_vals_real_normed)
plt.xlabel("kHz")
plt.ylabel("dB")
plt.show()
