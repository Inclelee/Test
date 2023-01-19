from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
# 使用FBV方式
# def login_fbv(request):
#     if request.method == "GET":
#         return HttpResponse("登录成功")
#     elif request.method == "POST":
#         pass


# 使用CBV方式
# class LoginView(View):                  # 需要继承自View类
#     def get(self, request):
#         return HttpResponse("登录成功")
#
#     def post(self, request):
#         pass

def fbv_test(request):
    context = {}
    context['hello'] = 'hello world'
    # print(context['hello'])
    return render(request, 'upgrade.html', context)
