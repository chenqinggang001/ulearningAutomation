import time
 
timeStamp1 = 1557502800
timeStamp2 = 1616757806
timeStamp3 = 1616757847
timeStamp4 = 1616757890
timeStamp5 = 1616757951
timeStamp6 = 1616757987
timeStamp7 = 1616757818
timeStamp8 = 1616757863
timeStamp9 = 1616757911
timeStamp10 = 616757975
timeStamp11 = 1616757999
timeStamp12 = 1617196764
timeStamp13 = 1616758032
timeStamp14 = 1616758039
timeStamp15 = 1616758044
timeStamp16 = 1617196761
timeStamp17 = 1616757983
timeStamp18 = 1616758004
timeStamp19 = 1616758008
timeStamp20 = 1616758012
timeStamp21 = 1616757935
timeStamp22 = 1616757963
timeStamp23 = 1616758014
timeStamp24 = 1616757977
timeStamp25 = 1616757900
timeStamp26 = 1616757874
timeStamp27 = 1616757918
timeStamp28 = 1616757854
timeStamp29 = 1616757835
timeStamp30 = 1616757865

timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)