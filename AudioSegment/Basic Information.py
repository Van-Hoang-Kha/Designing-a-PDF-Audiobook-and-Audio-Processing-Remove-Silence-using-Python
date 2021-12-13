#Basic Information

import numpy as np
import matplotlib.pyplot as plt
import audiosegment

print("Reading in the wave file...")
seg = audiosegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")

print("Information:")
print("Channels:", seg.channels)
print("Bits per sample:", seg.sample_width * 8)
print("Sampling frequency:", seg.frame_rate)
print("Length:", seg.duration_seconds, "seconds")
