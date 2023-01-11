from django.http import HttpResponse
from test_mode.models import Test


# 测试插入数据
def testdb(request):
    test_str = Test(test_str='test')    # 初始化Test类
    test_str.save()
    return HttpResponse("<p>添加数据成功</p>")
