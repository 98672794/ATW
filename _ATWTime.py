import time # 引入time

def NowIsTime():    
    nowTime = int(time.time()) # 取得現在時間
    struct_time = time.localtime(nowTime) # 轉換成時間元組
    timeString = str(time.strftime("%Y%m%d%H%M%S", struct_time)) # 將時間元組轉換成想要的字串
    Now = timeString
    return Now
