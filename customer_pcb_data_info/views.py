import os
from uuid import uuid1

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.utils.http import urlquote

from customer_delivery_address_info.models import CustomerDeliveryAddress
from .models import CustomerPcbDataInfo


# 客户资料 保存
def add(request):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            layer = request.POST.get('layer')
            width = request.POST.get('width')
            length = request.POST.get('length')
            pcb_num = request.POST.get('pcb_num')
            thickness = request.POST.get('thickness')
            solder_color = request.POST.get('solder_color')
            char_color = request.POST.get('char_color')
            pad_cover = request.POST.get('pad_cover')
            pad_spraying = request.POST.get('pad_spraying')
            minute_test = request.POST.get('minute_test')
            delivery_time = request.POST.get('delivery_time')
            required_invoice = request.POST.get('required_invoice')
            required_add_customer_num = request.POST.get('required_add_customer_num')
            required_book = request.POST.get('required_book')
            required_add_date_in_pcs = request.POST.get('required_add_date_in_pcs')
            required_wait_delivery_together = request.POST.get('required_wait_delivery_together')
            required_pack = request.POST.get('required_pack')
            required_receipt_and_delivery_note = request.POST.get('required_receipt_and_delivery_note')
            outside_barcode = request.POST.get('outside_barcode')
            required_smt = request.POST.get('required_smt')
            required_steel = request.POST.get('required_steel')
            remarks = request.POST.get('remarks')
            customer_pcb_data_info = CustomerPcbDataInfo(id=uuid1(), layer=layer, width=width, length=length,
                                                         pcb_num=pcb_num, thickness=thickness,
                                                         solder_color=solder_color,
                                                         char_color=char_color, pad_cover=pad_cover,
                                                         pad_spraying=pad_spraying,
                                                         minute_test=minute_test, delivery_time=delivery_time,
                                                         required_invoice=required_invoice,
                                                         required_add_customer_num=required_add_customer_num,
                                                         required_book=required_book,
                                                         required_add_date_in_pcs=required_add_date_in_pcs,
                                                         required_wait_delivery_together=required_wait_delivery_together,
                                                         required_pack=required_pack,
                                                         required_receipt_and_delivery_note=required_receipt_and_delivery_note,
                                                         outside_barcode=outside_barcode, required_smt=required_smt,
                                                         required_steel=required_steel, remarks=remarks,
                                                         customer_id=customer_id)
            customer_pcb_data_info.save()
            json_data['success'] = True
            json_data['id'] = customer_pcb_data_info.id
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '保存失败'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户资料 更新
def update(request):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            id = request.POST.get('id')
            if id:
                layer = request.POST.get('layer')
                width = request.POST.get('width')
                length = request.POST.get('length')
                pcb_num = request.POST.get('pcb_num')
                thickness = request.POST.get('thickness')
                solder_color = request.POST.get('solder_color')
                char_color = request.POST.get('char_color')
                pad_cover = request.POST.get('pad_cover')
                pad_spraying = request.POST.get('pad_spraying')
                minute_test = request.POST.get('minute_test')
                delivery_time = request.POST.get('delivery_time')
                required_invoice = request.POST.get('required_invoice')
                required_add_customer_num = request.POST.get('required_add_customer_num')
                required_book = request.POST.get('required_book')
                required_add_date_in_pcs = request.POST.get('required_add_date_in_pcs')
                required_wait_delivery_together = request.POST.get('required_wait_delivery_together')
                required_pack = request.POST.get('required_pack')
                required_receipt_and_delivery_note = request.POST.get('required_receipt_and_delivery_note')
                outside_barcode = request.POST.get('outside_barcode')
                required_smt = request.POST.get('required_smt')
                required_steel = request.POST.get('required_steel')
                remarks = request.POST.get('remarks')
                CustomerPcbDataInfo.objects.filter(id=id).update(layer=layer, width=width, length=length,
                                                                 pcb_num=pcb_num, thickness=thickness,
                                                                 solder_color=solder_color,
                                                                 char_color=char_color, pad_cover=pad_cover,
                                                                 pad_spraying=pad_spraying,
                                                                 minute_test=minute_test, delivery_time=delivery_time,
                                                                 required_invoice=required_invoice,
                                                                 required_add_customer_num=required_add_customer_num,
                                                                 required_book=required_book,
                                                                 required_add_date_in_pcs=required_add_date_in_pcs,
                                                                 required_wait_delivery_together=required_wait_delivery_together,
                                                                 required_pack=required_pack,
                                                                 required_receipt_and_delivery_note=required_receipt_and_delivery_note,
                                                                 outside_barcode=outside_barcode,
                                                                 required_smt=required_smt,
                                                                 required_steel=required_steel, remarks=remarks,
                                                                 customer_id=customer_id, status=0)
                json_data['success'] = True
                json_data['id'] = id
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '更新失败'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户资料 ID 查询
def get_by_id(request, id):
    print(id)
    json_data = {}
    try:
        customer_pcb_data_info = CustomerPcbDataInfo.objects.get(id=id)
        customer_pcb_data_info_list = {
            'id': customer_pcb_data_info.id,
            'layer': str(customer_pcb_data_info.layer),
            'width': customer_pcb_data_info.width,
            'length': customer_pcb_data_info.length,
            'pcb_num': customer_pcb_data_info.pcb_num,
            'thickness': str(customer_pcb_data_info.thickness),
            'solder_color': customer_pcb_data_info.solder_color,
            'char_color': customer_pcb_data_info.char_color,
            'pad_cover': customer_pcb_data_info.pad_cover,
            'pad_spraying': customer_pcb_data_info.pad_spraying,
            'minute_test': customer_pcb_data_info.minute_test,
            'delivery_time': customer_pcb_data_info.delivery_time,
            'required_invoice': customer_pcb_data_info.required_invoice,
            'required_add_customer_num': customer_pcb_data_info.required_add_customer_num,
            'required_book': customer_pcb_data_info.required_book,
            'required_add_date_in_pcs': customer_pcb_data_info.required_add_date_in_pcs,
            'required_wait_delivery_together': customer_pcb_data_info.required_wait_delivery_together,
            'required_pack': customer_pcb_data_info.required_pack,
            'required_receipt_and_delivery_note': customer_pcb_data_info.required_receipt_and_delivery_note,
            'outside_barcode': customer_pcb_data_info.outside_barcode,
            'required_smt': customer_pcb_data_info.required_smt,
            'required_steel': customer_pcb_data_info.required_steel,
            'remarks': customer_pcb_data_info.remarks,
            'status': customer_pcb_data_info.status
        }
        json_data['success'] = True
        json_data['customerPcbDataInfo'] = customer_pcb_data_info_list
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户资料 customer_id 查询
def list_by_customer_id(request):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        if customer_id:
            customer_pcb_data_info_s = CustomerPcbDataInfo.objects.filter(customer_id=customer_id)
            customer_pcb_data_info_list_s = []
            for customer_pcb_data_info in customer_pcb_data_info_s:
                customer_pcb_data_info_list_s.append({
                    'key': customer_pcb_data_info.id,
                    'layer': customer_pcb_data_info.layer,
                    'width': customer_pcb_data_info.width,
                    'length': customer_pcb_data_info.length,
                    'pcb_num': customer_pcb_data_info.pcb_num,
                    'thickness': customer_pcb_data_info.thickness,
                    'minute_test': customer_pcb_data_info.minute_test,
                    'delivery_time': customer_pcb_data_info.delivery_time,
                    'required_smt': customer_pcb_data_info.required_smt,
                    'required_steel': customer_pcb_data_info.required_steel,
                    'pcb_file_name': customer_pcb_data_info.pcb_file_name,
                    'remarks': customer_pcb_data_info.remarks,
                    'status': customer_pcb_data_info.status,
                })
            json_data['success'] = True
            json_data['data'] = customer_pcb_data_info_list_s
        else:
            json_data['success'] = False
            json_data['msg'] = '请登录'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 客户资料 删除
def delete(request, id):
    print(id)
    json_data = {}
    try:
        if id:
            CustomerPcbDataInfo.objects.filter(id=id).delete()
            json_data['success'] = True
            json_data['id'] = id
        else:
            json_data['success'] = False
            json_data['msg'] = 'ID 不存在'
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '删除异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 提交PCB 资料 审核
def check(request, id):
    print(id)
    json_data = {}
    try:
        if id:
            CustomerPcbDataInfo.objects.filter(id=id).update(status=1)
            json_data['success'] = True
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '操作异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')


# 分页查询客户资料
def list(request, page, page_size):
    print(page, page_size)
    customer_pcb_data_info_s = CustomerPcbDataInfo.objects.all()
    return HttpResponse(serialize('json', customer_pcb_data_info_s))


# 客户 上传PCB 文件
def pcb_upload(request):
    json_data = {}
    try:
        print(request.FILES)
        pcb_file = request.FILES.get('file', None)
        if pcb_file is not None:
            pcb_file_name = pcb_file.name  # 上传文件名称
            target_pcb_file_name = str(uuid1()) + "_" + pcb_file_name  # 保存在磁盘上 的目标文件名称
            target_pcb_file_path = os.path.join("D:\\PCB_UPLOAD", target_pcb_file_name)  # 目标文件路径
            target_pcb_file = open(target_pcb_file_path, 'wb+')  # 写 方式 打开目标文件
            for chunk in pcb_file.chunks():  # 块 方式 写入 目标文件
                target_pcb_file.write(chunk)
            target_pcb_file.close()  # 关闭 写
            id = request.GET.get("id")
            if id:
                CustomerPcbDataInfo.objects.filter(id=id).update(pcb_file_name=pcb_file_name,
                                                                 pcb_file_url=target_pcb_file_path, status=0)
                json_data['success'] = True
        else:
            print('pcb file is NONE')
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '上传异常'
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


# PCB 下载文件
def pcb_down(request, id):
    print(id)
    customer_pcb_data_info = CustomerPcbDataInfo.objects.filter(id=id).first()
    pcb_file_name = customer_pcb_data_info.pcb_file_name
    pcb_file_url = customer_pcb_data_info.pcb_file_url
    print(pcb_file_name, pcb_file_url)
    pcb_file_name.encode('utf-8').decode('utf-8')
    response = StreamingHttpResponse(file_iterator(pcb_file_url))
    response['Content_Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(urlquote(pcb_file_name))
    return response


def get__order_info(request, id):
    json_data = {}
    try:
        customer_id = request.session.get('customer_id')
        print(id, customer_id)
        if customer_id:
            customer_pcb_data_info = CustomerPcbDataInfo.objects.get(id=id)
            customer_delivery_address_info = CustomerDeliveryAddress.objects.get(customer_id=customer_id,
                                                                                 is_default=True)
            customer_pcb_data_info_list = {
                'id': customer_pcb_data_info.id,
                'layer': str(customer_pcb_data_info.layer),
                'width': customer_pcb_data_info.width,
                'length': customer_pcb_data_info.length,
                'pcb_num': customer_pcb_data_info.pcb_num,
                'thickness': str(customer_pcb_data_info.thickness),
                'solder_color': customer_pcb_data_info.solder_color,
                'char_color': customer_pcb_data_info.char_color,
                'pad_cover': customer_pcb_data_info.pad_cover,
                'pad_spraying': customer_pcb_data_info.pad_spraying,
                'minute_test': customer_pcb_data_info.minute_test,
                'delivery_time': customer_pcb_data_info.delivery_time,
                'required_invoice': customer_pcb_data_info.required_invoice,
                'required_add_customer_num': customer_pcb_data_info.required_add_customer_num,
                'required_book': customer_pcb_data_info.required_book,
                'required_add_date_in_pcs': customer_pcb_data_info.required_add_date_in_pcs,
                'required_wait_delivery_together': customer_pcb_data_info.required_wait_delivery_together,
                'required_pack': customer_pcb_data_info.required_pack,
                'required_receipt_and_delivery_note': customer_pcb_data_info.required_receipt_and_delivery_note,
                'outside_barcode': customer_pcb_data_info.outside_barcode,
                'required_smt': customer_pcb_data_info.required_smt,
                'required_steel': customer_pcb_data_info.required_steel,
                'remarks': customer_pcb_data_info.remarks,
                'status': customer_pcb_data_info.status
            }
            customer_delivery_address_info_list = {
                'id': customer_delivery_address_info.id,
                'link_man': customer_delivery_address_info.link_man,
                'link_man_mobile': customer_delivery_address_info.link_man_mobile,
                'pro': customer_delivery_address_info.province,
                'city': customer_delivery_address_info.city,
                'area': customer_delivery_address_info.area,
                'detail': customer_delivery_address_info.detail
            }
            customer_pcb_order_cost_info_list = [{
                'key': 'key',
                'engineering_cost': 100.00,
                'imposition_cost': 0.00,
                'spray_cost': 0.00,
                'board_cost': 100.00,
                'test_cost': 0.00,
                'film_cost': 0.00,
                'urgent_cost': 0.00,
                'color_cost': 0.00,
                'large_board_cost': 0.00,
                'tax_cost': 0.00,
                'express_cost': 20.00,
                'steel_cost':0.00,
                'steel_express_cost':0.00
            }]
            json_data['success'] = True
            json_data['customerPcbDataInfo'] = customer_pcb_data_info_list
            json_data['customerDeliveryAddressInfo'] = customer_delivery_address_info_list
            json_data['customerPcbOrderCostInfo'] = customer_pcb_order_cost_info_list
            json_data['total_amount'] = 220.00
    except BaseException as e:
        print(e)
        json_data['success'] = False
        json_data['msg'] = '查询异常'
    return HttpResponse(JsonResponse(json_data), 'application/json')
