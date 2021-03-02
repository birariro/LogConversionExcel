import os

result = []
readfileName=[]
Conversion =["null","null","null","null","null"]
# 시간 , ip , url , query , body
# 로그 파일의 문자열을 가공한다.

def timeLog(logStr):
    #초기화
    Conversion[0]="empty"
    Conversion[1]="empty"
    Conversion[2]="empty"
    Conversion[3]="empty"
    Conversion[4]="empty"

    startChar = "[F] - "
    log = logStr[logStr.find(startChar)+len(startChar): -1]
    Conversion[0] = log
    return
def urlAndipLog(logStr):
    startChar = "info: "
    logStr = logStr[logStr.find(startChar)+len(startChar) : ]

    splitIndex = logStr.find(" ",logStr.find(" ")+1)
    urlLog = logStr[ 0 : splitIndex ]
    ipLog  = logStr[ splitIndex+1 : ]

    Conversion[1] = ipLog
    Conversion[2] = urlLog
 
    return
def queryLog(logStr):
    startChar = "query: {"
    endChar = "}"
    log = logStr[logStr.find(startChar)+len(startChar) : logStr.rfind(endChar)]
    Conversion[3] = log
   
    return
def bodyLog(logStr):
    startChar = "body:"
    log = logStr[logStr.find(startChar)+len(startChar) : -1]
    Conversion[4] = log
    return

def endLog():
    result.append(Conversion[:]) # 그냥 넣으면 깊은 복사가 된다. [:]슬라이싱으로 얇은 복사로 처리
    return


def logStringConversion(logStr):

    

    if "[F]" in logStr:
        timeLog(logStr)
    elif "info" in logStr:
        urlAndipLog(logStr)
    elif "query" in logStr:
        queryLog(logStr)
    elif "body" in logStr:
        bodyLog(logStr)
    elif "elapsed-time" in logStr:
        endLog()
 
    

# 로그 파일을 읽는다.
def logFileRead(target,LOG_FILE_PATH):
    logfile = open(LOG_FILE_PATH+target,'r')
    while True:
        line = logfile.readline()
        if not line: 
            break
        logStringConversion(line)
    logfile.close()


# 파일명에 .log 가 붙은 파일만 찾는다.
def select_logFile(oldfiles,LOG_FILE_PATH):
    fileList= os.listdir(LOG_FILE_PATH)

    for target in fileList:
        if ".log" in target: 
            # 이미 읽은적이있는 파일인지 검사
            isOverLap = isOverLapFile(oldfiles,target)
            if isOverLap :
                print(target+" 이미 읽은적 이있다.")
            else :
                print(target+" 읽기")
                readfileName.append(target[:])
                logFileRead(target,LOG_FILE_PATH)
            

def isOverLapFile(oldfiles,target):
    for oldfile in oldfiles:
        if target in oldfile:
            return True
    return False

def run(oldfiles,LOG_FILE_PATH):
 
    select_logFile(oldfiles,LOG_FILE_PATH)
    
    return result,readfileName