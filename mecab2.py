import sys
import MeCab
m = MeCab.Tagger("-Ochasen -d /usr/lib/mecab/dic/mecab-ipadic-neologd")
print m.parse("ドラゴンボールの作者は鳥山先生である。")
