__author__ = 'neavemj'



def degToDec(dms):
    deg = float(str(dms)[0:2])
    min = float(str(dms)[2:4])
    sec = float(str(dms)[4:8])
    print deg, min, sec
    dd = deg + (min/60) + (sec/3600)
    print dd

def degToDec2(dms):
    deg = float(str(dms)[0:3])
    min = float(str(dms)[3:5])
    sec = float(str(dms)[5:9])
    print deg, min, sec
    dd = deg + (min/60) + (sec/3600)
    print dd

degToDec2(1703351)