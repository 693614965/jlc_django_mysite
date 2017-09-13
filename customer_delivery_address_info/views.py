from uuid import uuid1

from django.http import JsonResponse, HttpResponse

from .models import CustomerDeliveryAddress


# 新增
def add(request):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            link_man = request.POST.get('link_man')
            link_man_mobile = request.POST.get('link_man_mobile')
            province = request.POST.get('province')
            city = request.POST.get('city')
            area = request.POST.get('area')
            detail = request.POST.get('detail')
            customer_delivery_address_info = CustomerDeliveryAddress(id=uuid1(), link_man=link_man,
                                                                     link_man_mobile=link_man_mobile, province=province,
                                                                     city=city, area=area, detail=detail,
                                                                     customer_id=customer_id)
            customer_delivery_address_info.save()
            json_data['success'] = True
            json_data['id'] = customer_delivery_address_info.id
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '保存异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户收货地址 更新
def update(request):
    json_data = {}
    try:
        id = request.POST.get('id')
        if id:
            link_man = request.POST.get('link_man')
            link_man_mobile = request.POST.get('link_man_mobile')
            province = request.POST.get('province')
            city = request.POST.get('city')
            area = request.POST.get('area')
            detail = request.POST.get('detail')
            CustomerDeliveryAddress.objects.filter(id=id).update(link_man=link_man, link_man_mobile=link_man_mobile,
                                                                 province=province, city=city, area=area, detail=detail)
            json_data['success'] = True
            json_data['id'] = id
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '更新异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 删除
def delete(request, id):
    print(id)
    CustomerDeliveryAddress.objects.filter(id=id).delete()
    return JsonResponse({'success': True})


# id 查询
def get_by_id(request, id):
    json_data = {}
    try:
        customer_delivery_address = CustomerDeliveryAddress.objects.get(id=id)
        customer_delivery_address_list = {
            'id': customer_delivery_address.id,
            'link_man': customer_delivery_address.link_man,
            'link_man_mobile': customer_delivery_address.link_man_mobile,
            'province': customer_delivery_address.province,
            'city': customer_delivery_address.city,
            'area': customer_delivery_address.area,
            'detail': customer_delivery_address.detail
        }
        json_data['success'] = True
        json_data['customerDeliveryInfo'] = customer_delivery_address_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户查询自己收获地址
def customer_list(request):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        customer_delivery_address = CustomerDeliveryAddress.objects.filter(customer_id=customer_id).order_by(
            '-is_default')
        customer_delivery_address_list = []
        for customer_delivery in customer_delivery_address:
            customer_delivery_address_list.append(
                {'key': customer_delivery.id, 'link_man': customer_delivery.link_man,
                 'link_man_mobile': customer_delivery.link_man_mobile, 'province': customer_delivery.province,
                 'city': customer_delivery.city, 'area': customer_delivery.area, 'detail': customer_delivery.detail,
                 'is_default': customer_delivery.is_default})
        json_data['success'] = True
        json_data['data'] = customer_delivery_address_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), content_type='application/json')


# 设置 默认
def set_default(request, id):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            CustomerDeliveryAddress.objects.filter(customer_id=customer_id).update(is_default=False)
            CustomerDeliveryAddress.objects.filter(id=id).update(is_default=True)
            json_data['success'] = True
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
    return HttpResponse(JsonResponse(json_data), 'application/json')
