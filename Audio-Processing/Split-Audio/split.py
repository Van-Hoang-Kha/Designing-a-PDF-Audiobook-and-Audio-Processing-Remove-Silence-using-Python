import itertools
import pydub
from pydub import AudioSegment
from pydub.utils import db_to_float
import csv
import control


def detect_silence(audio_segment, min_silence_len, silence_thresh, seek_step):
    seg_len = len(audio_segment)

    # you can't have a silent portion of a sound that is longer than the sound
    if seg_len < min_silence_len:
        return []

    # convert silence threshold to a float value (so we can compare it to rms)
    silence_thresh = db_to_float(silence_thresh) * \
        audio_segment.max_possible_amplitude
    print("silence_thresh: ", silence_thresh)

    # find silence and add start and end indicies to the to_cut list
    silence_starts = []

    # check successive (1 sec by default) chunk of sound for silence
    # try a chunk at every "seek step" (or every chunk for a seek step == 1)
    last_slice_start = seg_len - min_silence_len
    slice_starts = range(0, last_slice_start + 1, seek_step)

    # guarantee last_slice_start is included in the range
    # to make sure the last portion of the audio is seached
    if last_slice_start % seek_step:
        slice_starts = itertools.chain(slice_starts, [last_slice_start])

    for i in slice_starts:
        audio_slice = audio_segment[i:i + min_silence_len]
        if audio_slice.rms <= silence_thresh:
            silence_starts.append(i)

    # short circuit when there is no silence
    if not silence_starts:
        return []

    # combine the silence we detected into ranges (start ms - end ms)
    silent_ranges = []

    prev_i = silence_starts.pop(0)
    current_range_start = prev_i

    for silence_start_i in silence_starts:
        continuous = (silence_start_i == prev_i + seek_step)

        # sometimes two small blips are enough for one particular slice to be
        # non-silent, despite the silence all running together. Just combine
        # the two overlapping silent ranges.
        silence_has_gap = silence_start_i > (prev_i + min_silence_len)

        if not continuous and silence_has_gap:
            silent_ranges.append([current_range_start,
                                  prev_i + min_silence_len])
            current_range_start = silence_start_i
        prev_i = silence_start_i

    silent_ranges.append([current_range_start,
                          prev_i + min_silence_len])

    return silent_ranges


def detect_nonsilent(audio_segment, min_silence_len, silence_thresh, seek_step):
    silent_ranges = detect_silence(
        audio_segment, min_silence_len, silence_thresh, seek_step)
    len_seg = len(audio_segment)

    # if there is no silence, the whole thing is nonsilent
    if not silent_ranges:
        return [[0, len_seg]]

    # short circuit when the whole audio segment is silent
    if silent_ranges[0][0] == 0 and silent_ranges[0][1] == len_seg:
        return []

    print("silent_ranges in detect_nonsilent: ", silent_ranges)
    prev_end_i = 0
    nonsilent_ranges = []
    for start_i, end_i in silent_ranges:
        nonsilent_ranges.append([prev_end_i, start_i])
        prev_end_i = end_i

    if end_i != len_seg:
        nonsilent_ranges.append([prev_end_i, len_seg])

    if nonsilent_ranges[0] == [0, 0]:
        nonsilent_ranges.pop(0)

    print("nonsilent_ranges in detect_nonsilent method", nonsilent_ranges)
    print("nonsilent_ranges in detect_nonsilent array size", len(nonsilent_ranges))
    return nonsilent_ranges


def split_on_silence(audio_segment, min_silence_len, silence_thresh, keep_silence, seek_step):
    """
    audio_segment - original pydub.AudioSegment() object
    min_silence_len - (in ms) minimum length of a silence to be used for
        a split. default: 1000ms
    silence_thresh - (in dBFS) anything quieter than this will be
        considered silence. default: -16dBFS
    keep_silence - (in ms) amount of silence to leave at the beginning
        and end of the chunks. Keeps the sound from sounding like it is
        abruptly cut off.
    """

    not_silence_ranges = detect_nonsilent(
        audio_segment, min_silence_len, silence_thresh, seek_step)

    chunks = []
    for start_i, end_i in not_silence_ranges:
        start_i = max(0, start_i - keep_silence)
        end_i += keep_silence

        chunks.append(audio_segment[start_i:end_i])

    return chunks


sound_file = AudioSegment.from_wav(
    r"/home/kha/Documents/text-to-speech/Result-Audiobook/convertedrate.wav")
audio_chunks = split_on_silence(sound_file,
                                # must be silent for at least half a second
                                min_silence_len=50,

                                # consider it silent if quieter than -16 dBFS
                                silence_thresh=-23,
                                keep_silence=100,
                                seek_step=1
                                )

print("Number of audio chunks produced from the given audio: ", len(audio_chunks))

silence_from_audio = detect_silence(
    sound_file, min_silence_len=50, silence_thresh=-23, seek_step=1)
total_audio_time = 0

header_row = [""]
chunks_peak_amp_row = ["Amplitude(Peak)"]
chunks_peak_amp_row_db = ["Amplitude(dB)"]
chunks_peak_amp_row_dBFS = ["Amplitude(dBFS)"]
chunks_time_duration = ["Time duration"]
chunks_frame_count = ["Frame Count"]

for i, chunk in enumerate(audio_chunks):
    header_row.append("chunk"+str(i+1))

print("header_row: ", header_row)

with open('Results.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(header_row)

    for i, chunk in enumerate(audio_chunks):
        out_file = "/home/kha/Documents/text-to-speech/Result-Audiobook/Split-data/split{0}.wav".format(
            i)
        print("exporting", out_file)
        chunk.export(out_file, format="wav")

        ##Peak Amplitude of each audio chunk
        chunks_peak_amp_row.append(chunk.max)
        chunks_peak_amp_row_db.append(control.mag2db(chunk.max))
        chunks_peak_amp_row_dBFS.append(chunk.max_dBFS)

        ##Time duration of each audio chunk
        chunks_time_duration.append(str(chunk.duration_seconds)+" sec")

        ##Frame count of each audio chunk
        chunks_frame_count.append(chunk.frame_count(ms=None))

        ##Total sum of audio lengths of all audio chunks
        total_audio_time = total_audio_time + chunk.duration_seconds

    writer.writerow(chunks_peak_amp_row)
    writer.writerow(chunks_peak_amp_row_db)
    writer.writerow(chunks_peak_amp_row_dBFS)
    writer.writerow(chunks_time_duration)
    writer.writerow(chunks_frame_count)
    writer.writerow(["Total audio output time", total_audio_time])
    csvFile.close()

print(total_audio_time, "seconds")
