#데이터를 전처리 한다.

def run(IP_WHITELIST,UNNECESSARY_PATTERNS,datas):
    ipfilterResult = whiteListFilter(IP_WHITELIST,datas)
    result = UnnecessaryFilter(UNNECESSARY_PATTERNS,ipfilterResult)
    return result

def whiteListFilter(WHITELIST,datas):
    result=[]
    for data in datas:
        isWhite = isWhiteip(WHITELIST,data)
        if not isWhite:
           result.append(data) 
    return result

def isWhiteip(WHITELIST,data):
    for whiteIp in WHITELIST:
        if whiteIp in data[1]:
            return True
    
    return False


def UnnecessaryFilter(UNNECESSARY_PATTERNS,datas):
    result =[]
    for data in datas:
        isUnnecessary = isUnnecessaryLog(UNNECESSARY_PATTERNS,data)
        if not isUnnecessary:
           result.append(data) 

    return result

def isUnnecessaryLog(UNNECESSARY_PATTERNS,data):
    for Unnecessary_Pattern in UNNECESSARY_PATTERNS:
        if Unnecessary_Pattern[0] == data[2] and Unnecessary_Pattern[1] == data[3] and Unnecessary_Pattern[2] == data[4]:
            return True
    
    return False