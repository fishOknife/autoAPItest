import pymysql
from config.getConfigInfo import *


# 连接数据库
def connect_mysql(db):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db)
    cursor = conn.cursor()
    return conn, cursor


# 用户查询
class QueryNumUser:
    def __init__(self):
        self.conn, self.cursor = connect_mysql("pingan_resume")

    # 查询用户总人数
    def search_all_user(self):
        count_user = "select count(1) from wts_user;"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("总用户条数：", search_result)
        return search_result

    # 查询岗位人数
    def search_user_by_positio(self, position):
        count_user = f"SELECT COUNT(1) FROM wts_user WHERE position_code='{position}';"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据岗位查询用户条数：", search_result)
        return search_result

    # 查询启用人数
    def search_user_by_status(self, status):
        count_user = f"SELECT COUNT(1) FROM wts_user WHERE status={status};"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据状态查询用户条数：", search_result)
        return search_result

    # 查询技术部人数
    def search_user_by_department(self, department_code):
        count_user = f"SELECT COUNT(1) FROM wts_user WHERE department_code='{department_code}';"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据部门查询用户条数：", search_result)
        return search_result

    # 查询项目成员人数
    def search_user_by_project(self, project_code):
        count_user = f"SELECT count(1) FROM wts_project_user wpu LEFT JOIN wts_user wu ON wpu.user_id=wu.id WHERE project_code={project_code};"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据项目查询成员条数：", search_result)
        return search_result

    def search_user_by_username(self, user_name):
        count_user = f"SELECT count(1) FROM wts_user WHERE user_name LIKE '%{user_name}%';"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据姓名查询条数：", search_result)
        return search_result

    def search_user_by_hire_date(self, start_date, end_date):
        count_user = f"SELECT count(1) FROM wts_user WHERE hire_date BETWEEN '{start_date}' AND '{end_date}';"
        self.cursor.execute(count_user)
        search_result = self.cursor.fetchone()[0]
        print("根据入职日期查询条数：", search_result)
        return search_result

    # 组合查询（将所有的查询条件组合在一起，可以替换以上查询函数）
    def query_info(self, position, status, department_code, project_code, user_name, start_date, end_date):
        query_sql = f"SELECT COUNT(DISTINCT wu.id) FROM wts_user wu " \
            f"LEFT JOIN wts_project_user wpu ON wu.id=wpu.user_id " \
            f"WHERE (position_code ='{position}' OR '{position}'='') " \
            f"AND (wu.status ='{status}' OR '{status}'='') " \
            f"AND (department_code = '{department_code}' OR '{department_code}'='') " \
            f"AND (project_code = '{project_code}' OR '{project_code}'='') " \
            f"AND (user_name like '%{user_name}%' OR '%{user_name}%'='') " \
            f"AND (hire_date BETWEEN '{start_date}' AND '{end_date}' OR '{start_date}'='')"
        self.cursor.execute(query_sql)
        search_result = self.cursor.fetchone()[0]
        print("查询结果:", search_result)
        # fetch_result = self.cursor.fetchone()
        return search_result


if __name__ == "__main__":
    query_user = QueryNumUser()
    query_user.query_info('', '', '', '', '', '', '')
