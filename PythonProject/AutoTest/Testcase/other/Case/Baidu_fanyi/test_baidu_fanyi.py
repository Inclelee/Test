import os
import unittest
import ddt
import random
import json
import requests
from time import sleep
from Comm.Data import read_excel
from Comm.Encryption import make_md5
from main import TestCasePath
from APIs.Base_api import BaseAPI, check_result

# 普通个人的百度翻译接口，设置appid和appkey（密钥）
app_id = "20220524001227222"
app_key = "SLnY2_kMRjcFelyY8E5M"

# 获取测试数据
file = os.path.join(TestCasePath, 'other\\Testdata\\baidu_fanyi.xlsx')
print('Excel File:', file)
test_data = read_excel(file)
print('TestData:', test_data)
api = 'APIs.Baidu_fanyi.baidu'      # 用于import_module动态导入的文件路径
# query长度在 6000 bytes 以内（汉字约为输入参数 2000 个）


@ddt.ddt
class TestBaiduFanyi(unittest.TestCase):
    """百度翻译接口测试"""
    def setUp(self):
        # print('api:', api)
        self.api = BaseAPI(api)

    # def test_check_baidu_fanyi(self):
    #     print('check baidu fanyi')

    @ddt.data(*test_data)
    def test_baidu_fanyi(self, test_data):
        """百度翻译接口测试"""
        # print('API_Test_baidu_fanyi')
        api = self.api

        # Build test_data 构建请求参数，这是些动态参数，在这里计算
        test_data['fanyi.req.appid'] = app_id
        salt = str(random.randint(32768, 65536))
        test_data['fanyi.req.salt'] = salt
        sign = app_id + test_data['fanyi.req.q'] + salt + app_key
        # print(sign)
        sign = make_md5(sign)
        test_data['fanyi.req.sign'] = sign

        # Build request 构建请求报文
        headers = {'Content-Type': 'application/x-www-from-urlencoded'}     # 请求头
        payload = api.payload(test_data)                                    # 请求参数
        # print('payload:\n', payload)

        # Send request 发送请求报文，接受响应报文
        res = requests.post(api.url, params=payload, headers=headers)
        result = res.json()
        expected = api.load_expected(test_data)
        # print('result:', result,'\nexpected:', expected)
        self.assertEqual(res.status_code, 200)
        check_result(self, expected, result)

        sleep(0.5)


# 测试代码
if __name__ == '__main__':
    print('start')
    unittest.main()
