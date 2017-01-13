#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "朱信靂",
                "學號": "B05505004"},
            2: {"姓名":"彭偉倫",
                "學號":"B05505023"},
            3: {"姓名":"呂智凱",
                "學號":"B05505043"},
            4: {"姓名":"孫鼎皓",
                "學號":"B05505044"},
            5: {"姓名":"郭凱",
                "學號":"T05902112"},            
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()
#print(sound.getparams())
tapeClip_set=[]

showAll = False # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes):                       
        waveData = sound.readframes(1)
        #print(waveData)
        tapeClip = struct.unpack("<h", waveData)    #可否不用struct
        #print(tapeClip)
        tapeClip_set.append(tapeClip[0])
    
        
fixsound = wave.open("GroupGenius.wav","w")
fixsound.setparams((1,2,11025, 110250,'NONE','not compressed'))


for x in range(0,441000,4):
    new_tapeClip = struct.pack("h",tapeClip_set[x])
    fixsound.writeframes(new_tapeClip)

print(fixsound.getparams())
fixsound.close()       



# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

from codecs import encode, decode
print(decode(b1,"cp950"))
print(decode(b2,"utf8"))
print(decode(b3,"utf16"))




# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = b"\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp"
s_utf8 = b"\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88"
s_utf16 = b"\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a"

print(s0.encode("cp950"))
print(s0.encode("UTF-8"))
print(s0.encode("UTF-16"))

# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？wifi
#      This is due to the broadcast range of the two technologies.Bluetooth devices emit a signal that travels for about 30 feet,
#      while Wi-Fi signals travel about ten times as far. Wi-Fi devices need more power to generate a stronger signal.

# (b). 哪一種傳輸方式較快速？wifi

# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

#      理論上的傳輸速度大約是24~25Mbps,但我們的實驗數據：
#      實驗(1)0.69Mbps
#      實驗(2)0.67Mbps
#      實驗(3)0.75Mbps
#      可以看出明顯的比理論值慢了快40倍對此我們認為有以下幾種可能
#      (1)手機、筆電wifi干擾
#      (2)人聲
#      因為bluetooth是透過24GHz的微波傳遞，因此只要只要是透過電磁波傳遞的方式都有可能造成破壞性干涉
#      又我們認為wifi是最主要的干涉源
#      (3)附近金屬、水泥物質
#      (4)水

#你們推測的種種原因，應繼續做實驗証明其會造成干擾。(助教)

