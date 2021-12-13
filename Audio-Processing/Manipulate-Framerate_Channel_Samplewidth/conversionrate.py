from pydub import AudioSegment
from pydub.playback import play
sound = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")

print("----------Before Conversion--------")
print("Frame Rate", sound.frame_rate)
print("Channel", sound.channels)
print("Sample Width",sound.sample_width)

# Change Frame Rate
sound = sound.set_frame_rate(23000) # Nen chon 16000Hz

# Change Channel
sound = sound.set_channels(1)     

# Change Sample Width
sound = sound.set_sample_width(1)

# Export the Audio to get the changed content
sound.export(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/convertedrate.wav", format="wav")

#Play Audio Conversion
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/convertedrate.wav", format="wav")
play(playaudio)

#Ctrl + Z de dung 