from Conf.Config import env_cfg
"""添加投放配置接口"""
# 动态读取数据前缀名会用到
API_NAME = 'add_ad_pass_config'

# 地址信息
uri_scheme = 'http'
endpoint = 'fxht.hnmengdou.com'
resource_path = '/admin.php/game_manager/ad_pass_config/add.html'

match env_cfg['env_code']:
    case 'test': env = 'test-'
    case 'pre': env = 'pre-'
    case 'prod': env = ''

url = uri_scheme + u'://' + env + endpoint + resource_path

# 请求报文参数
req_param = {
    "activate[pass_rate]": "1",
    "activate[pass_end]": "1",
    "activate[pass_status]": "1",
    "register[pass_rate]": "1",
    "register[pass_end]": "1",
    "register[pass_status]": "1",
    "pay[gap_time]": "1",
    "pay[pass_rate]": "1",
    "pay[pass_end]": "1",
    "pay[pass_status]": "1",
    "pay[start_time_hour]": "00",
    "pay[start_time_second]": "00",
    "pay[end_time_hour]": "00",
    "pay[end_time_second]": "00",
    "app_id": "58",
    "app_select_ckb": "1",
    "company_id": "1",
    "pass_type": "2",
    "pass_status": "0"
}

# 相应报文参数
res_param = {
    "code": 0,
    "msg": "",
    "data": "",
    "url": "",
    "wait": ""
}
