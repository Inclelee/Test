from django.http import HttpResponse
from test_mode.models import Test


# 测试插入数据
def test_add_data(request):
    test_str = Test(test_str='test')    # 初始化Test类
    test_str.save()
    return HttpResponse("<p>添加数据成功</p>")

# 测试查询数据
def test_search_data(request):
    res = ""
    res_data = []

    # 获取所有数据
    list_data = Test.objects.all()
    res_data.append(Test.objects.filter(id=1))
    res_data.append(Test.objects.get(id=1))
    res_data.append(Test.objects.order_by('test_str')[0:2])
    res_data.append(Test.objects.order_by('id'))
    res_data.append(Test.objects.filter(test_str="test").order_by('id'))

    for var in list_data:
        # print(var)
        # print(var.test_str)
        res += var.test_str + "\n"
    for var_1 in res_data:
        print(var_1)
        # print(type(var))
        for var_2 in var_1:
            print(var_2.test_str)
            res += var_2.test_str + "\n"
    return HttpResponse("<p>" + res + "</p>")
