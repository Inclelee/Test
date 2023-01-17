from django.http import HttpResponse
from test_mode.models import Test


# 测试插入数据
def test_add_data(request):
    # 方法一：创建对象后，使用save()保存
    test_str = Test(test_str='test')    # 初始化Test类
    test_str.save()

    # 方法二：调用create()方法添加
    res = Test(test_str='test')
    print("res:", res, type(res))
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

    i = 0
    for var in list_data:
        # print(var)
        # print(var.test_str)
        res += var.test_str + "\n"
    for var_1 in res_data:
        i += 1
        print(i)
        print(var_1)
        print(type(var_1))
        res += str(i)
        if type(var_1) == Test:
            print(var_1.test_str)
            res += var_1.test_str + "\n"
        else:
            for var_2 in var_1:
                print(var_2.test_str)
                res += var_2.test_str + "\n"
    return HttpResponse("<p>" + res + "</p>")


# 测试修改数据
def test_update_data(request):
    test_data = Test.objects.filter(id=2).first()
    test_data.test_str = "update_test_2"
    test_data.save()
    print("Save:%s" % test_data.test_str)
    test_data = Test.objects.filter(id=3).update(test_str="update_test_3")      # update方法返回成功结果 成功：1 | 失败：0
    type(test_data)
    print("Save:%s" % test_data)
    return HttpResponse("<p>修改数据成功</p>")


# 测试删除数据
def test_delete_data(request):
    test_str = Test.objects.filter(id=4).delete()
    test_str.save()
    return HttpResponse("<p>添加数据成功</p>")
