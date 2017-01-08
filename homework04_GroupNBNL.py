#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "謝惟遠",
                "學號": "B05505009"},
            2: {"姓名":"張致瑜",
                "學號":"	b05505016"},
            3: {"姓名":"高晟霖",
                "學號":"	b05505015"},
            4: {"姓名":"林品均",
                "學號":"	b05505017"},            
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("./44100.wav")
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()


print(sound.getparams())
newSound = wave.open("./11025.wav", "wb")
newSound.setparams((nchannels, sampwidth, 11025, 110250, comptype, compname))

showAll = False # Show all data in raw string at once.
if showAll == True:
    tapeAll = sound.readframes(nframes)
else:
    for i in range(0, nframes, 4):
        waveData = sound.readframes(1)
        tapeClip = struct.unpack("<h", waveData)
        #print(type(tapeClip[0]))
        newSound.writeframes(struct.pack('h',int(tapeClip[0])))
sound.close()
newSound.close()
        


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b1 = b1.decode('big5')
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b2 = b2.decode()
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"
b3 = b3.decode('utf-16')
print('b1 = ', b1, 'b2 = ', b2, 'b3 = ', b3, sep = ', ')

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = s0.encode('cp950')
s_utf8 = s0.encode()
s_utf16 = s0.encode('utf-16')
print(s_cp950, s_utf8, s_utf16, sep = '\n')

# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
 #wifi
# (b). 哪一種傳輸方式較快速？
 #wifi
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。
 #手機A(HTC10):Bluetooth4.2   筆電B(Asus UX330):Bluetooth4.1
#理論傳輸速度:24Mbps
#照片檔案大小:2.9MB   理論花費時間:0.96秒 實際花費時間:75秒      實際傳輸速度:0.0394MBps=0.3157Mbps
#照片檔案大小:3.96MB  理論花費時間:1.31秒 實際花費時間:105秒     實際傳輸速度:0.0377MBps=0.3017Mbps
#照片檔案大小:2.96MB  理論花費時間:0.98秒 實際花費時間:75秒      實際傳輸速度:0.03946MBps=0.315Mbps
#差距如此大  可能原因為作業系統不同，傳輸速度受限，環境影響，品牌各自的裝置不同
