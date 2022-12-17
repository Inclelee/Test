# test-helloworld
# from django.http import HttpResponse
from django.shortcuts import render


# def hello(request):
#     return HttpResponse('hello world!')
def page(request):
    context = {"hello": "Hello World!"}
    views_name = "测试页面"
    # 列表list
    views_list = ["测试数据0", "测试数据1", "测试数据2"]
    # 字典dict
    views_dict = {"key": "value"}

    # context['hello'] = 'Hello World!'
    # return render(request, 'page.html', context)    # 向模板提交数据
    return render(request, 'page.html', {"hello": context['hello'],
                                         "name": views_name,
                                         "views_list": views_list,
                                         "views_dict": views_dict}
                  )
