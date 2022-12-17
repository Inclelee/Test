from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import importlib
import logging

# 定义页面操作
SimpleActions = ['clear()', 'send_keys()', 'click()', 'submit()', 'size', 'text', 'is_displayed()', 'get_attribute()']
logger = logging.getLogger('main.page')


class Page(object):
    def __init__(self, driver, page):
        self.driver = driver
        self.page = page
        self.elements = get_page_elements(page)
        self.by = ()
        self.action = None

    # 获取元素定位 by 及操作 action
    def _get_page_elem(self, elem):
        # print('ele:', self.elements)
        for each in self.elements:
            if each['name'] == elem:
                self.by = each['by']
                if 'action' in each and each['action'] is not None:
                    self.action = each['action']
                else:
                    self.action = None

    def oper_elem(self, elem, args=None):
        self._get_page_elem(elem)
        # print(elem, args)
        cmd = self._selenium_cmd('find_element', args)
        # print(cmd)
        return eval(cmd)

    def oper_elems(self, elem, args=None):
        self._get_page_elem(elem)
        # print(elem, args)
        cmd = self._selenium_cmd('find_elements', args)
        return eval(cmd)

    # 拼接 selenium 查找命令，查找单个元素时find_type为'find_element'，多个元素时为'find_elements'
    def _selenium_cmd(self, find_type='find_element', args=None):
        cmd = 'self.driver.' + find_type + '(*self.by)'
        if self.action:
            if self.action in SimpleActions:
                cmd = cmd + '.' + self.action
                # print(cmd)
                if args:
                    cmd = cmd[:-1] + 'args' + ')'
                    # print(cmd)
        # print(cmd)
        return cmd


def get_page_elements(page):
    """动态加载页面定义文件，获取页面元素列表elements"""
    elements = None
    if page:
        try:
            m = importlib.import_module(page)
            elements = m.elements
        except Exception as e:
            logger.error('error info : %s' % e)
            logger.error('error reason : import UI elements error')
    return elements
