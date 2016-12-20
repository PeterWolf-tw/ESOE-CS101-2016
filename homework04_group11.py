#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "陳筱婷",
                "學號": "B05505034"},
            2: {"姓名":"黃晨怡",
                "學號":"B05505026"},
            3: {"姓名":"湯凱沂",
                "學號":"B05505037"},
            4: {"姓名":"劉沁雅",
                "學號":"B05505005"}
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav","rb")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

showAll = True # Show all data in raw string at once.
origin=()
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        origin = origin.append(tapeClip[0])
        
rewrite = wave.open("./11025.wav","wb")
rewrite.setparams((1,2,11025,11025,"NONE","not compressed"))

for i in range(0,nframes//4,4):
    redata = struct.pack("h",origin[i])
    rewrite.writeframes(redata)

rewrite.close()

# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print(b1.decode("big5"))
print(b2.decode("utf-8"))
print(b3.decode("utf-16"))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"

print(s0.encode("cp950"))
print(s0.encode("utf-8"))
print(s0.encode("utf-16"))

s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
       #Wifi
# (b). 哪一種傳輸方式較快速？
       #Wifi
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
       #型號:Sony Xperia Z5 compact 
       #規格:bluetooth 4.1 傳輸速度: 24Mbps
       #檔案大小:2.51MB
       #理論時間:0.837 秒
       #實際時間:6.03 秒
       #影響因素:<1>可能受干擾源干擾
       #        <2>雙方手機的硬體規格