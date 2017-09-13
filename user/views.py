from uuid import uuid1

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.template import loader

from customer_info.models import CustomerInfo


# 用户登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = auth.authenticate(username=username, password=password)  # user 验证
        if user is not None and user.is_active:
            auth.login(request, user)  # user 登录
            # 封装 session
            user = User.objects.get(username=username)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            customer_info = CustomerInfo.objects.get(user_id=user.id)
            request.session['customer_id'] = customer_info.id

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'msg': '验证失败!'})
    else:
        return HttpResponse(loader.get_template('login.html').render({}, request))


# 用户 注册
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({'success': False, 'msg': '用户名已经存在!'})
        user = User.objects.create_user(username=username, password=password, email=email)
        print(user.id)
        customer_info = CustomerInfo()
        customer_info.id = uuid1()
        customer_info.email = email
        customer_info.user_id = user.id
        customer_info.save()
        return JsonResponse({'success': True})
    else:
        return HttpResponse(loader.get_template('register.html').render({}, request))


# 用户 列表
def user_list(request):
    users = User.objects.all()
    json_data = {}
    try:
        json_data['success'] = True
        users_list = []
        for user in users:
            users_list.append({'id': user.id, 'username': user.username})
        json_data['data'] = users_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
    return HttpResponse(JsonResponse(json_data), content_type='application/json')
