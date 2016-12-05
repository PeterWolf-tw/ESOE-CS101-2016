# encoding: utf-8
# Python 團體作業(IV)
# 請將組員名單詳列如下，並將範例說明用的「王大錘」及其學號取代為你的組員。若你的組員超過三人，請自行加上。

crewDICT = {1: {"姓名": "曾冠維",
                "學號": "B05505008"},
            2: {"姓名": "林伯松",
                "學號": "B05505001"},
            3: {"姓名": "郭長霖",
                "學號": "B05505002"},
            4: {"姓名": "蔡秉言",
                "學號": "B05505050"},            
            }

# 第一題：請利用 wave 和 struct 套件讀出 44100.wav 的內容。該檔案的取樣率為 44100hz，請將其重新取樣為 11025hz並另存新檔。

import wave
import struct
sound = wave.open("/Users/wayne/Desktop/Python/44100.wav","r")
a,b,c,d,e,f = sound.getparams()

data_list = [] 

for i in range(0,d):
    str_data = sound.readframes(1)
    data_tuple = struct.unpack("<h",str_data) # 讀取wave檔案中的所有frames
    data_list.append(data_tuple[0])  # 將tuple中第零筆資料加到list後面

d = int((d/c)*11025)  # 設定新的frame number

new_sound = wave.open("/Users/wayne/Desktop/Python/new_wave.wav","w")
new_sound.setparams((a,b,11025,d,e,f)) # 設定頻率為11025Hz
print(new_sound.getparams())

for r in range(0,441000,4): # range(a,b,c) 傳回一個整數迭代器，從0到441000，每次跨越4個數字迭代
    new_data = struct.pack("h",data_list[r])
    new_sound.writeframesraw(new_data)
    # 想請問 writeframesraw 跟 writeframes 的差別，wave.py 說明中說 writeframesraw 比較好？
    
new_sound.close()

# 第二題：請查詢 Python3 的 decode() 文件，利用 Python3 的 decode() 將以下三個字串轉成中文字串並印出。

b1 = b"\xa5x\xa4j\xa4u\xac\xec"
b2 = b"\xe5\x8f\xb0\xe5\xa4\xa7\xe5\xb7\xa5\xe7\xa7\x91"
b3 = b"\xff\xfe\xf0S'Y\xe5]\xd1y"

b1= b1.decode("big5")
b2= b2.decode("utf-8")
b3= b3.decode("utf-16") 
#編碼結果：台大工科
print(b1, b2, b3)

# 第三題：請查詢 Python3 的 encode() 文件，利用 Python3 的 encode() 將以下的字串轉成 cp950, utf-8 和 utf-16 的編碼。

s0 = "計算機概論與程式設計"
s_cp950.encode("cp950")
s_cp950.encode("utf-8")
s_cp950.encode("utf-16")

#cp950編碼：b'\xadp\xba\xe2\xbe\xf7\xb7\xa7\xbd\xd7\xbbP\xb5{\xa6\xa1\xb3]\xadp'
#utf-8編碼：b'\xe8\xa8\x88\xe7\xae\x97\xe6\xa9\x9f\xe6\xa6\x82\xe8\xab\x96\xe8\x88\x87\xe7\xa8\x8b\xe5\xbc\x8f\xe8\xa8\xad\xe8\xa8\x88'
#utf-16編碼：b'\xff\xfe\x08\x8a\x97{_j\x82i\xd6\x8a\x07\x82\x0bz\x0f_-\x8a\x08\x8a'


"""第四題：請說明 Wifi 和 Bluetooth 之間..."""
"""(a). 哪一種傳輸方式較為耗電？"""
# Wifi比較耗電(雖然wifi通訊協定中沒有規定功率下限，但是整體)
"""(b). 哪一種傳輸方式較快速？"""
# Wifi比較快速。根據IEEE 802.11 Wifi 通訊協定，Wifi理論可達速率可達1.3Gbps，然而藍芽僅能達到
#大約2.0Mbps(以藍芽4.2為例，藍芽通訊協定並未被採認)，差了500倍以上。
"""(c). 請實際測試：請查出你的手機型號採用的 Bluetooth 規格，再用你的手機拍攝一張照片，
            並透過 Bluetooth 傳送該照片到朋友的手機裡。 考量到雙方手機的藍芽設備規格以及照
            片的解析度、檔案大小，理論上應該耗時多少時間完成傳送？而實際上又耗了多少時間進行
            傳送？ 最後並請列出所有可能影響傳送時間的因素。"""
# 手機使用bluetooth 4.0，照片大小 2.83 MB ，理論傳輸時間(1Mbps)為22.64秒，實際花費時間40秒。
# 影響因素：雙方設備硬體規格、軟體規格、地形、距離、無線電波干擾...等


