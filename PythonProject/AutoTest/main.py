import unittest
import os
import time
import logging
from Comm.Email import Email
from Comm.Log import log_init
from BeautifulReport import BeautifulReport
from appium import webdriver as app_web


# 初始化主程序日志
log_init()
logger = logging.getLogger('main')

# 定义各个目录
ProjectHome = os.path.split(os.path.realpath(__file__))[0]
# print(ProjectHome)
PageObjectPath = os.path.join(ProjectHome, "Page")
TestCasePath = os.path.join(ProjectHome, "Testcase")
ReportPath = os.path.join(ProjectHome, "Report")

# APP自动化
desired_caps = {
    'platformName': 'Android',      # 操作系统平台
    'platformVersion': '9',  # 移动操作系统版本
    # 'Udid': '358523021146419',       # 连接的物理设备的唯一设备标识符
    'deviceName': 'emulator-5558',               # 使用的移动设备或模拟器种类
    'appPackage': 'com.zsqkand.game',               # APP包名
    'appActivity': 'cn.lqgame.sdk.lqSdkDemo',              # apk的launcherActivity
    'unicodeKeyboard': True         # 使用unicodeKeyboard的编码方式来发送字符串
}

app_driver = app_web.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
app_driver.implicitly_wait(30)
app_driver.find_element(AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button').click()


# 汇总测试结果，作为邮件正文
def summary_format(result):
    summary = "\n" + u"<p>          测试结果汇总信息                </p>" + "\n" + \
                 u"<p> 开始时间: " + result['beginTime'] + u" </p>" + "\n" + \
                 u"<p> 运行时间: " + result['totalTime'] + u" </p>" + "\n" + \
                 u"<p> 执行用例数: " + str(result['testAll']) + u" </p>" + "\n" + \
                 u"<p> 通过用例数: " + str(result['testPass']) + u" </p>" + "\n" + \
                 u"<p> 失败用例数: " + str(result['testFail']) + u" </p>" + "\n" + \
                 u"<p> 忽略用例数: " + str(result['testSkip']) + u" </p>" + "\n"
    return summary


def send_email(file, context):
    title = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '自动化测试结果'
    mail = Email(title, context, file)
    send = mail.send_mail()
    if send:
        print('测试报告邮件发送成功')
    else:
        print('测试报告邮件发送失败')


# 加载测试用例
def get_suite(case_path=TestCasePath, rule="test*.py"):
    """加载所有测试用例"""
    unittest_suite = unittest.TestSuite()
    # print('case_path:', case_path)
    # discover_default = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    ui_path = os.path.join(case_path, "UI\\Case")                                                            # UI测试用例路径
    api_path = os.path.join(case_path, "API\\Case")                                                          # API测试用例路径
    other_path = os.path.join(case_path, "other\\Case")

    # 匹配测试模式
    test_mode = 3
    match test_mode:
        case 0:
            test_case_path = case_path          # 执行所有测试用例
        case 1:
            test_case_path = ui_path            # 仅执行UI测试用例
        case 2:
            test_case_path = api_path           # 仅执行API测试用例
        case 3:
            test_case_path = other_path         # 仅执行其他测试用例

    # 遍历所有符合条件的test_case
    discover = unittest.defaultTestLoader.discover(test_case_path, pattern=rule, top_level_dir=None)

    for each in discover:
        unittest_suite.addTests(each)       # 添加用例
        # print('Case:', each)

    return unittest_suite


# 执行用例，生成测试报告，并返回报告附件路径、邮件正文内容
def suite_run(unittest_suite):
    """执行所有用例，并把结果写入测试报告"""
    run_result = BeautifulReport(unittest_suite)

    now = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = now + '_report.html'
    run_result.report(filename=filename, description=now, report_dir=ReportPath)
    rpt_summary = summary_format(run_result.fields)
    return os.path.join(ReportPath, filename), rpt_summary


# 主程序
if __name__ == "__main__":
    run_test_flag = False
    if run_test_flag:
        suite = get_suite()  # 获取测试用例
        report_file, report_summary = suite_run(suite)  # 执行测试用例,并接收测试报告和测试汇总信息
        print(report_summary)
        send_flag = False
        if send_flag:
            # send_email(report_file, report_summary)     # 发送邮件
            logger.info('Info : send email')


    # 测试代码
    # title = '测试标题'
    # context = '测试正文'
    # file = {}
    # mail = Email(title, context, file)
    # send = mail.send_mail()
    # print(send)
