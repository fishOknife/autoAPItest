import json
import requests

allUser = "http://test-rencaiku.tobowork.com:8026/api/v1/workingTime/user/showUserList"
header = {
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNTMxMDQ5MDAwMSIsInN1YiI6IntcImFjY291bnRcIjpcIjE1MzEwNDkwMDAxXCIsXCJjcmVhdGVkQnlcIjpcInN5c3RlbVwiLFwiZGF0YUxldmVsc1wiOltcIjBcIixcIjNcIl0sXCJkZXBhcnRtZW50Q29kZVwiOlwiVEVDSE5JQ0FMX0RFUFRcIixcImVtYWlsXCI6XCJ3dWhvbmdzZW5AdG9ib3NvZnQuY29tLmNuXCIsXCJlbXBOdW1cIjpcIjAxNzA5M1wiLFwiaGlyZURhdGVcIjpcIjIwMjEtMDItMDVcIixcImlkXCI6MjUsXCJsYWJvckNvc3RcIjpcIjIwMFwiLFwicGFzc3dvcmRcIjpcIjhhYWNkZjNjZTE4N2I5ODA5ZTRmNmJmNGM1NThiNmY2XCIsXCJwb3NpdGlvbkNvZGVcIjpcIlNPRlRfVEVTVFwiLFwicm9sZUNvZGVzXCI6W1wiQURNSU5cIixcIlBNXCJdLFwidGVsZXBob25lXCI6XCIxNTMxMDQ5MDAwMVwiLFwidXBkYXRlZEJ5XCI6XCLlkLTmtKrmo65cIixcInVzZXJOYW1lXCI6XCLlkLTmtKrmo65cIn0iLCJpc3MiOiJzeXN0ZW0iLCJpYXQiOjE2NTcyNDM5OTgsImV4cCI6MTY1NzI1NDc5OH0.rSLfZRPjNNrAdt-Gk1p94vBXh0loMVNZQSXJ1-vuA_4"
}
# data = {"position": "", "project": "", "status": "", "departmentCode": "", "userName": "", "startDate": "",
#         "endDate": "", "pageNum": 1, "pageSize": 800}
data = {}
responseData = requests.post(url=allUser, headers=header, json=data).text
totalNum = json.loads(responseData)['data']['total']

print(type(totalNum))
print(totalNum)

