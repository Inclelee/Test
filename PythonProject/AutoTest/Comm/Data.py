import pandas


# 读取excel文件
def read_excel(file, **kwargs):
    data_dict = []
    # try:
    data = pandas.read_excel(file, **kwargs).fillna('')
    data_dict = data.to_dict('records')
    # print('Read Excel:', data_dict)
    # except ValueError:
    #     raise ValueError("Read excel file failed: %s" % ValueError)
    # finally:
    return data_dict


# # 测试代码
# sheet1 = read_excel('data.xlsx')
# sheet2 = read_excel('data.xlsx', sheet_name='Sheet2')
# print(sheet1)
# print(sheet2)

# # 添加签名
# data = pandas.read_excel('data.xlsx')
# data['sign'] = data["中文"] + '.aa.' + data["English"]
# data_dict = data.to_dict('records')
# print(data_dict)
