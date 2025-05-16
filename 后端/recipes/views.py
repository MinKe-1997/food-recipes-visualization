from django.shortcuts import render

# Create your views here.

import uuid
from collections import Counter
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.db.models import *
from recipes import models
import json
from django.core import serializers


# 登陆
def login(request):
    data = {}
    res = json.loads(request.body)
    password = res.get("password")
    name = res.get("name")
    print(name, password)
    use = models.User.objects.filter(name=name).filter(password=password).values()
    print(len(use))
    data["login"] = len(use)
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


# 注册
def zc(request):
    data = {}
    res = json.loads(request.body)
    password = res.get("password")
    name = res.get("name")

    print(f"Registering user: {name}, {password}")

    # 查找是否已存在用户
    user = models.User.objects.filter(name=name)
    if not user.exists():  # 改成 exists() 判断是否已存在
        # 对密码进行加密
        encrypted_password = make_password(password)

        # 创建并保存用户
        user = models.User(id=uuid.uuid1(), name=name, password=encrypted_password)
        user.save()

        print(f"User {name} created successfully.")
        zc = 1  # 注册成功
    else:
        print(f"User {name} already exists.")
        zc = 0  # 用户已存在，注册失败

    # 返回响应
    data["login"] = zc
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


def home(request):
    data = {}
    res = json.loads(request.body)
    name = res.get("type")

    # 获取前5张图片
    img = models.Menu.objects.filter(big_type=name).values("img")[:5]

    # 使用 Django ORM 聚合
    items = models.Menu.objects.filter(big_type=name).values('type').annotate(type_count=Count('type')).order_by(
        '-type_count')

    item = []
    for i in items:
        d = {"label": i['type']}
        item.append(d)

    data["img"] = list(img)
    data["items"] = list(item)
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


def info(request):
    res = json.loads(request.body)
    data = {}
    i = res.get("pageIndex")
    size = res.get("pageSize")
    name = res.get("name")
    big = res.get("value")
    num = res.get("num")

    # 聚合 big_type 并计算总数
    ll = models.Menu.objects.values('big_type').annotate(value=Count('big_type')).order_by('big_type')

    # 使用 Django ORM 进行过滤和分页
    filter_args = {}
    if name:
        filter_args['name__contains'] = name
    if big:
        filter_args['big_type__contains'] = big
    if num:
        filter_args['num'] = num

    li = models.Menu.objects.filter(**filter_args).order_by('type')[(i - 1) * size: i * size]
    total = models.Menu.objects.filter(**filter_args).count()

    item = [{"value": i['big_type'], "label": i['big_type']} for i in ll]

    data["items"] = item
    data["list"] = list(li.values())
    data["total"] = total
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


def echarts(request):
    data = {}

    # 聚合 big_type 的计数
    big = models.Menu.objects.values('big_type').annotate(value=Count('big_type')).order_by('-value')[:20]
    data["big"] = [{"name": i['big_type'], "value": i['value']} for i in big]

    # 聚合 type 的计数
    type = models.Menu.objects.values('type').annotate(value=Count('type')).order_by('-value')[:50]
    data["type"] = [{"name": i['type'], "value": i['value']} for i in type]

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


# 提取重复的聚合逻辑到一个辅助函数中
def get_num_data(queryset, group_by_field):
    # 返回前十个聚合结果
    return queryset.values(group_by_field).annotate(value=Count(group_by_field)).order_by('-value')[:10]


def echarts1(request):
    data = {}

    # 获取总数聚合数据
    num = get_num_data(models.Menu.objects.all(), 'num')
    data["num"] = [{"name": i['num'], "value": i['value']} for i in num]

    # 获取各大类的聚合数据，按 big_type 分类
    data["china"] = get_num_data(models.Menu.objects.filter(big_type='中国菜'), 'num')
    data["china"] = [{"name": i['num'], "value": i['value']} for i in data["china"]]

    data["wai"] = get_num_data(models.Menu.objects.filter(big_type='外国菜'), 'num')
    data["wai"] = [{"name": i['num'], "value": i['value']} for i in data["wai"]]

    data["ge"] = get_num_data(models.Menu.objects.filter(big_type='各地小吃'), 'num')
    data["ge"] = [{"name": i['num'], "value": i['value']} for i in data["ge"]]

    data["cs"] = get_num_data(models.Menu.objects.filter(big_type='菜式'), 'num')
    data["cs"] = [{"name": i['num'], "value": i['value']} for i in data["cs"]]

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


from django.db.models import Count
from django.http import JsonResponse


def get_menu_data(big_type=None, category_field='sc', limit=10):
    """
    获取菜单数据的通用函数，返回特定 big_type 的前 limit 条记录。
    使用 Django ORM 替代 raw SQL 查询。
    """
    filters = {f"{category_field}__contains": '万'}
    if big_type:
        filters["big_type"] = big_type

    # 使用 ORM 查询，按 name 分组并统计出现次数，按值排序
    return models.Menu.objects.filter(**filters).values('name').annotate(
        value=Count('name')
    ).order_by('-value')[:limit]


def echarts3(request):
    data = {}

    # 获取中国菜数据
    zg_data = get_menu_data(big_type='中国菜')
    data['zg'] = [{"name": item['name'], "value": item['value']} for item in zg_data]

    # 获取外国菜数据
    wg_data = get_menu_data(big_type='外国菜')
    data['wg'] = [{"name": item['name'], "value": item['value']} for item in wg_data]

    # 获取各地小吃数据
    gd_data = get_menu_data(big_type='各地小吃')
    data['gd'] = [{"name": item['name'], "value": item['value']} for item in gd_data]

    # 获取菜式数据
    cs_data = get_menu_data(big_type='菜式')
    data['cs'] = [{"name": item['name'], "value": item['value']} for item in cs_data]

    # 获取所有类别数据（取前20）
    sc_data = get_menu_data(limit=20)
    data['sc'] = [{"name": item['name'], "value": item['value']} for item in sc_data]

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


from django.db.models import Count, F
from django.http import JsonResponse


def get_menu_data2(big_type=None, category_field='cat', limit=10):
    """
    获取菜单数据的通用函数，返回特定 big_type 的前 limit 条记录。
    使用 Django ORM 替代 raw SQL 查询。
    """
    filters = {f"{category_field}__contains": '万'}
    if big_type:
        filters["big_type"] = big_type

    # 使用 ORM 查询，按 name 分组并统计出现次数，按值排序
    return models.Menu.objects.filter(**filters).values('name').annotate(
        value=Count('name')
    ).order_by('-value')[:limit]


def echarts4(request):
    data = {}

    # 获取中国菜数据
    zg_data = get_menu_data2(big_type='中国菜')
    data['zg'] = [{"name": item['name'], "value": item['value']} for item in zg_data]

    # 获取外国菜数据
    wg_data = get_menu_data2(big_type='外国菜')
    data['wg'] = [{"name": item['name'], "value": item['value']} for item in wg_data]

    # 获取各地小吃数据
    gd_data = get_menu_data2(big_type='各地小吃')
    data['gd'] = [{"name": item['name'], "value": item['value']} for item in gd_data]

    # 获取菜式数据
    cs_data = get_menu_data2(big_type='菜式')
    data['cs'] = [{"name": item['name'], "value": item['value']} for item in cs_data]

    # 获取所有类别数据（取前20）
    cat_data = get_menu_data2(limit=20)
    data['cat'] = [{"name": item['name'], "value": item['value']} for item in cat_data]

    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})


import pymysql


def echarts5(request):
    # 初始化响应数据
    data = {}

    # 获取请求的 JSON 数据
    res = json.loads(request.body)
    p = res.get("name")
    p = '%%' + p + '%%'  # 为了进行模糊查询（SQL LIKE 语法）

    # 使用 PyMySQL 连接到数据库
    connection = pymysql.connect(
        host='localhost',  # 替换为你的 MySQL 主机
        user='root',  # 替换为你的 MySQL 用户名
        password='minke1090461393',  # 替换为你的 MySQL 密码
        database='rent',  # 替换为你的数据库名
        charset='utf8mb4'
    )

    try:
        # 创建一个游标对象
        with connection.cursor() as cursor:
            # 第一个 SQL 查询：获取按 'zz' 分组的统计数据
            cursor.execute("""
                SELECT zz AS name, COUNT(zz) AS value
                FROM menu
                GROUP BY zz
                ORDER BY value DESC
                LIMIT 100
            """)
            name = cursor.fetchall()
            # 将查询结果转换为字典格式，并存入响应数据
            name_items = [{"name": item[0], "value": item[1]} for item in name]
            data["name"] = name_items  # 将 name 数据添加到响应中

            # 打印调试 SQL 查询
            print(f"SQL for name: {p}")

            # 第二个 SQL 查询：根据 'cat' 和 'peiliao' 来筛选和分组
            sql = """
                SELECT 
                    CAST(SUBSTRING_INDEX(MIN(cat), '万', 1) AS DECIMAL(10,1)) AS value, -- 使用 MIN 聚合函数
                    COUNT(DISTINCT name) AS count_name,
                    name,
                    MIN(id) AS id
                FROM menu
                WHERE LOCATE('万', cat) > 0 AND peiliao LIKE %s
                GROUP BY name
                ORDER BY value DESC
                LIMIT 10;

            """
            cursor.execute(sql, (p,))  # 通过参数化查询来避免 SQL 注入
            cat = cursor.fetchall()

            # 将查询结果转换为字典格式，并存入响应数据
            cat_items = [{"name": item[2], "value": item[0]} for item in cat]
            data["cat"] = cat_items  # 将 cat 数据添加到响应中

            # 返回 JSON 响应
            return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})

    except pymysql.MySQLError as e:
        # 捕获 MySQL 错误并返回 500 错误响应
        print(f"MySQL 错误: {e}")
        return JsonResponse({"error": "数据库错误"}, status=500)

    finally:
        # 关闭数据库连接
        connection.close()
