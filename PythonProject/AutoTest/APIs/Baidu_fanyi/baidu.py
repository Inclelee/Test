"""百度通用翻译接口"""
# 动态读取数据前缀名会用到
API_NAME = 'fanyi'

# 地址信息
uri_scheme = 'http'                                     # 请求协议
endpoint = 'api.fanyi.baidu.com'                        # 请求地址
resource_path = '/api/trans/vip/translate'              # 接口目录
url = uri_scheme + u'://' + endpoint + resource_path    # 拼接成请求链接

# 基本不变的参数
_from = 'zh'    # 源文语言
_to = 'en'      # 译文语言

# 请求报文参数
req_param = {
    "q": "",        # 请求翻译query,UTF-8
    "from": _from,   # 源文语言
    "to": _to,      # 译文语言
    "appid": "",    # APP ID
    "salt": "",     # 随机数
    "sign": ""      # 签名，appid+q+salt+密钥 的MD5值
}

# 响应报文参数
res_param = {
    "from": _from,
    "to": _to,
    "trans_result": [
        {
            "src": "This is the 1st paragraph",
            "dst": "这是第一段"
        },
        {
            "src": "This is the 2nd paragraph",
            "dst": "这是第二段"
        }
    ]
}