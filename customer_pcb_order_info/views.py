from uuid import uuid1

from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.utils.http import urlquote

from customer_delivery_address_info.models import CustomerDeliveryAddress
from customer_pcb_data_info.models import CustomerPcbDataInfo
from .models import CustomerPcbOrderInfo, CustomerPcbOrderCost


# 新增 PCB 订单
def add(request):
    json_data = {}
    try:
        # PCB 资料信息 ID
        pcb_info_id = request.POST.get('pcb_info_id')
        # 客户收货地址ID
        delivery_id = request.POST.get('delivery_id')
        # 订单总额
        total_amount = float(request.POST.get('total_amount'))
        # 快递公司
        express_type = request.POST.get('express_type')
        # 支付方式
        pay_type = request.POST.get('pay_type')
        # 订单费用信息
        engineering_cost = request.POST.get('engineering_cost')  # 工程费
        imposition_cost = request.POST.get('imposition_cost')  # 拼版费
        spray_cost = request.POST.get('spray_cost')  # 喷镀费
        board_cost = request.POST.get('board_cost')  # 板费
        test_cost = request.POST.get('test_cost')  # 测试费
        film_cost = request.POST.get('film_cost')  # 菲林费
        urgent_cost = request.POST.get('urgent_cost')  # 加急费
        color_cost = request.POST.get('color_cost')  # 颜色费
        large_board_cost = request.POST.get('large_board_cost')  # 大板费
        tax_cost = request.POST.get('tax_cost')  # 税费
        express_cost = request.POST.get('express_cost')  # 快递费
        steel_cost = request.POST.get('steel_cost')  # 钢网费
        steel_express_cost = request.POST.get('steel_express_cost')  # 钢网运费

        # ID 查询 客户资料信息实例
        pcb_info = CustomerPcbDataInfo.objects.get(id=pcb_info_id)
        # ID 查询 客户收货地址信息实例
        delivery_info = CustomerDeliveryAddress.objects.get(id=delivery_id)
        # 生成一条订单信息 实例
        customer_order_info = CustomerPcbOrderInfo(id=uuid1(),
                                                   # PCB 资料
                                                   layer=pcb_info.layer,
                                                   width=pcb_info.layer,
                                                   length=pcb_info.length,
                                                   board_area=pcb_info.board_area,
                                                   pcb_num=pcb_info.pcb_num,
                                                   thickness=pcb_info.thickness,
                                                   solder_color=pcb_info.solder_color,
                                                   char_color=pcb_info.char_color,
                                                   pad_cover=pcb_info.pad_cover,
                                                   pad_spraying=pcb_info.pad_spraying,
                                                   minute_test=pcb_info.minute_test,
                                                   delivery_time=pcb_info.delivery_time,
                                                   required_invoice=pcb_info.required_invoice,
                                                   required_add_customer_num=pcb_info.required_add_customer_num,
                                                   required_book=pcb_info.required_book,
                                                   required_add_date_in_pcs=pcb_info.required_add_date_in_pcs,
                                                   required_wait_delivery_together=pcb_info.required_wait_delivery_together,
                                                   required_pack=pcb_info.required_pack,
                                                   required_receipt_and_delivery_note=pcb_info.required_receipt_and_delivery_note,
                                                   outside_barcode=pcb_info.outside_barcode,
                                                   required_smt=pcb_info.required_smt,
                                                   required_steel=pcb_info.required_steel,
                                                   remarks=pcb_info.remarks,
                                                   pcb_file_name=pcb_info.pcb_file_name,
                                                   pcb_file_url=pcb_info.pcb_file_url,
                                                   customer_id=pcb_info.customer_id,
                                                   # 客户收货地址信息
                                                   link_man=delivery_info.link_man,
                                                   link_man_mobile=delivery_info.link_man_mobile,
                                                   province=delivery_info.province,
                                                   city=delivery_info.city,
                                                   area=delivery_info.area,
                                                   detail=delivery_info.detail,
                                                   # 订单 信息
                                                   number_order=get_order_number(),
                                                   total_amount=total_amount,
                                                   pay_type=pay_type,
                                                   express_type=express_type,
                                                   order_type=get_order_type(pcb_info.pcb_num))
        # 生成订单 对应的费用 实例
        customer_order_cost_info = CustomerPcbOrderCost(id=uuid1(),
                                                        pcb_order_id=customer_order_info.id,
                                                        pcb_number_order=customer_order_info.number_order,
                                                        engineering_cost=engineering_cost,
                                                        imposition_cost=imposition_cost,
                                                        spray_cost=spray_cost,
                                                        board_cost=board_cost,
                                                        test_cost=test_cost,
                                                        film_cost=film_cost,
                                                        urgent_cost=urgent_cost,
                                                        color_cost=color_cost,
                                                        large_board_cost=large_board_cost,
                                                        tax_cost=tax_cost,
                                                        express_cost=express_cost,
                                                        steel_cost=steel_cost,
                                                        steel_express_cost=steel_express_cost)
        customer_order_info.save()
        customer_order_cost_info.save()
        json_data['success'] = True
        json_data['id'] = customer_order_info.id
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '保存订单异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# ID 查询
def get(request, id):
    json_data = {}
    try:
        print(id)
        # PCB 订单
        customer_pcb_order_info = CustomerPcbOrderInfo.objects.get(id=id)
        # PCB 订单费用明细
        customer_pcb_order_cost = CustomerPcbOrderCost.objects.get(pcb_order_id=customer_pcb_order_info.id)
        # PCB 订单 json 格式 数据 封装
        customer_pcb_order_info_list = {
            # PCB 板子信息
            'id': customer_pcb_order_info.id,
            'layer': str(customer_pcb_order_info.layer),
            'width': customer_pcb_order_info.width,
            'length': customer_pcb_order_info.length,
            'pcb_num': customer_pcb_order_info.pcb_num,
            'thickness': str(customer_pcb_order_info.thickness),
            'solder_color': customer_pcb_order_info.solder_color,
            'char_color': customer_pcb_order_info.char_color,
            'pad_cover': customer_pcb_order_info.pad_cover,
            'pad_spraying': customer_pcb_order_info.pad_spraying,
            'minute_test': customer_pcb_order_info.minute_test,
            'delivery_time': customer_pcb_order_info.delivery_time,
            'required_invoice': customer_pcb_order_info.required_invoice,
            'required_add_customer_num': customer_pcb_order_info.required_add_customer_num,
            'required_book': customer_pcb_order_info.required_book,
            'required_add_date_in_pcs': customer_pcb_order_info.required_add_date_in_pcs,
            'required_wait_delivery_together': customer_pcb_order_info.required_wait_delivery_together,
            'required_pack': customer_pcb_order_info.required_pack,
            'required_receipt_and_delivery_note': customer_pcb_order_info.required_receipt_and_delivery_note,
            'outside_barcode': customer_pcb_order_info.outside_barcode,
            'required_smt': customer_pcb_order_info.required_smt,
            'required_steel': customer_pcb_order_info.required_steel,
            'remarks': customer_pcb_order_info.remarks,
            # 联系人及收货地址信息
            'link_man': customer_pcb_order_info.link_man,
            'link_man_mobile': customer_pcb_order_info.link_man_mobile,
            'pro': customer_pcb_order_info.province,
            'city': customer_pcb_order_info.city,
            'area': customer_pcb_order_info.area,
            'detail': customer_pcb_order_info.detail,
            # 订单信息
            'number_order': customer_pcb_order_info.number_order,
            'total_amount': customer_pcb_order_info.total_amount,
            'order_status': customer_pcb_order_info.order_status,
            'pay_type': customer_pcb_order_info.pay_type,
            'express_type': customer_pcb_order_info.express_type,
            'order_type': customer_pcb_order_info.order_type,
            'date_order': customer_pcb_order_info.date_order.strftime('%Y-%m-%d %H:%M:%S')
        }
        # PCB 费用明细 json 格式封装
        customer_pcb_order_cost_list = [{
            'engineering_cost': customer_pcb_order_cost.engineering_cost,
            'imposition_cost': customer_pcb_order_cost.imposition_cost,
            'spray_cost': customer_pcb_order_cost.spray_cost,
            'board_cost': customer_pcb_order_cost.board_cost,
            'test_cost': customer_pcb_order_cost.test_cost,
            'film_cost': customer_pcb_order_cost.film_cost,
            'urgent_cost': customer_pcb_order_cost.urgent_cost,
            'color_cost': customer_pcb_order_cost.color_cost,
            'large_board_cost': customer_pcb_order_cost.large_board_cost,
            'tax_cost': customer_pcb_order_cost.tax_cost,
            'express_cost': customer_pcb_order_cost.express_cost,
            'steel_cost': customer_pcb_order_cost.steel_cost,
            'steel_express_cost': customer_pcb_order_cost.steel_express_cost,
            'pcb_number_order': customer_pcb_order_cost.pcb_number_order,
            'pcb_order_id': customer_pcb_order_cost.pcb_order_id,
        }]
        json_data['success'] = True
        json_data['customerPcbOrderInfo'] = customer_pcb_order_info_list
        json_data['customerPcbOrderCostInfo'] = customer_pcb_order_cost_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户查询自己的订单
def get_by_customer_id(request, page, page_size):
    print(page, page_size)
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            print(customer_id)
            customer_pcb_order_info = CustomerPcbOrderInfo.objects.filter(customer_id=customer_id).order_by(
                '-date_order')  # 客户ID 查询 客户订单
            customer_pcb_order_info_list = []
            for order in customer_pcb_order_info:
                customer_pcb_order_info_list.append({
                    'key': order.id,
                    'pcb_file_name': order.pcb_file_name,
                    'pcb_file_url': order.pcb_file_url,
                    'number_order': order.number_order,
                    'total_amount': order.total_amount,
                    'order_status': order.order_status,
                    'express_type': order.express_type,
                    'order_type': order.order_type,
                    'pay_type': order.pay_type,
                    'date_order': order.date_order.strftime('%Y-%m-%d %H:%M:%S')
                })
            json_data['success'] = True
            json_data['data'] = customer_pcb_order_info_list
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 迭代 下载文件
def file_iterator(file_name, chunk_size=512):
    with open(file_name, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def pcb_down(request, id):
    print(id)
    customer_pcb_order_info = CustomerPcbOrderInfo.objects.filter(id=id).first()
    pcb_file_name = customer_pcb_order_info.pcb_file_name
    pcb_file_url = customer_pcb_order_info.pcb_file_url
    print(pcb_file_name, pcb_file_url)
    pcb_file_name.encode('utf-8').decode('utf-8')
    response = StreamingHttpResponse(file_iterator(pcb_file_url))
    response['Content_Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(urlquote(pcb_file_name))
    return response


# 订单号 生成
def get_order_number():
    import datetime
    import random
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    print(now_time)
    random_num = random.randint(0, 100)  # 生成随机整数
    if random_num <= 10:
        random_num = str(0) + str(random_num)
    unique_num = str(now_time) + str(random_num)
    print(unique_num)
    return unique_num


# 订单分类 判断
def get_order_type(pcb_num):
    if pcb_num > 30:
        return 'batch'
    else:
        return 'simple'
