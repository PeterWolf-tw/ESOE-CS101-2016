#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "鄭尊仁",
                "學號": "B05505039"},
            2: {"姓名":"沈奐宇",
                "學號":"b05505012"},
            3: {"姓名":"沈濂富",
                "學號":"b05505035"},
            4: {"姓名"："莊邵謙",
                "學號"："b04b02016"}


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

original= wave.open("./44100.wav","r")
nchannels, sampwidth, framerate, nframes, comptype, compname = original.getparams() #讀取格式訊息
data_save= []

showAll = False
if showAll == True:
    tapeAll = original.readframes(nframes)
else:
    for i in range(0, nframes):
        waveData = original.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        data_save.append(tapeClip[0])

nchannels=1
sampwidth=2
framerate=11025
nframes=110250
comptype="NONE"
compname="not compressed"

baru= wave.open("./11025.wav","w")
baru.setparams((nchannels,sampwidth,framerate,nframes,comptype,compname))

for x in range(0,nframes,4):
    barudata= struct.pack("h",data_save[x])
    baru.writeframes(barudata)

baru.close()

# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"
print(b1.decode('cp950','strict'))
print(b2.decode('utf_8','strict'))
print(b3.decode('utf_16','strict'))
# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
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
            #Samsung Galaxy A7(2016)藍牙規格爲4.1
            #檔案2.43MB
            #理論傳輸速度 24Mbps
            #實際傳輸所用時間 36.32s
            #理論所需時間 0.81s
            #其他電器用品也會干擾傳輸速度
            

