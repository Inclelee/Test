import pymysql

# test
host = '49.235.204.77'
user = 'tester'
password = 'Dr6getstqghsfDxcmQ'
database = 'dlcenter_role_report'
port = 4580

# dlcenter_sdk
# dlcenter_role_report

# localhost
# host = 'localhost'
# user = 'root'
# password = '123456'
# database = 'test_plat'
# port = 3306

db = pymysql.connect(host=host,
                     user=user,
                     password=password,
                     database=database,
                     port=port,
                     charset='utf8')
cursor = db.cursor()


def update_sql(table, key_value, condition='1'):
    sql = 'update %s set %s where %s' % (table, key_value, condition)
    print(sql)
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount, "record(s) affected")
    return cursor.rowcount


def insert_sql(table, key, value):
    sql = 'insert into %s (%s) values (%s)' % (table, key, value)
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount, "record(s) affected")
    return cursor.rowcount


def delete_sql(table, condition=' '):
    sql = 'delete from %s' % table
    if condition != '':
        sql += ' where %s' % condition
    print(sql)
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount, "record(s) affected")
    return cursor.rowcount


def select_sql(table, fild_select='*', condition=''):
    sql = 'select %s from %s' % (fild_select, table)
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
    test_flag = 0
    if test_flag == 1:      # 查询身份证所在表
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
    if test_flag == 1:      # 根据身份证查询平台账号id
        table = 'plat_user_login_hh'
        fild = 'id'
        # condition = 'plat_user_name = \'13553349001\' ' \
        #             'or bind_phone = \'13553349001\''
        condition = 'idcard = \'440681199512243676\' '
        res_select = select_sql(table,
                                fild,
                                condition)
        print(res_select)

    test_flag = 1
    if test_flag == 1:
        print('test-配置等级')

        level = 501
        table_update = 'dlcenter_role_report.role_upgrade_42 AS ru,' \
                'dlcenter_log.statis_role_183 AS sr,' \
                'dlcenter_sdk.account_red_packet_bind_role AS arpbr '
        data_key_value = 'arpbr.`level` = %i,sr.`level` = %i,ru.role_level = %i' % (level, level, level)
        condition_update = 'arpbr.role_id = \'hh114005\' ' \
                    'AND arpbr.role_id = ru.role_id ' \
                    'AND arpbr.role_id = sr.role_id ' \
                    'AND arpbr.app_id = 42 ' \
                    'AND arpbr.game_id = 183 ' \
                    'AND arpbr.game_id = sr.game_id ' \
                    'AND arpbr.app_id = ru.app_id;'
        update_sql(table_update, data_key_value, condition_update)
