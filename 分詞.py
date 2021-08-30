#!/usr/bin/env python
# coding: utf-8

# In[37]:


#簡轉繁
'''
from opencc import OpenCC
cc = OpenCC('s2twp')
text = '投票當天需攜帶投票通知單、國民身分證及印章，若沒有收到投票通知書，可以向戶籍所在地鄰長查詢投票所，印章則是可以用簽名代替，至於身分證則是一定要攜帶。'
'''
# -*- coding:utf8 -*-
import os
import jieba
import json
import simplejson

def splitSentence(inputFile):
    fin = open(inputFile, 'r',encoding="utf-8")                                  #以讀的方式打開文件
    global fout                                                
    global stop
    for eachLine in fin:
        eachLine_dict = simplejson.loads(eachLine)
        #print(eachLine_dict['text'])
        line = eachLine_dict['text'].strip()
        line=line.strip('\n')                                   #去掉多余空行
        wordList = list(jieba.cut(line))                        #用結巴分詞，對每行內容進行分詞     
    
        outStr = ''
        for word in wordList:#
            if len(word)>1:
                    outStr += word
                    outStr += ' '

        fout.write(outStr.strip())              #將分詞好的結果寫入到輸出文件
    fout.write('\n')
    fin.close()



import os
path = "wiki_zh" #資料夾目錄
folder1= os.listdir(path) #得到資料夾下的所有檔名稱
for folder in folder1:
    print(folder)
    fout = open(folder+'.txt', 'w',encoding='utf-8')
    files= os.listdir(path+"/"+folder)
    for file in files:
        print(file)
        splitSentence(path+"/"+folder+"/"+file)
    fout.close()
    

