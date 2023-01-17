from django.db import models
# Create your models here.
# 创建你的模型


# 新建应用相当于建库：库名=[应用名称]
# 新建类相当于新建表：表名=[应用名称]_[类名]
# 类名 =》 数据表名
# 字段 =》 数据表字段
class Test(models.Model):
    test_str = models.CharField(max_length=64)
    # user = models.CharField(max_length=20)
    # password = models.IntegerField()


class RoleInfo(models.Model):
    plat_user_name = models.CharField(max_length=64)
    uid = models.CharField(max_length=10)
    role_name = models.CharField(max_length=64)
    role_id = models.CharField(max_length=64)
    role_level = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField()
