# encoding: utf-8
# B05505008 python作業二

# 助教不好意思 我看不懂作業的要求，請問是要將課本習題引入做計算嗎？
# 是

# 作業 2-1 定義一個將二進位表示數轉為十進位制的函式

def convert(n):
    counter = len(n)
    box = list(n)
    x = 0
    r = int(counter)
    while r > 0:
        a = r
        b = r-1
        x += int(box[a])*pow(2,b)
    print(x)
    return None


