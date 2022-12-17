from selenium.webdriver.common.by import By

page_url = 'https://www.baidu.com/s'

# name: 每个元素+操作的唯一标识。一个元素可能由于操作不同，而要定义多个，但大部分只要定义一个。
# desc:元素+操作的描述。
# by:元素的定位方式，使用selenium的原生定位方式，不自己定义封装。
# ec: 等待元素出现的方式，这个暂时未用。
# action:元素的对应操作。使用原生的selenium动作方法，不自己定义封装。
# 初始化页面元素
elements = [
    {'name': 'result_list', 'desc': '结果列表', 'by': (By.XPATH, u'//*[@tpl="se_com_default"]'), 'ec': 'presence_of_all_elements_located', 'action': None},
    {'name': 'text', 'desc': '文本', 'by': (By.XPATH, u'//*[@tpl="se_com_default"]/div/div[1]/h3/a'), 'ec': 'presence_of_element_logcated', 'action': 'text'},
    {'name': 'link', 'desc': '链接', 'by': (By.XPATH, u'//*[@tpl="se_com_default"]/div/div[1]/h3/a'), 'ec': 'presence_of_element_logcated', 'action': 'href'},
]
