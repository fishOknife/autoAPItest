import json
import pytest
import allure
import requests
from config.getConfigInfo import *
from basicMethod import usemysql, useexcel

host_url = "http://test-rencaiku.tobowork.com:8026"
headers = {
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNTMxMDQ5MDAwMSIsInN1YiI6IntcImFjY291bnRcIjpcIjE1MzEwNDkwMDAxXCIsXCJjcmVhdGVkQnlcIjpcInN5c3RlbVwiLFwiZGF0YUxldmVsc1wiOltcIjBcIixcIjFcIl0sXCJkZXBhcnRtZW50Q29kZVwiOlwiVEVDSE5JQ0FMX0RFUFRcIixcImVtYWlsXCI6XCJ3dWhvbmdzZW5AdG9ib3NvZnQuY29tLmNuXCIsXCJlbXBOdW1cIjpcIjAxNzA5M1wiLFwiaGlyZURhdGVcIjpcIjIwMjEtMDItMDVcIixcImlkXCI6MjUsXCJsYWJvckNvc3RcIjpcIjIwMFwiLFwicGFzc3dvcmRcIjpcIjhhYWNkZjNjZTE4N2I5ODA5ZTRmNmJmNGM1NThiNmY2XCIsXCJwb3NpdGlvbkNvZGVcIjpcIlNPRlRfVEVTVFwiLFwicm9sZUNvZGVzXCI6W1wiQURNSU5cIixcIlBNXCJdLFwidGVsZXBob25lXCI6XCIxNTMxMDQ5MDAwMVwiLFwidXBkYXRlZEJ5XCI6XCLlkLTmtKrmo65cIixcInVzZXJOYW1lXCI6XCLlkLTmtKrmo65cIn0iLCJpc3MiOiJzeXN0ZW0iLCJpYXQiOjE2NTc1MTM3NjAsImV4cCI6MTY1NzUyNDU2MH0.pjo1gstqO7jmGoa2VpeWGElTg8gtD8zx-tYSWq5tmN8"
}
seach_test_data = useexcel.get_test_data(test_data_file, inquire_user_sheet_name)
query_user = usemysql.QueryNumUser()


@allure.feature('用户管理')
class TestQuireUser:

    @allure.story("用户查询")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', seach_test_data)
    def test_quire_one_project_user(self, case_name, api, request_data, response_data):
        # print("测试数据：", case_name, api, request_data, response_data)
        json_data = json.loads(request_data)
        # print("发送数据：", json_data)
        res_data = requests.post(url=host_url + api, headers=headers, json=json_data).text
        total_num = json.loads(res_data)['data']['total']
        assert total_num == query_user.query_info(json_data['position'], json_data['status'],
                                                  json_data['departmentCode'], json_data['project'],
                                                  json_data['userName'], json_data['startDate'],
                                                  json_data['endDate'])


if __name__ == '__main__':
    # main方法参数：1、测试文件，可以不传 2、生成的临时json文件地址 3、执行前清空alluredir临时文件
    pytest.main(['testCase/usermanagement.py', '--alluredir=./report/temp', '--clean-alluredir'])
    # 1、./ reportTemp为临时文件目录，与main方法中的json文件地址一致 2、./testReport为生成报告存放目录，清空原文件
    os.system("allure generate ./report/temp -o ./report/report --clean")
