import os.path
import time
from Conf.Config import log_cfg
from PIL import ImageGrab

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

# 测试代码
grab_screen('test')