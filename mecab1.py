#python3

import MeCab
mecab = MeCab.Tagger("-Ochasen")
print(mecab.parse("今日はいい天気ですね。"))