#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "郭明昇",
                "學號": "B02610037"},
            2: {"姓名": "沈智暐",
                "學號": "B02610044"},
            3: {"姓名": "黃子傑",
                "學號": "B05505038"},
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()

showAll = True # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        print(tapeClip)


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"
print(b1.decode('big5'))
print(b2.decode('utf-8'))
print(b3.decode('utf-16'))
    
# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = s0.encode('cp950')
print(s_cp950)
s_utf8 = s0.encode('utf-8')
print(s_utf8)
s_utf16 = s0.encode('utf-16')
print(s_utf16)


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
       #Wifi

# (b). 哪一種傳輸方式較快速？
       #Wifi

# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

#手機型號ASUS ZenFone2 藍牙裝置V4.0 傳輸速度最大24Mbps
#檔案大小：0.92MB
#理論耗時：0.322秒
#實際耗時：6.12秒
#影響原因：(1)附近干擾源多：有其他使用2.4GHz或5GHz波段的無線裝置
#                           例如：鄰居家的Wifi無線基地台、沒關掉Wifi連線的筆電
#          (2)裝置本身硬碟品質

#請証明Wifi 的開/關和的硬碟的品質如何影響傳輸速度。(助教)
