import os
import pytest

if __name__ == "__main__":
    # main方法参数：1、测试文件，可以不传 2、生成的临时json文件地址 3、执行前清空alluredir临时文件
    # pytest.main(['testCase/testorgmanage.py', 'test_1.py', '--alluredir=./reportTemp', '--clean-alluredir'])
    # pytest.main(['--alluredir=./report/temp', '--clean-alluredir'])
    # 1、./ report/temp为临时文件目录，与main方法中的json文件地址一致 2、./testReport为生成报告存放目录，清空原文件
    # os.system("allure generate ./report/temp -o ./report/report --clean")
    # pytest.main(['testCase/usermanagement.py::TestQuireUser::test_quire_department_user', '--alluredir=./report/temp', '--clean-alluredir'])
    pytest.main(['testCase/usermanagement.py', '--alluredir=./report/temp', '--clean-alluredir'])
    # 1、./ reportTemp为临时文件目录，与main方法中的json文件地址一致 2、./testReport为生成报告存放目录，清空原文件
    os.system("allure generate ./report/temp -o ./report/report --clean")
