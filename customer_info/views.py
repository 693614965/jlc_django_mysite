from uuid import uuid1

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from .models import CustomerInfo


# 客户信息 新增
def add(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        home_address = request.POST.get('home_address')
        work_unit = request.POST.get('work_unit')
        education = request.POST.get('education')
        email = request.POST.get('email')
        qq = request.POST.get('qq')
        customer_info = CustomerInfo(id=uuid1(), code=code, name=name, age=age, mobile=mobile,
                                     home_address=home_address,
                                     work_unit=work_unit, education=education, email=email, qq=qq)
        customer_info.save()
        return JsonResponse({'success': True, 'id': customer_info.id})
    else:
        return JsonResponse({'success': False})


# 客户信息 更新
def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        code = request.POST.get('code')
        name = request.POST.get('name')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        home_address = request.POST.get('home_address')
        work_unit = request.POST.get('work_unit')
        education = request.POST.get('education')
        email = request.POST.get('email')
        qq = request.POST.get('qq')
        CustomerInfo.objects.filter(id=id).update(code=code, name=name, age=age, mobile=mobile,
                                                  home_address=home_address, work_unit=work_unit, education=education,
                                                  email=email, qq=qq)
        return JsonResponse({'success': True, 'id': id})
    else:
        return JsonResponse({'success': False})


# 客户信息 ID 查询
def get_by_id(request, id):
    customer_info = CustomerInfo.objects.filter(id=id)
    return HttpResponse(serialize('json', customer_info))


# 客户 获取个人信息
def get_personnel_info(request):
    json_data = {}
    try:
        username = request.session.get('username')
        customer_info = CustomerInfo.objects.filter(user_id=User.objects.get(username=username).id).first()
        json_data['success'] = True
        json_data['customerInfo'] = {
            'id': customer_info.id,
            'code': customer_info.code,
            'name': customer_info.name,
            'age': customer_info.age,
            'mobile': customer_info.mobile,
            'home_address': customer_info.home_address,
            'work_unit': customer_info.work_unit,
            'education': customer_info.education,
            'email': customer_info.email,
            'qq': customer_info.qq
        }
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), content_type='application/json')


# 客户信息 删除
def delete(request, id):
    print(id)
    CustomerInfo.objects.filter(id=id).delete()
    return JsonResponse({'success': True})


# 客户信息 分页查询
def list(request, page, page_size):
    print(page, page_size)
    customer_info_s = CustomerInfo.objects.all()
    return HttpResponse(serialize('json', customer_info_s))
