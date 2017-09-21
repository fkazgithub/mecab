#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import time
import math
import codecs
# import Tkinter
# import tkMessageBox
import MeCab

f = open('sample.txt', 'r')#読み込むファイルを開く
text = f.read()#ファイルから全データを読み込む
f.close()#ファイルを閉じる

ff = open('sample2.txt','w')#書き出し用ファイル開く

def mecabb(text):#mecab関数化
 m = MeCab.Tagger()
 n = m.parseToNode(text)


 while n:
 #	print (n.feature)
 		if n.surface != "":
 			token = n.feature.split("")
 			ntype = token[0]
 			word = token[6]

		#temp = "データを処理中（ワード：%s，品詞：%s）" % (word, ntype)

		#if ntype== "名詞" or ntype=="動詞" or ntype=="形容詞":
if ntype == "名詞":
	print (word)#表示
	ff.write(word)#形態素解析した単語を１語ずつ書き出していく
	ff.write('　')#１語毎にスペースあける

n = n.next


mecabb(text)#引数入力
ff.close()#書き出したファイル閉じる
