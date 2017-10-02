# -*- coding: utf-8 -*-

# https://librosa.github.io/librosa/core.html#audio-processing

# https://librosa.github.io/librosa/_modules/librosa/core/audio.html#load
# load wave file
'''
    Returns
-------
y    : np.ndarray [shape=(n,) or (2, n)]
    audio time series

sr   : number > 0 [scalar]
    sampling rate of `y`
'''

# https://librosa.github.io/librosa/generated/librosa.core.stft.html?highlight=stft#librosa.core.stft

'''
Parameters:	
y : np.ndarray [shape=(n,)], real-valued

the input signal (audio time series)

n_fft : int > 0 [scalar]

FFT window size

hop_length : int > 0 [scalar]

number audio of frames between STFT columns. If unspecified, defaults win_length / 4.

win_length : int <= n_fft [scalar]

Each frame of audio is windowed by window(). The window will be of length win_length and then padded with zeros to match n_fft.

If unspecified, defaults to win_length = n_fft.

window : string, tuple, number, function, or np.ndarray [shape=(n_fft,)]

a window specification (string, tuple, or number); see scipy.signal.get_window
a window function, such as scipy.signal.hanning
a vector or array of length n_fft
center : boolean

If True, the signal y is padded so that frame D[:, t] is centered at y[t * hop_length].
If False, then D[:, t] begins at y[t * hop_length]
dtype : numeric type

Complex numeric type for D. Default is 64-bit complex.

mode : string

If center=True, the padding mode to use at the edges of the signal. By default, STFT uses reflection padding.

Returns:	
D : np.ndarray [shape=(1 + n_fft/2, t), dtype=dtype]

STFT matrix
'''

import librosa
import numpy as np

sound_fpath = "../res"
sound_file = "hanekawa_voices2.wav"

sr = 44100
n_fft = 2048 # fft points (samples)

frame_shift = 0.0125 # seconds
frame_length = 0.05 # seconds
hop_length = int(sr*frame_shift) # samples -> frame_shift
win_length = int(sr*frame_length) # samples -> frame_length


n_mels = 80 # Number of Mel banks to generate

def get_spectrograms(sound_file):
    '''
    :param sound_file:
     String data. full path to a sound file
    :return: 
    '''

    # Loading sound file
    y, sr = librosa.load(sound_file, sr=None)

    # stft. D: (1+n_fft//2, T)
    # //2 means what? 10/2/2017
    D = librosa.stft(y=y,
                     n_fft=n_fft,
                     hop_length=hop_length,
                     win_length=win_length)
    # magnitude spectrogram
    magnitude = np.abs(D) # (1+n_fft/2, T)

    # power spectrogram
    power = magnitude**2 # (1+n_fft/2, T)

    # mel spectrogram
    S = librosa.feature.melspectrogram(S=power, n_mels=n_mels) # (n_mels, T)

    # (T, n_mels), (T, 1+n_fft/2)
    return np.transpose(S.astype(np.float32)), np.transpose(magnitude.astype(np.float32))





def main():
    get_spectrograms(sound_fpath + sound_file)