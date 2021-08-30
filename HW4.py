from opencc import OpenCC
cc = OpenCC('s2twp')

import os
path = "cut_word" #資料夾目錄
files= os.listdir(path) #得到資料夾下的所有檔名稱

document=[]
for file in files:
    print("Now INPUT file:"+file)
    words=''
    fin = open(path+"/"+file, 'r',encoding="utf-8")
    for eachLine in fin:
        words+=eachLine
    document.append(words)

word=cc.convert(document[0])
print(word)