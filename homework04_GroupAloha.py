#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "陳冠妤",
                "學號": "B04204008"},
            2: {"姓名": "王元婷",
                "學號": "B03303054"},
            3: {"姓名": "許卿柔",
                "學號": "B03303094"},
            4: {"姓名": "蒯心柔",
                "學號": "B03303119"},
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

original= wave.open("./44100.wav","r")
nchannels, sampwidth, framerate, nframes, comptype, compname = original.getparams() #讀取格式訊息
data_save= []

showAll = False # Show all data in raw string at once.
if showAll == True:
    tapeAll = original.readframes(nframes) #讀取聲音數據
else:
    for i in range(0, nframes):
        waveData = original.readframes(1)
        tapeClip = struct.unpack("<h", waveData) #unpack二進數據還原成python數據
        data_save.append(tapeClip[0]) 
        #print (tapeClip)
        #len(data_save)

nchannels = 1
sampwidth = 2
framerate = 11025
nframes = 110250
comptype = "NONE"
compname = "not compressed"

new= wave.open("./11025","w")
new.setparams((nchannels, sampwidth, framerate, nframes,comptype, compname))

for x in range(0,nframes,4):
	newdata= struct.pack("h",data_save[x]) #轉成二進位數據
	new.writeframes(newdata)

#print(new.getframerate())
new.close()


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

b1= b1.decode("big5")
b2= b2.decode("utf-8")
b3= b3.decode("utf-16")
print(b1, b2, b3)

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"

s_cp950= s0.encode("cp950")
s_utf8= s0.encode("utf8")
s_utf16= s0.encode("utf16")
print(s_cp950, s_utf8, s_utf16)


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
# ans(a):Wifi
# (b). 哪一種傳輸方式較快速？
#ans(b):Wifi
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
#ans(c1):我的型號是4.0,對方型號為3.0,最高速度皆可達24Mbps；照片大小為3.2MB，傳輸時間理論值應為(3.2*8)/24=1.6(s)
#ans(c2):實際上花了約15秒傳送
#ans(c3):附近干擾源多:周圍有大鐵櫃,微波爐,電源；裝置本身硬碟品質。

#你覺得傳輸的時候，會用到硬碟嗎？那麼手機沒有硬碟的條件下，使用藍芽是否就提升了速度呢？(助教)
