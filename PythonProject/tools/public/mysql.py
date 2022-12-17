import pymysql

host = '49.235.204.77'
user = 'tester'
password = 'Dr6getstqghsfDxcmQ'
database = 'dlcenter_sdk'
port = 4580

db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database=database,
                     port=port,
                     charset='utf8')
cursor = db.cursor()


def update_sql(sql):
    cursor.execute(sql)


def insert_sql(sql):
    cursor.execute(sql)


def delete_sql(sql):
    cursor.execute(sql)


def select_sql(table_select, fild_select='*', condition=''):
    sql = 'select %s from %s' % (fild_select, table_select)
    if condition != '':
        sql += ' where %s' % condition
    print(sql)
    cursor.execute(sql)
    return cursor.fetchall()


# 执行sql
def execute_sql(sql):
    cursor.execute(sql)


# 测试代码
if __name__ == '__main__':
    table = ''
    test_flag = 1
    if test_flag == 1:
        sql_user_table = 'SELECT table_name ' \
                         'FROM information_schema.STATISTICS ' \
                         'WHERE table_schema = \'dlcenter_sdk\' ' \
                         'AND table_name LIKE \'plat_user_login_%\' ' \
                         'group by table_name'
        execute_sql(sql_user_table)
        res_table = cursor.fetchall()
        print(type(res_table))
        print(res_table)
        for each in res_table:
            for element in each:
                table = element
                # sql_search_user = 'select * from %s where plat_user_name = \'13553349001\'' % table
                sql_search_user = 'select * from %s where idcard = \'440681199512243676\'' % table
                execute_sql(sql_search_user)
                res_search_user = cursor.fetchall()
                if len(res_search_user) != 0:
                    print(element, 'get')
                    print(res_search_user)
            # print('')

    test_flag = 0
    if test_flag == 1:
        table = 'plat_user_login_hh'
        # fild = 'uid'
        # condition = 'plat_user_name = \'13553349001\' ' \
        #             'or bind_phone = \'13553349001\''
        condition = 'idcard = \'440681199512243676\' '
        res_select = select_sql(table,
                                # fild,
                                condition)
        print(res_select)
