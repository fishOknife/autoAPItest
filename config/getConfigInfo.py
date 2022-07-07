import os
import configparser

# 获取配置文件路径
parentPath = os.path.dirname(os.path.abspath(__file__)) + r"\config.ini"

# 读取配置文件
conf = configparser.ConfigParser()
conf.read(parentPath, encoding="utf-8")

# 读取服务器host
server_host = conf.get("serverInfo", "host")
# print(server_host)

# 读取测试数据
# defaultTestDataFile = conf.get("testData", "defaultDataFilePath")
# testDataFile = conf.get("testData", "testDataFilePath")
# print(defaultTestDataFile)
# print(testDataFile)

# 读取请求头
header = dict(conf.items("header"))

# 读取mysql信息
host = conf.get("mysql", "host")
port = conf.getint("mysql", "port")
user = conf.get("mysql", "user")
password = conf.get("mysql", "password")

# 读取url地址
add_org_url = conf.get("url", "add_org_url")
add_role_url = conf.get("url", "add_role_url")
add_position_url = conf.get("url", "add_position_url")
add_user_url = conf.get("url", "add_user_url")

# 读取sheet信息
default_org_data_sheet_name = conf.get("defaultDataSheetName", "org_data_sheet_name")
default_role_data_sheet_name = conf.get("defaultDataSheetName", "role_sheet_name")
default_position_data_sheet_name = conf.get("defaultDataSheetName", "position_sheet_name")
default_user_data_sheet_name = conf.get("defaultDataSheetName", "user_sheet_name")

if __name__ == '__main__':
    print(host)
