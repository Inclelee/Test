import pandas
import os
import public.tools


default_data_path = os.path.pardir + '\\data\\data.xlsx'


# 读取excel文件
def read_excel_dict(file, **kwargs):
    data = pandas.read_excel(file, **kwargs)
    data_dict = data.to_dict('records')
    print('Read Excel:', data_dict)
    return data_dict


def read_excel(file, **kwargs):
    data = pandas.read_excel(file, **kwargs)
    # print(type(data))
    # print(data)
    return data


def make_insert_sql(data, table_name):
    sql_head = 'INSERT INTO `dlcenter_sdk`.`'+table_name+'` ('
    sql_values = ' VALUES ('
    sql = []
    # print(data.keys().values)
    for each in data.keys().values:
        sql_head = sql_head+'`%s`,' % each
        # print('sql_head:', sql_head)
    sql_head = sql_head[:-1:] + ')'
    num = 0

    for each in data.fillna(' ').values:            # 把空值全部替换后的DataFrame
        sql_tem = sql_values
        for value in each:
            # print('value:', value)
            # print('value_type:', type(value))
            if value != 'nan':
                if isinstance(value, str):
                    sql_tem = sql_tem+'\'%s\',' % value
                else:
                    sql_tem = sql_tem+'%s,' % int(value)
            else:
                sql_tem = sql_tem+'` `,'
            # print('sql_values:', sql_tem)
        sql_tem = sql_tem[:-1:] + ');'
        # print('sql_values:', sql_tem)
        sql.append(sql_head+sql_tem)
        # print('sql:', sql[num])
        num += 1
    # print('num:', num)
    return sql


# # 测试代码
if __name__ == '__main__':
    print('Data.py test')


# # 添加签名
# data = pandas.read_excel_dict('data.xlsx')
# data['sign'] = data["中文"] + '.aa.' + data["English"]
# data_dict = data.to_dict('records')
# print(data_dict)
