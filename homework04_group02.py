#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "邊鈞天",
                "學號": "B05505010"},
            2: {"姓名":"洪子惟",
                "學號":"B05505013"},
            3: {"姓名":"廖垣誠",
                "學號":"B05505014"},
            4: {"姓名":"黃保鑫",
                "學號":"B05505036"}
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。

import wave
import struct

'''
sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()


showAll = False # Show all data in raw string at once.

if showAll == False:
    tapeAll = sound.readframes(nframes)
    print(tapeAll)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        print(tapeClip)
'''
    

sourceSound = wave.open("./44100.wav", "rb")    
nchannels, sampwidth, framerate, nframes, comptype, compname = sourceSound.getparams()

targetSound = wave.open("./11025_group2.wav", "wb")
targetSound.setparams( (nchannels, sampwidth, framerate//4, nframes//4, comptype, compname) )

sampleValues = []

for i in range(0, nframes):
    waveData = sourceSound.readframes(1)
    tapeClip = struct.unpack("<h", waveData)
    sampleValues.append(tapeClip[0])
    

for i in range(0, nframes):
    if(i%4 == 0):
        waveData = struct.pack("h", sampleValues[i])
        targetSound.writeframes(waveData)
        
sourceSound.close()
targetSound.close()



# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print('b1:',b1.decode('cp950'))
print('b2:',b2.decode('utf-8'))
print('b3:',b3.decode('utf-16'))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"

s_cp950 = s0.encode('cp950')
s_utf8 = s0.encode('utf-8')
s_utf16 = s0.encode('utf-16')

print('s_cp950 = ',s_cp950)
print('s_utf8 = ',s_utf8)
print('s_utf16 = ',s_utf16)


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？ 
#      Wi-Fi
# (b). 哪一種傳輸方式較快速？ 
#      Wi-Fi
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
#
#手機型號： InFocus M370 
#藍芽規格： 4.1
#解析度： 1836x3264
#檔案大小： 1.31MB
#理論傳輸速度： 24Mbps (最高速度)
#理論傳輸時間： 0.437s ( 1.31MB * 8 / 24Mbps )
#實際傳輸時間： 6.30s (取3次平均)
#影響傳輸因素：
#  1. Wi-Fi
#  2. 微波爐
#  3. 2.4GHz的其他無線裝置
#  4. 障礙物(金屬、水泥)
