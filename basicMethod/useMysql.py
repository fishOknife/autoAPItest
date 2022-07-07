import pymysql
from config.getConfigInfo import *


def connect_mysql(db):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
    cursor = conn.cursor()
    return conn, cursor


def count_user_num():
    conn, cursor = connect_mysql("pingan_resume")
    count_user = "select count(1) from wts_user"
    cursor.execute(count_user)
    print("用户条数：", cursor.fetchone()[0])


# 查询表中所有的信息
def query_info(table_name):
    conn, cursor = connect_mysql("hami_db_stg")
    query_sql = f"select * from {table_name}"
    cursor.execute(query_sql)
    # print("这是查询结果", cursor.fetchall())
    fetch_result = cursor.fetchall()
    return fetch_result


# 传入表名、字段名、值，查询ID,返回list
def query_id_from_table(table_name, table_field, field_tuple):
    id_list = []
    conn, cursor = connect_mysql("hami_db_stg")
    query_sql = f"select id from {table_name} where {table_field} in %s" % (field_tuple,)
    cursor.execute(query_sql)
    fetch_result = cursor.fetchall()
    for i in range(0, len(fetch_result)):
        id_list.append(fetch_result[i][0])
    return id_list


# 删除业务系统、工作流机构信息
def del_org_data():
    conn, cursor = connect_mysql("hami_db_stg")
    # 查询机构id，保存至列表，删除工作流中的机构时需要用到
    org_id_tuple = ()
    inquire_org_id = 'SELECT id from hm_org WHERE tenant_id="autoTest";'
    cursor.execute(inquire_org_id)
    org_id = cursor.fetchall()
    for i in range(0, len(org_id)):
        # print(user_account[i])
        org_id_tuple = org_id_tuple + org_id[i]
    # print("机构id列表：", org_id_tuple)

    # 删除业务系统信息
    del_hm_org = 'DELETE FROM hm_org WHERE tenant_id="autoTest";'
    try:
        cursor.execute(del_hm_org)
        conn.commit()
        print("删除业务系统机构信息成功")
    except Exception as result:
        conn.rollback()
        print("删除业务系统机构信息失败", result)
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")

    # 删除工作流信息
    if org_id_tuple:
        conn, cursor = connect_mysql("hami_workflow_stg")
        del_sys_org_sql = f"delete from sys_org where CODE_ in {org_id_tuple}"
        try:
            cursor.execute(del_sys_org_sql)
            conn.commit()
            print("删除工作流机构信息成功")
        except Exception as result:
            conn.rollback()
            print("删除工作流机构信息失败", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭工作流数据库链接")
    else:
        print("查询机构ID列表为空，未删除工作流数据")


# 删除业务系统角色信息，角色菜单权限（角色信息未同步工作流，）
def del_role_data():
    conn, cursor = connect_mysql("hami_db_stg")
    # 查询机构id，保存至列表，删除工作流中的机构时需要用到
    role_id_tuple = ()
    inquire_role_id = 'SELECT id from hm_role WHERE tenant_id="autoTest";'
    cursor.execute(inquire_role_id)
    role_id = cursor.fetchall()
    for i in range(0, len(role_id)):
        # print(user_account[i])
        role_id_tuple = role_id_tuple + role_id[i]
    # print("机构id列表：", org_id_tuple)

    # 删除业务系统信息
    del_hm_role_menu = f"delete from hm_role_menu where role_id in {role_id_tuple}"
    del_hm_role = 'delete from hm_role WHERE tenant_id="autoTest";'
    try:
        cursor.execute(del_hm_role_menu)
        cursor.execute(del_hm_role)
        conn.commit()
        print("删除业务系统角色信息成功")
    except Exception as result:
        conn.rollback()
        print("删除业务系统角色信息失败，回滚", result)
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")


# 删除岗位信息（业务系统、工作流）
def del_position_data():
    conn, cursor = connect_mysql("hami_db_stg")
    # 删除业务系统岗位信息
    # 查询机构id，保存至列表，删除工作流中的机构时需要用到
    position_code_tuple = ()
    inquire_position_code = "SELECT detail_code FROM hm_dictionary_detail WHERE dic_id=4 AND remark LIKE '新增%';"
    cursor.execute(inquire_position_code)
    position_code = cursor.fetchall()
    for i in range(0, len(position_code)):
        # print(user_account[i])
        position_code_tuple = position_code_tuple + position_code[i]
    # print("机构id列表：", position_code_tuple)

    # 删除业务系统信息
    del_hm_position = 'DELETE FROM hm_dictionary_detail WHERE dic_id=4 AND remark LIKE "新增%";'
    try:
        cursor.execute(del_hm_position)
        conn.commit()
        print("删除业务系统岗位信息成功")
    except Exception as result:
        conn.rollback()
        print("删除业务系统岗位信息失败，回滚", result)
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")

    # 删除工作流信息
    if position_code_tuple:
        conn, cursor = connect_mysql("hami_workflow_stg")
        del_sys_org_rel_sql = f"delete from sys_org_rel where REL_CODE_ in {position_code_tuple}"
        try:
            cursor.execute(del_sys_org_rel_sql)
            conn.commit()
            print("删除工作流岗位信息成功")
        except Exception as result:
            conn.rollback()
            print("删除工作流岗位信息失败，回滚", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭工作流数据库链接")
    else:
        print("查询岗位CODE列表为空，未删除工作流数据")


# 删除业务系统、工作流机构用户信息
def del_org_user_data():
    conn, cursor = connect_mysql("hami_db_stg")
    # 查询account，保存至列表，删除工作流中的用户时需要用到
    user_account_tuple = ()
    inquire_user_account = 'SELECT account from hm_user WHERE tenant_id="autoTest";'
    cursor.execute(inquire_user_account)
    user_account = cursor.fetchall()
    for i in range(0, len(user_account)):
        # print(user_account[i])
        user_account_tuple = user_account_tuple + user_account[i]
    # print("机构用户账号列表：", user_account_tuple)

    # 删除业务系统信息
    del_hm_user_role = 'DELETE from hm_user_role WHERE user_id in (SELECT id FROM hm_user WHERE tenant_id="autoTest");'
    del_hm_user_position = 'DELETE from hm_user_position WHERE user_id in (SELECT id FROM hm_user WHERE tenant_id="autoTest");'
    del_hm_user = 'DELETE FROM hm_user WHERE tenant_id="autoTest";'
    try:
        cursor.execute(del_hm_user_role)
        cursor.execute(del_hm_user_position)
        cursor.execute(del_hm_user)
        conn.commit()
        print("删除业务系统机构用户信息成功")
    except Exception as result:
        conn.rollback()
        print("删除业务系统机构用户信息失败，回滚", result)
    finally:
        conn.close()
        cursor.close()
        print("关闭业务系统数据库链接")

    if user_account_tuple:
        # 删除工作流信息
        conn, cursor = connect_mysql("hami_workflow_stg")
        del_sys_user_sql = f"delete from sys_user where ACCOUNT_ in {user_account_tuple}"
        try:
            cursor.execute(del_sys_user_sql)
            conn.commit()
            print("删除工作流机构用户信息成功")
        except Exception as result:
            conn.rollback()
            print("删除工作流机构用户信息失败，回滚", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭工作流数据库链接")
    else:
        print("查询机构用户account列表为空，未删除工作流数据")


"""
class DelDBData:
    @staticmethod
    def connect_mysql(db):
        conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
        cursor = conn.cursor()
        return conn, cursor

    # 查询表中所有的信息
    @classmethod
    def query_info(cls, table_name):
        conn, cursor = cls.connect_mysql("hami_db_stg")
        query_sql = f"select * from {table_name}"
        cursor.execute(query_sql)
        # print("这是查询结果", cursor.fetchall())
        fetch_result = cursor.fetchall()
        return fetch_result

    # 传入表名、字段名、值，查询ID,返回list
    @classmethod
    def query_id_from_table(cls, table_name, field_name, values):
        id_list = []
        conn, cursor = cls.connect_mysql("hami_db_stg")
        query_sql = f"select id from {table_name} where {field_name} in %s" % (values,)
        cursor.execute(query_sql)
        fetch_result = cursor.fetchall()
        for i in range(0, len(fetch_result)):
            id_list.append(fetch_result[i][0])
        return id_list

    # 删除业务系统、工作流机构信息
    @classmethod
    def del_org_data(cls):
        conn, cursor = cls.connect_mysql("hami_db_stg")
        # 查询机构id，保存至列表，删除工作流中的机构时需要用到
        org_id_tuple = ()
        inquire_org_id = 'SELECT id from hm_org WHERE tenant_id="autoTest";'
        cursor.execute(inquire_org_id)
        org_id = cursor.fetchall()
        for i in range(0, len(org_id)):
            # print(user_account[i])
            org_id_tuple = org_id_tuple + org_id[i]
        # print("机构id列表：", org_id_tuple)

        # 删除业务系统信息
        del_hm_org = 'DELETE FROM hm_org WHERE tenant_id="autoTest";'
        try:
            cursor.execute(del_hm_org)
            conn.commit()
            print("删除业务系统机构信息成功")
        except Exception as result:
            conn.rollback()
            print("删除业务系统机构信息失败", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭业务系统数据库链接")

        # 删除工作流信息
        if org_id_tuple:
            conn, cursor = cls.connect_mysql("hami_workflow_stg")
            del_sys_org_sql = f"delete from sys_org where CODE_ in {org_id_tuple}"
            try:
                cursor.execute(del_sys_org_sql)
                conn.commit()
                print("删除工作流机构信息成功")
            except Exception as result:
                conn.rollback()
                print("删除工作流机构信息失败", result)
            finally:
                conn.close()
                cursor.close()
                print("关闭工作流数据库链接")
        else:
            print("查询机构ID列表为空，未删除工作流数据")

    # 删除业务系统角色信息，角色菜单权限（角色信息未同步工作流，）
    @classmethod
    def del_role_data(cls):
        conn, cursor = cls.connect_mysql("hami_db_stg")
        # 查询机构id，保存至列表，删除工作流中的机构时需要用到
        role_id_tuple = ()
        inquire_role_id = 'SELECT id from hm_role WHERE tenant_id="autoTest";'
        cursor.execute(inquire_role_id)
        role_id = cursor.fetchall()
        for i in range(0, len(role_id)):
            # print(user_account[i])
            role_id_tuple = role_id_tuple + role_id[i]
        # print("机构id列表：", org_id_tuple)

        # 删除业务系统信息
        del_hm_role_menu = f"delete from hm_role_menu where role_id in {role_id_tuple}"
        del_hm_role = 'delete from hm_role WHERE tenant_id="autoTest";'
        try:
            cursor.execute(del_hm_role_menu)
            cursor.execute(del_hm_role)
            conn.commit()
            print("删除业务系统角色信息成功")
        except Exception as result:
            conn.rollback()
            print("删除业务系统角色信息失败，回滚", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭业务系统数据库链接")

    # 删除岗位信息（业务系统、工作流）
    @classmethod
    def del_position_data(cls):
        conn, cursor = cls.connect_mysql("hami_db_stg")
        # 删除业务系统岗位信息
        # 查询机构id，保存至列表，删除工作流中的机构时需要用到
        position_code_tuple = ()
        inquire_position_code = "SELECT detail_code FROM hm_dictionary_detail WHERE dic_id=4 AND remark LIKE '新增%';"
        cursor.execute(inquire_position_code)
        position_code = cursor.fetchall()
        for i in range(0, len(position_code)):
            # print(user_account[i])
            position_code_tuple = position_code_tuple + position_code[i]
        # print("机构id列表：", position_code_tuple)

        # 删除业务系统信息
        del_hm_position = 'DELETE FROM hm_dictionary_detail WHERE dic_id=4 AND remark LIKE "新增%";'
        try:
            cursor.execute(del_hm_position)
            conn.commit()
            print("删除业务系统岗位信息成功")
        except Exception as result:
            conn.rollback()
            print("删除业务系统岗位信息失败，回滚", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭业务系统数据库链接")

        # 删除工作流信息
        if position_code_tuple:
            conn, cursor = cls.connect_mysql("hami_workflow_stg")
            del_sys_org_rel_sql = f"delete from sys_org_rel where REL_CODE_ in {position_code_tuple}"
            try:
                cursor.execute(del_sys_org_rel_sql)
                conn.commit()
                print("删除工作流岗位信息成功")
            except Exception as result:
                conn.rollback()
                print("删除工作流岗位信息失败，回滚", result)
            finally:
                conn.close()
                cursor.close()
                print("关闭工作流数据库链接")
        else:
            print("查询岗位CODE列表为空，未删除工作流数据")

    # 删除业务系统、工作流机构用户信息
    @classmethod
    def del_org_user_data(cls):
        conn, cursor = cls.connect_mysql("hami_db_stg")
        # 查询account，保存至列表，删除工作流中的用户时需要用到
        user_account_tuple = ()
        inquire_user_account = 'SELECT account from hm_user WHERE tenant_id="autoTest";'
        cursor.execute(inquire_user_account)
        user_account = cursor.fetchall()
        for i in range(0, len(user_account)):
            # print(user_account[i])
            user_account_tuple = user_account_tuple + user_account[i]
        # print("机构用户账号列表：", user_account_tuple)

        # 删除业务系统信息
        del_hm_user_role = 'DELETE from hm_user_role WHERE user_id in (SELECT id FROM hm_user WHERE tenant_id="autoTest");'
        del_hm_user_position = 'DELETE from hm_user_position WHERE user_id in (SELECT id FROM hm_user WHERE tenant_id="autoTest");'
        del_hm_user = 'DELETE FROM hm_user WHERE tenant_id="autoTest";'
        try:
            cursor.execute(del_hm_user_role)
            cursor.execute(del_hm_user_position)
            cursor.execute(del_hm_user)
            conn.commit()
            print("删除业务系统机构用户信息成功")
        except Exception as result:
            conn.rollback()
            print("删除业务系统机构用户信息失败，回滚", result)
        finally:
            conn.close()
            cursor.close()
            print("关闭业务系统数据库链接")

        if user_account_tuple:
            # 删除工作流信息
            conn, cursor = cls.connect_mysql("hami_workflow_stg")
            del_sys_user_sql = f"delete from sys_user where ACCOUNT_ in {user_account_tuple}"
            try:
                cursor.execute(del_sys_user_sql)
                conn.commit()
                print("删除工作流机构用户信息成功")
            except Exception as result:
                conn.rollback()
                print("删除工作流机构用户信息失败，回滚", result)
            finally:
                conn.close()
                cursor.close()
                print("关闭工作流数据库链接")
        else:
            print("查询机构用户account列表为空，未删除工作流数据")
"""

if __name__ == "__main__":
    count_user_num()
    # field_list = ("HM0A001", "HM0A002", "HM0A003", "HM0A004")
    # print(query_id_from_table("hm_org", "org_code", field_list))
    # query_org_code = ("GSB001", "GSB002", "GSB003", "GSB004", "GSB005", "GSB006", "GSB007", "GSB008", "GSB009")
    # queryResult = query_id_from_table("hm_org", "org_code", query_org_code)
    # print(queryResult)
    # del_org_data()
    # del_role_data()
    # del_org_user_data()
    # del_position_data()
    # query_info("hm_org")
    # DelDBData.connect_mysql("hami_db_stg")
    # pass
