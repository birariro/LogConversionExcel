
from Slave import ReadLogFile
from Slave import ExcelUpdata
from Slave import ExcelCreate

# 생성될 엑셀 이름
SAVE_FILE_NAME = "test.xlsx"


#엑셀파일이 없다면 생성한다.
ExcelCreate.run(SAVE_FILE_NAME)

#로그파일을 읽는다.
#datas = 가공된 로그내용 , files=읽은 파일 이름
datas,files = ReadLogFile.run()


#로그정보를 시트에 저장한다.
ExcelUpdata.runLog(SAVE_FILE_NAME,datas)

#읽은 파일 제목을 시트에 저장한다.
ExcelUpdata.runfile(SAVE_FILE_NAME,files)

