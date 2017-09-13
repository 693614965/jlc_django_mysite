from django.template.response import TemplateResponse


# 网站首页
def index(request):
    context = {
        'name': '张三'
    }
    return TemplateResponse(request, 'index.html', context)


# 客户登录页面
def login(request):
    context = {
        'name': '张三'
    }
    return TemplateResponse(request, 'index.html', context)


# 客户平台页面
def client(request):
    context = {
        'name': '张三'
    }
    return TemplateResponse(request, 'index.html', context)
