from django.db import models

# Create your models here.
# 创建你的模块


# 类名 =》 数据表名
# 字段 =》 数据表字段
class Test(models.Model):
    test_str = models.CharField(max_length=20)
