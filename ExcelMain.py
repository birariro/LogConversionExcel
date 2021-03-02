
import os

from Slave import ReadLogFile
from Slave import ExcelUpdata
from Slave import ExcelCreate
from Slave import OverLapLogFileNames
from Slave import preprocessor
from Slave import Analysis

"""
Python Version = 3.9.2
pip install openpyxl (version 1.4.1)

"""


# 생성될 엑셀 이름
SAVE_FILE_NAME = "test.xlsx"
# 로그 파일 경로
LOG_FILE_PATH = os.getcwd()+"\\Logs\\"

# 화이트 리스트
IP_WHITELIST = ["14.206.18.218","223.39.215.205"]
#불필요한 로그의 패턴
UNNECESSARY_PATTERNS=[['GET /','null',' '],['POST /','null',' ']]





#엑셀파일이 없다면 생성한다.
ExcelCreate.run(SAVE_FILE_NAME)

#oldfiles = 이미 읽은적이 있는 로그파일 이름 들
oldfiles = OverLapLogFileNames.run(SAVE_FILE_NAME)

#로그파일을 읽는다.
#datas = 가공된 로그내용 , files=읽은 파일 이름
datas,files = ReadLogFile.run(oldfiles,LOG_FILE_PATH)

# 화이트 ip 로그 제거 및 불필요한 로그 제거
filterdata = preprocessor.run(IP_WHITELIST,UNNECESSARY_PATTERNS,datas)

#로그정보를 시트에 저장한다.
ExcelUpdata.runLog(SAVE_FILE_NAME,filterdata)

#읽은 파일 제목을 시트에 저장한다.
ExcelUpdata.runfile(SAVE_FILE_NAME,files)


#엑셀에있는 ip들의 어택 카운팅을 저장한다.
Analysis.attackCount(SAVE_FILE_NAME)
