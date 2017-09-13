from uuid import uuid1

from django.core.serializers import serialize
from django.http import HttpResponse

from .models import DictModel, DictDetailModel


# 字典 新增
def add(request):
    dict = DictModel()
    dict.id = uuid1()
    dict.name = '分类'
    dict.code = 'type'
    dict.serial = 100
    DictModel.save(dict)
    return HttpResponse({'success': True})


# 字典 ID 查询
def get_by_id(request, id):
    print(id)
    dict = DictModel.objects.filter(id=id)
    return HttpResponse(serialize('json', dict))


# 字典 查询
def list(request, page, page_size):
    print(page, page_size)
    dicts = DictModel.objects.all()
    return HttpResponse(serialize('json', dicts))


# 字典 更新
def update(request, id):
    print(id)
    name = request.POST.get('name')
    DictModel.objects.filter(id=id).update(name=name)
    return HttpResponse({'success': True})


# 字典 删除
def delete(request, id):
    print(id)
    DictModel.objects.filter(id=id).delete()
    return HttpResponse({'success': True})


# 字典明细 新增
def detail_add(request):
    dict_detail = DictDetailModel()
    dict_detail.id = uuid1()
    dict_detail.name = '分类'
    dict_detail.code = 'type'
    dict_detail.serial = 100
    dict_detail.dictId = '2c258d46-8230-11e7-97cd-d151c6632e8e'
    DictDetailModel.save(dict_detail)
    return HttpResponse({'success': True})


# 字典明细 ID 查询
def detail_get_by_id(request, id):
    print(id)
    dict_detail = DictDetailModel.objects.filter(id=id)
    return HttpResponse(serialize('json', dict_detail))


# 字典明细 查询
def detail_list(request, page, page_size):
    print(page, page_size)
    dict_details = DictDetailModel.objects.all()
    return HttpResponse(serialize('json', dict_details))


# 字典明细 更新
def detail_update(request, id):
    print(id)
    name = request.POST.get('name')
    DictDetailModel.objects.filter(id=id).update(name=name)
    return HttpResponse({'success': True})


# 字典明细 删除
def detail_delete(request, id):
    print(id)
    DictDetailModel.objects.filter(id=id).delete()
    return HttpResponse({'success': True})
