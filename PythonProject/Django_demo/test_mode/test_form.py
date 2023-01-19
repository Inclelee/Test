from django import forms
from django.core.exceptions import ValidationError
from . import models


class RoleForm(forms.Form):
    plat_user_name = forms.CharField(label="平台账号")
    uid = forms.CharField(label="uid")
    role_name = forms.CharField(label="角色名称")
    role_id = forms.CharField(label="角色ID")
    role_level = forms.IntegerField(label="角色等级",
                                    min_value=1,
                                    error_messages={"min_value": "所填等级太小",
                                                    "required": "字段不可为空"})
