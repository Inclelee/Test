import os
import unittest
import ddt
import logging
from selenium import webdriver
from time import sleep
from Page.BasePage import Page
from Comm.Log import grab_screen
from Comm.Data import read_excel
from main import TestCasePath


logger = logging.getLogger('main.baidu_search')
# 读取测试数据
file = os.path.join(TestCasePath, 'other/Testdata/baidu_search.xlsx')
test_data = read_excel(file)

PO_bd = 'Page.baidu.Baidu_base_page'
PO_search = 'Page.baidu.Baidu_search_page'


@ddt.ddt
class TestBaiduSearch(unittest.TestCase):
    """百度搜索测试"""
    def setUp(self) -> None:
        # print('UI setUp')
        self.driver = webdriver.Chrome()
        self.count = 0
        self.result = []

    def tearDown(self) -> None:
        # print('UI tearDown')
        sleep(1)
        self.driver.quit()

    # def test_check_baidu_ui(self):
    #     print('check baidu UI')

    @ddt.data(*test_data)
    def test_baidu_search(self, test_data):
        """百度搜索测试"""
        print('UI_Test_baidu_search')
        url = 'http://www.baidu.com'
        keyword = test_data['keyword']
        self.driver.implicitly_wait(5)

        try:
            self.driver.get(url)
            bd = Page(self.driver, PO_bd)
            bd_search = Page(self.driver, PO_search)
            # print('bd:', bd)
            # print('bd_search:', bd_search)
            # print(keyword)
            sleep(2)
            bd.oper_elem('search_input', keyword)
            sleep(2)
            bd.oper_elem('search_button')

            list_res = bd_search.oper_elems('result_list')
            print('list_res:', list_res)

            for each in list_res:
                self.count += 1
                page_each = Page(each, PO_search)
                name = page_each.oper_elem('text')
                link = page_each.oper_elem('link')
                self.result.append([name, link])
                # print('Page_each', each)
                # print('name:', name)
                # print('link:', link)
        except Exception as E:
            logger.error('error info : %s' % E)
            grab_screen(test_data['keyword'])
        # print('data:', test_data)
        grab_screen(test_data['keyword'])

        # self.assertEqual(test_data['count'], self.count)
        # print(self.result)
