import wave
import numpy as np

# 対象データは hanekawa_all.wav
# 配列の長さ: 118707388

# まず,0でない値が入ったiを見つける
# これがchunkの開始地点
# start_chunk_i

# 次に, 0が入ったi=k_0を見つける
# この時, i=k_0-1は
# end_chunk_i
# そこから1.5秒以上の無音区間があるかどうかを調べる

# 1.5秒以上の空白は無音区間とする
# sampling_rate=48000の場合,
# 無音区間を
# 1.5*48000=72000個の"0"が連続する部分と
# 読み換えられる

# i=k_0から,k_71999まで0ならTrue
# 無音区間がTrueの場合は,
# k_0は前のchunkの終端,
# k_71999(または,これより大きい値)で,
# 初めて0でない値がでるiが
# 次のchunkの開始
# 途中で0でない値が出た場合,
# k_0を更新して, そこから再度チェックを開始する
# end_chunk_iも更新


def load_wav(filename):
    # wavf = wave.open(filename, 'r')
    sampling_rate = 0
    npframes = 0

    with wave.open(filename, 'r') as wavf:

        sampling_rate = wavf.getsampwidth() * 8

        # read frame binary data
        frames = wavf.readframes(wavf.getnframes())
        #　convert to nparray
        npframes = np.frombuffer(frames, dtype='int16')
        npframes = npframes * (1.0 / 32768.0) # pcm decode?

    print(npframes)
    return (sampling_rate, npframes)


def save_wav(sig, filename, samplingrate):
    # pcm encode
    sig = sig * float(0x7fff)

    samples = np.array(sig, np.int16)

    w = wave.Wave_write(filename)
    w.setnchannels(1)
    w.setsampwidth(2) # 2 bytes
    w.setframerate(samplingrate)
    w.setnframes(len(samples))
    w.setcomptype('NONE', 'desrip') # No compression

    w.writeframes(samples.tostring())
    w.close()

def db_to_float(db, using_amplitude=True):
    """
    Converts the input db to a float, which represents the equivalent
    ratio in power.
    """
    db = float(db)
    if using_amplitude:
        return 10 ** (db / 20)
    else: # using power
        return 10 ** (db / 10)


# '_': grobal variable
# res file names
_resdir = './res/'
_filename = 'hanekawa_all.wav'
(_samplingrate, _waveform) = load_wav(_resdir + _filename)
# print(max(_waveform))
print(len(_waveform))

#csvファイルとして保存
# np.savetxt('out.csv',_waveform,delimiter=',')

print(_waveform[0:10000])
exit(0)

_start_chunk_i = 0
_end_chunk_i = 0
zero_count = 0
for i in range(len(_waveform)):
    print(zero_count) # for debug
    is_silent = True
    chunk_detected = False
    if chunk_detected:
        break
    if _waveform[i] != 0:
        # same chunk or next chunk
        if is_silent:
            _start_chunk_i = i # k_0
            is_silent = False
        _end_chunk_i = i
        zero_count = 0
    else:
        # silent
        is_silent = True
        zero_count += 1
        if (zero_count > 72000):
            # slient large enough
            chunk_detected = True

print(_start_chunk_i)
print(_end_chunk_i)