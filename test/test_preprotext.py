

import re
import numpy as np

def load_vocab():
    vocab = "EG abcdefghijklmnopqrstuvwxyz'" # E: Empty. ignore G
    char2idx = {char:idx for idx, char in enumerate(vocab)}
    idx2char = {idx:char for idx, char in enumerate(vocab)}
    return char2idx, idx2char


text = "This is sample text."
text2 = "Is this sample text."
text3 = "Yes, this is sample text."
texts = []

print("original:" + text)
text = re.sub(r"[^ a-z']", "", text.strip().lower())

print("strip:" + text)

for char in text:
    print("char:" + char)


char2idx, idx2char = load_vocab()

indexlist = np.array([char2idx[char] for char in text], np.int32)

print(indexlist)

print(indexlist[0])

texts.append(np.array([char2idx[char] for char in text], np.int32).tostring())

print(texts)