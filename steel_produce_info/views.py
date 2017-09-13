from uuid import uuid1

from django.http import HttpResponse, JsonResponse

from .models import SteelProduceInfo


# 新增 钢网产品信息
def add(request):
    json_data = {}
    try:
        steel_produce_info = SteelProduceInfo(id=uuid1(),
                                              spec='37.0cm X 47.0cm',
                                              area='19.0cm x 29.0cm',
                                              net_pay_price='50元/个',
                                              express_coll_price='90元/个',
                                              gross_weight='1.5KG')
        steel_produce_info.save()
        json_data['success'] = True
        json_data['id'] = steel_produce_info.id
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '保存异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 更新 钢网产品信息
def update(request):
    json_data = {}
    try:
        id = request.POST.get('id')
        spec = request.POST.get('spec')
        area = request.POST.get('area')
        net_pay_price = request.POST.get('net_pay_price')
        express_coll_price = request.POST.get('express_coll_price')
        gross_weight = request.POST.get('gross_weight')
        if id:
            SteelProduceInfo.objects.filter(id=id).update(spec=spec,
                                                          area=area,
                                                          net_pay_price=net_pay_price,
                                                          express_coll_price=express_coll_price,
                                                          gross_weight=gross_weight)
            json_data['success'] = True
            json_data['id'] = id
        else:
            json_data['success'] = False
            json_data['msg'] = 'ID 不存在'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '更新异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# ID 查询 钢网产品信息
def get_by_id(request, id):
    json_data = {}
    try:
        steel_produce_info = SteelProduceInfo.objects.get(id=id)
        steel_produce_info_list = {
            'id': steel_produce_info.id,
            'spec': steel_produce_info.spec,
            'area': steel_produce_info.area,
            'net_pay_price': steel_produce_info.net_pay_price,
            'express_coll_price': steel_produce_info.express_coll_price,
            'gross_weight': steel_produce_info.gross_weight
        }
        json_data['success'] = True
        json_data['steelProduceInfo'] = steel_produce_info_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 查询钢网产品信息
def list(request):
    json_data = {}
    try:
        steel_produce_info = SteelProduceInfo.objects.all()
        steel_produce_info_list = []
        for steel in steel_produce_info:
            steel_produce_info_list.append({
                'key': steel.id,
                'spec': steel.spec,
                'area': steel.area,
                'net_pay_price': steel.net_pay_price,
                'express_coll_price': steel.express_coll_price,
                'gross_weight': steel.gross_weight
            })
        json_data['success'] = True
        json_data['data'] = steel_produce_info_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')
