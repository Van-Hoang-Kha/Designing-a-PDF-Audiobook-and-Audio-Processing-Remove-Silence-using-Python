from pydub.playback import play
from pydub import AudioSegment

sound = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/pdf_audio.mp3")

def speed_change(sound, speed):

    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    filename = r'/home/kha/Documents/text-to-speech/Result-Audiobook/Change-slow-pdf.mp3'

    sound_with_altered_frame_rate.export(filename, format ="mp3")


# To Slow down audio
slow_sound = speed_change(sound, 0.75)


# Play audio
playaudio = AudioSegment.from_file(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/Change-slow-pdf.mp3", format="mp3")
play(playaudio)


# 1.0 is the Normal Speed Rate
