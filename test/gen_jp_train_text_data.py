
'''
### はじめに
声優音声コーパスのデータを,  github.com/Kyubyong/tacotron の
学習データに使用するためにデータを処理するプログラム.

目標:
学習用のテキストデータと音声ファイルのメタデータをまとめた csvファイルを作る.

### 雑記
fujitou_normal_002
tsuchiya_normal_003

uemura_angry
uemura_happy
uemura_normal

TAG:
fujitou, tsuchiya, uemura
happy, normal, angry

python, wave, playing time
http://denshi.blog.jp/signal_processing/python/wave_time

'''

import wave

def pad_with_zero(number):
    return '{0:03d}'.format(number) # 50 => '050'

def get_wave_playing_time(filename):
    wf = wave.open(filename, "r") # require : full path
    ptime = float(wf.getnframes()) / wf.getframerate()
    return format(ptime, '.1f') # float, format: 10.1000101 => 10.1

def load_lines(filename):
    lines = []
    with open(filename, encoding='UTF-8') as f:  # 文字コードの指定
        for line in f:
            elements = line.rstrip().split('\t')  # カンマ区切りの場合
            lines.append(elements[1]) # [1]: カタカナセリフ
            # print(line)
    return lines

FMAX_NUM = 100

def main():
    out_csvdata = ''
    fname = 'res/tts/sentences_v2.txt'

    valist = ['fujitou', 'tsuchiya', 'uemura']
    feelings = ['happy', 'normal', 'angry']

    lines = load_lines(fname)

    for vaname in valist:
        for feeling in feelings:
            fname = vaname + '_' + feeling #  >>> uemura_angry
            for i in range(FMAX_NUM):
                number_padded = pad_with_zero(i + 1)
                wfname = fname + '_' + number_padded # >>> fujitou_normal_002
                fpath = fname + '/' + wfname #  >>> fujitou_normal/fujitou_normal_002
                fullpath = 'res/voices/' + fpath + '.wav'
                ptime = get_wave_playing_time(fullpath)

                targetline = fpath + ',' + lines[i] + ',' + ptime
                # >>> uemura_angry/uemura_angry_003,コンピュータ ゲーム ノ メーカー ヤ ギョーカイ ダンタイ ナド ニ カンレン スル ジンブツ ノ カテゴリ,8.3

                print(targetline)

                out_csvdata = out_csvdata + targetline + '\n'

    outfname = 'sentences.csv'
    outfname = 'out/' + outfname
    with open(outfname, 'w') as f:
        f.write(out_csvdata)

if __name__ == '__main__':
    main()
