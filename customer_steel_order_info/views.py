from uuid import uuid1

from django.http import HttpResponse, JsonResponse

from steel_produce_info.models import SteelProduceInfo
from .models import CustomerSteelOrderInfo


def add(request):
    json_data = {}
    try:
        # 客户选择 的PCB 订单 （只有在PCB订单的基础上 才可以下钢网订单）
        customer_pcb_order_id = request.POST.get('customer_pcb_order_id')
        # 客户选择的钢网产品
        steel_produce_info_id = request.POST.get('steel_produce_info_id')
        print(customer_pcb_order_id, steel_produce_info_id)
        # 钢网下单属性
        steel_number = request.POST.get('steel_number')  # 下单钢网数目
        required_pack = request.POST.get('required_pack')  # 包装要求
        required_receipt_and_delivery_note = request.POST.get('required_receipt_and_delivery_note')  # 是否需要收据和送货单
        steel_use = request.POST.get('steel_use')  # 用途
        required_mark = request.POST.get('required_mark')  # MARK要求
        polishing_process = request.POST.get('polishing_process')  # 抛光工艺
        required_engineering_process = request.POST.get('required_engineering_process')  # 工程处理要求
        remark = request.POST.get('remark')  # 备注
        # 查询钢网产品
        steel_produce_info = SteelProduceInfo.objects.get(id=steel_produce_info_id)
        # 封装客户钢网下单信息
        customer_steel_order_info = CustomerSteelOrderInfo(id=uuid1(),
                                                           # 客户选择的PCB ID
                                                           customer_pcb_order_id=customer_pcb_order_id,
                                                           # 客户选择的钢网产品
                                                           spec=steel_produce_info.spec,
                                                           area=steel_produce_info.area,
                                                           net_pay_price=steel_produce_info.net_pay_price,
                                                           express_coll_price=steel_produce_info.express_coll_price,
                                                           gross_weight=steel_produce_info.gross_weight,
                                                           # 钢网订单属性
                                                           steel_number=steel_number,
                                                           required_pack=required_pack,
                                                           required_receipt_and_delivery_note=required_receipt_and_delivery_note,
                                                           steel_use=steel_use,
                                                           required_mark=required_mark,
                                                           polishing_process=polishing_process,
                                                           required_engineering_process=required_engineering_process,
                                                           remark=remark)
        customer_steel_order_info.save()
        json_data['success'] = True
        json_data['id'] = customer_steel_order_info.id
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '保存异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


def get_by_id(request, id):
    json_data = {}
    try:
        print(id)
        # customer_steel_order_info = CustomerSteelOrderInfo.objects.get(id=id)
        # customer_steel_order_info_list = {
        #     'id': customer_steel_order_info.id
        # }
        json_data['success'] = True
        json_data['customerSteelOrderInfo'] = id
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')
