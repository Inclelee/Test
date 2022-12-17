import os
import unittest
import ddt
import json
import requests
from Comm.Data import read_excel
from main import TestCasePath
from APIs.Base_api import BaseAPI, check_result
from urllib import parse


test_data_file = os.path.join(TestCasePath, 'API\\Testdata\\add_ad_pass_config.xlsx')
# print('Excel File:', test_data_file)
test_data = read_excel(test_data_file)
# print('TestData:', test_data)
api_case = 'APIs.ad_pass_config.add_ad_pass_config'


@ddt.ddt
class TestAddAdPassConfig(unittest.TestCase):
    def setUp(self) -> None:
        # print('api:', api)
        self.api = BaseAPI(api_case)

    @ddt.data(*test_data)
    def test_add_ad_pass_config(self, test_data):
        """添加投放配置接口"""
        # print('API_Add_Ad_Pass_Config')
        api = self.api
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'hisiadmin_language=zh-cn; '
                      'PHPSESSID=4f66d0e17f5dc270c349725bb0adcba9; '
                      'hisihisi_admin_theme=0; '
                      'hisihisi_iframe=1',
            'Host': 'test-fxht.hnmengdou.com',
            'Proxy-Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest'
        }
        # print(test_data)
        # print('data:', parse.urlencode(test_data))
        # payload = api.payload(parse.urlencode(test_data))
        payload = api.payload(test_data)
        payload = parse.urlencode(payload)
        # print('payload:', payload)

        res = requests.post(api.url, data=payload, headers=headers)
        # print('type:', type(res))
        # parram : 参数放在链接
        # data  : 参数放在数据体

        # print('res:', res)
        # print(res.url)
        # print(res.headers)
        # print(res.reason)
        # print(res.text)
        print('****************************************************')
        self.assertEqual(res.status_code, 200)
        expected = api.load_expected(test_data)
        print('Expected:', expected)
        result = res.json()
        # print('result:', result)
        check_result(self, expected, result)
        print('****************************************************')


# 测试代码
if __name__ == '__main__':
    print('start')
    unittest.main()
