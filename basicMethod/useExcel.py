import pandas as pd
from config.getConfigInfo import *


# 获取指定列数据保存至列表中（数据驱动ddt）
def get_test_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name, keep_default_na=False, usecols=[3, 4, 5, 6])
    data_list = df.values.tolist()
    return data_list


# 获取所有数据保存至列表中
def get_dict_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name, keep_default_na=False)
    # 将数组对象转为list
    data_list = df.values.tolist()
    # 返回第一行数据
    return data_list[0]


# 获取所有列数据，组合为字典，再保存至列表中
def get_excel_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name, keep_default_na=False)
    data_list = []
    # 获取行号索引，并遍历
    for i in df.index.values:
        row_data = df.loc[i].to_dict()
        data_list.append(row_data)
    return data_list


if __name__ == "__main__":
    # print(get_excel_data(defaultTestDataFile, default_org_data_sheet_name))
    data = get_excel_data(defaultTestDataFile, default_org_data_sheet_name)
    print(data)
