import os
import logging
# from Conf.Config import log_cfg
from logging.handlers import TimedRotatingFileHandler
import os.path
import time
from Conf.Config import log_cfg
from PIL import ImageGrab

_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

_log_level = eval(log_cfg['log_level'])
_log_path = log_cfg['log_path']
_log_format = log_cfg['log_format']

_log_file = os.path.join(_BaseHome, _log_path, 'log.log')


def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)

    # TimedRotatingFileHandler 参数简介
    # filename 日志文件名
    # when 切割条件：周（W）、天（D）、时（H）、分（M）、秒（S）
    # interval 间隔：when的值
    # backupCount 日志备份数量：超过数量会把最早的删除，从而实现滚动删除
    # 如下：日志文件名为 _log_file ，每天生成一个日志文件，并保留7天内的日志
    handler = TimedRotatingFileHandler(filename=_log_file, when="D", interval=1, backupCount=7)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # 在控制台中打印日志
    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)

# #######################测试日志效果#######################
# log_init()
# logger = logging.getLogger('main')
# logger.info('---log test---')
##########################################################


_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
_log_path = log_cfg['log_path']


# 获取日期时间
_today = time.strftime("%Y%m%d")
# 截图文件存放路径
_screen_path = os.path.join(_BaseHome, _log_path, 'Screen', _today)


# 截屏操作
def grab_screen(name):
    t = time.time()
    # 截屏，无参数默认全屏
    png = ImageGrab.grab()
    # 如果找不到路径，则创建文件夹
    if not os.path.exists(_screen_path):
        os.makedirs(_screen_path)
    image_name = os.path.join(_screen_path, name)
    png.save('%s_%s.png' % (image_name, str(round(t * 1000))))

# #######################测试截图效果#######################
# grab_screen('test')
##########################################################
