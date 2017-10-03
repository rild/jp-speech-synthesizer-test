# -*- coding: utf-8 -*-

'''
声優音声コーパスのデータをうまくワードごとに分割したい
理由は, tacotron/WEB/text.csv の形式に近づけるため.

日本語は文節ごとにスペースを入れない文章であるから,
言語処理を行って, 単語や助詞ごとに分割を行う.

1. .txt ファイルから,  １行ごとの String データを配列に入れる
2. String データを　スペース(タブ？）ごとに分割する
3. 声優音声コーパステキスト sentence 部分を構文解析によって分割する
4. 分割された単語ごとにカタカナの文を分割する (ここは人力で頑張る）
5. 学習用のテキストデータの, sentence 部分完成！

とりあえずこんな感じ.
'''


# import codecs
#
# fpath = './res/'
# file_name = 'balance_sentences.txt'
# file_name = fpath + file_name
#
# fo = codecs.open(file_name, 'r', 'ascii')
# content = fo.read()  ## returns unicode
# print(content)
#
# # with open(file_name, "rU") as f:
# #     data = map(lambda x:x.split("\t"), f.read().strip().split("\n"))
# #
# #     print(data[0])

import sys
import codecs

from janome.tokenizer import Tokenizer
fname = sys.argv[1]
print('read: ' + fname)

t = Tokenizer()
tokens = t.tokenize(u'pythonの本を読んだ')
out = ''
with open(fname, encoding='UTF-8') as f:  # 文字コードの指定
    for line in f:
        elements = line.rstrip().split('\t')  # カンマ区切りの場合
        tokens = t.tokenize(elements[1], wakati=True)
        text = ''
        for token in tokens:
            text += str(token) + ' '
        # print(text)
        out += text + '\n'
        # for element in elements:
        #     print(element.encode('utf-8'))

if len(sys.argv) != 3:
    exit(0)

fname = sys.argv[2]
print('write: ' + fname)
with open(fname, 'w') as f:
    f.write(out)

print('finish')