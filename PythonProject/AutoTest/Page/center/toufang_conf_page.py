from selenium.webdriver.common.by import By

page_url = 'http://test-fxht.hnmengdou.com/admin.php/system/index/index.html'

elements = [
    {
        'name': 'add_button',
        'desc': '添加按钮',
        'by': (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/a'),
        'action': 'click()'
    }
]

"""
    {
        'name': '元素名', 
        'desc': '描述',
        'by': (By.方法, '属性'), 
        'action': '操作'
    }
"""
