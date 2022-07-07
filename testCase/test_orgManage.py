import pytest
import allure
from prepare.prepareTestData import *


@allure.feature('添加用户')
class TestOrgManageClass:
    # 机构管理
    @allure.story("添加用户")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', org_test_data)
    def test_org_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print("转为json：", json_data)
        if "deleteOrg" in api:
            res_data = requests.get(url, headers=header, params=json_data)
            assert response_data in res_data.text
        else:
            res_data = requests.post(url, headers=header, json=json_data)
            assert response_data in res_data.text

    @allure.story("角色管理")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', role_test_data)
    def test_role_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        res_data = requests.post(url, headers=header, json=json_data)
        assert response_data in res_data.text

    @allure.story("岗位管理")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', position_test_data)
    def test_position_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print(json_data)
        if "findAllPosition" in api:
            res_data = requests.get(url, headers=header, params=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "dicDetailAdd" in api:
            res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "updateDicDetail" in api:
            res_data = requests.put(url, headers=header, json=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "deleteDir" in api:
            res_data = requests.get(url, headers=header, params=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        else:
            print("没有接口：", api)

    @allure.story("机构用户管理")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', org_user_test_data)
    def test_org_user_manage(self, case_name, api, request_data, response_data):
        url = server_host + api
        json_data = json.loads(request_data)
        # print(json_data)
        if "findOrgUserList" in api:
            res_data = requests.get(url, headers=header)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "addUser" in api:
            res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "updateUser" in api:
            res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        elif "updateStatus" in api:
            res_data = requests.post(url, headers=header, json=json_data)
            # print(self.res_data)
            assert response_data in res_data.text
        else:
            print("没有接口：", api)


@allure.feature('订单管理')
class TestOrderManageClass:
    @allure.story("查询")
    @allure.title("{case_name}")
    @pytest.mark.parametrize('case_name,api,request_data,response_data', order_bpmId)
    def test_order_detail(self, case_name, api, request_data, response_data):
        # print(case_name)
        get_order_detail_url = server_host + api
        json_data = json.loads(request_data)
        res_data = requests.post(url=get_order_detail_url, headers=header, json=json_data)
        assert response_data in res_data.text


if __name__ == '__main__':
    # main方法参数：1、测试文件，可以不传 2、生成的临时json文件地址 3、执行前清空alluredir临时文件
    pytest.main(['testCase/test_orgManage.py', '--alluredir=../reportTemp', '--clean-alluredir'])
    # 1、./ reportTemp为临时文件目录，与main方法中的json文件地址一致 2、./testReport为生成报告存放目录，清空原文件
    os.system("allure generate ../reportTemp -o ../testReport --clean")

