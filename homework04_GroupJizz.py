#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。
crewDICT = {1: {"姓名": "楊喬松",
                "學號": "B04505013"},
            2: {"姓名":"林奕明",
                "學號":"b05505040"},
            3: {"姓名":"林信和",
                "學號":"b05505007"},
            }


# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave

origSound = wave.open("./44100.wav", "rb")
nchannels, sampwidth, framerate, nframes, comptype, compname = origSound.getparams()

newSound = wave.open("./11025.wav", "wb")
newSound.setparams((1,2,11025, 110250,'NONE','not compressed'))

#the following loop will only write on the new sound wave each 4th sample from the original sound wave
for i in range(0, nframes):
    if i % 4 == 0:
        origData = origSound.readframes(1)
        newSound.writeframes(origData)
    else:
        origData = origSound.readframes(1)

newSound.close()


# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

print(b1.decode(encoding = "big5", errors = "strict"))
print(b2.decode(encoding = "utf-8", errors = "strict"))
print(b3.decode(encoding = "utf-16", errors = "strict"))

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = s0.encode(encoding = "cp950", errors = "strict")
s_utf8 = s0.encode(encoding = "utf-8", errors = "strict")
s_utf16 = s0.encode(encoding = "utf-16", errors = "strict")

#print(s_cp950,"\n",s_utf8,"\n",s_utf16)


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a). 哪一種傳輸方式較為耗電？
#      Wifi較為耗電.
# (b). 哪一種傳輸方式較快速？
#      Wifi較為快速.
# (c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
#      並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
#      片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
#      傳送？ 最後並請列出所有可能影響傳送時間的因素。

#你們的測試結果是？(助教)
