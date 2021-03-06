# !/usr/bin/env python3
# -*- coding: utf8 -*-


crewDICT = {1: {"姓名":"翁維陽","學號":"B05505029"},
            2: {"姓名":"謝承軒","學號":"B05505051"},
            3: {"姓名":"曾子恩","學號":"B05505030"},
               {"姓名":"胡靖","學號":"B05505031"}
            }   

# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。
import wave
import struct

sound = wave.open("C:/Users/wyueng/Desktop/44100.wav", 'rb')
nchannels, sampwidth, framerate, nframes, comptype, compname = sound.getparams()
tapeAll=[]
showAll = True
if showAll == True:
    for i in range(nframes):
        tapeAll.append( sound.readframes(1))

sound.close()



new = wave.open("C:/Users/wyueng/Desktop/11025.wav", 'wb')
new.setparams((nchannels, sampwidth, framerate // 4, nframes // 4, comptype, compname))

for i in range(0, nframes ,4):
    
    new.writeframes(tapeAll[i])


new.close()
print("finish")

# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。
b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"
print(b1.decode("cp950"))
print(b2.decode("utf8"))
print(b3.decode("utf16"))
# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。
s0 = "計算機概論與程式設計"
s_cp950 = s0.encode("cp950")
s_utf8 = s0.encode("utf8")
s_utf16 = s0.encode("utf16")


# 第四題：請說明 Wifi 和 Bluetooth 之間...
# (a).
#Wifi較為耗電
# (b).
#Wifi較為快速
# (c).
#機台型號：iphone6s ; HTC New one M7
#藍牙規格：Bluetooth4.2 ; Bluetooth4.2
#照片檔案：解析度1920 × 1080
#       檔案大小266kB
#理論時間：理論上以Bluetooth4.2協定來說Basic Rate為3Mbps，約為0.375MBps，
#        因此理想上應只花費0.71秒即可完成傳輸。
#實際時間：2.21秒 (三次實測所得平均值)
#影響速率因素：(1)周圍有人在使用wifi，由於LAN所使用的頻段分佈在2.4Ghz附近，與藍牙相同，
#             推測可能因此使得傳輸速率下降。
    #          (2)環境周圍其他無線裝置的頻段干擾。
    #         (3)硬體之間本身有金屬影響到速率的傳輸。
    #        (4)藍牙晶片本身性質差異導致。