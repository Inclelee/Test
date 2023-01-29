from hashlib import md5,sha1


def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
    # return md5(s.encode().hexdigest())


def make_sha1(s, encoding='utf-8'):
    return sha1(s.encode(encoding)).hexdigest()


# 测试代码
if __name__ == '__main__':
    # android
    str_md5 = 'app_name=wzry&app_version=0.0.0.1.220310&channel_id=272453&co_id=1&device=869169028778036&device_mac=00:DB:1F:E2:CE:64&device_type=M973Q&device_uuid=387bb0cb-bfa5-74f2-47d2-c141758f23f7&game_id=183&log_imei=869169028778036&log_imei_ctime=2023-01-29 04:36:06&log_imei_file=869169028778036&log_imeifile_ctime=2023-01-29 04:36:06&log_mac=00:DB:1F:E2:CE:64&log_mac_ctime=2023-01-29 04:36:06&log_mac_file=00:DB:1F:E2:CE:64&log_macfile_ctime=2023-01-29 04:36:06&mac=00:DB:1F:E2:CE:64&network_type=wifi&orange_company_id=&package_name=com.zsqkand.game&package_type=android&package_version=20230110&reg_game_id=183&reg_mac=00:DB:1F:E2:CE:64&sdk_version=2.0.2.9&svn_version=1&system_type=android&system_version=9&uuid=387bb0cb-bfa5-74f2-47d2-c141758f23f7&webview_ua=Mozilla/5.0 (Linux; Android 9; M973Q Build/PQ3B.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36PRwalJXvvsXYWeJO'
    # str_md5 = 'app_name=zsqk&app_version=0.0.0.1.220310&channel_id=253721&co_id=1&device=000000000000000&device_mac=9A:26:B7:00:74:E8&device_type=Redmi K20 Pro&device_uuid=fe1911a4-f54f-44d3-e625-a175781d3cee&game_id=255&log_imei=000000000000000&log_imei_ctime=2023-01-29 10:03:03&log_imei_file=000000000000000&log_imeifile_ctime=2023-01-29 10:03:03&log_mac=9A:26:B7:00:74:E8&log_mac_ctime=2023-01-29 10:03:03&log_mac_file=9A:26:B7:00:74:E8&log_macfile_ctime=2023-01-29 10:03:03&mac=9A:26:B7:00:74:E8&network_type=wifi&orange_company_id=&package_name=com.zsqkand.game&package_type=android&package_version=20230110&reg_game_id=255&reg_mac=9A:26:B7:00:74:E8&sdk_version=2.0.2.9&svn_version=1&system_type=android&system_version=10&uuid=fe1911a4-f54f-44d3-e625-a175781d3cee&webview_ua=Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36pktRytdjDOenuSlG'

    # ios
    # str_md5 = ''

    res = make_md5(str_md5)
    print('md5:%s' % res)
