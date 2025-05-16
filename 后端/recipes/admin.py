# Register your models here.

from django.contrib import admin  # 导入 Django 管理后台模块

# 导入当前应用的所有模型，这样它们就可以在管理后台中注册
from .models import *

# 设置管理后台的头部标题
admin.site.site_header = '美食菜谱后台管理'
# 设置管理后台在浏览器标签页中显示的标题
admin.site.site_title = '美食菜谱后台管理'
# 设置管理后台主页的标题
admin.site.index_title = '美食菜谱后台管理'

from django.contrib import admin
from .models import Menu, User
from django.utils.html import format_html


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'big_type', 'type', 'name', 'display_img')  # 添加 display_img 方法
    search_fields = ('name', 'big_type')
    list_filter = ('big_type', 'type')

    def display_img(self, obj):
        """如果 img 字段不为空，则显示图片链接"""
        if obj.img:
            return format_html('<img src="{}" width="50" height="50"/>', obj.img)
        return "-"

    display_img.short_description = "Image"  # 设置列标题


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password')
    search_fields = ('name',)


# 注册 Menu 和 User 模型到后台
admin.site.register(Menu, MenuAdmin)
admin.site.register(User, UserAdmin)
