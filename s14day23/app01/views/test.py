from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models

def index(request):
    # models.UserType.objects.all().values('name', 'user__pwd')
    # users = models.User.objects.all()
    # for row in users:
    #     print(row.user,row.pwd,row.ut_id)   #第一次sql请求
    #     print(row.ut.name)    #再次发起一次sql请求,
    #     #如果涉及到跨表，就会再次发起sql请求，如果想要仅仅发起一次sql请求，可以使用values('user','pwd','ut__name')
    #
    #
    # #select_related
    #     users = models.User.objects.all().select_related('ut')   #会将所有跨表关联的数据进行一次查询出来.可以加多个参数，注意参数只能是关联的字段，表示也会查询与ut关联的表的数据;
    #     #连表查询查询数据是快的，浪费存储资源，但是查询速度快了;数据库范式:foreignkey，onetoone，m2m
    #
    # #prefetch_related
    # users = models.User.objects.filter(id__gt=30).prefetch_related('ut')
    # #select * from users where id>30    --->第一次
    # #获取上一步骤中所有的ut_id=[1,2....]
    # #select * from user_type where id in [1,2]    -->第二次
    # for row in users:
    #     print(row.user,row.pwd,row.ut_id)
    #     print(row.ut.name)

    # models.UserInfo.objects.create(name='root',email='root')
    # obj = models.UserInfo(name='charles',email='1111')
    # obj.full_clean()   #这里会做验证(对所有的字段)，如果失败，直接报错
    # obj.save()

    from app01.forms import UserInfoForm
    if request.method == 'GET':
        obj = UserInfoForm({'user':"charles"})    #每次刷新的时候，会执行这个操作，将全部的数据封装在obj中
        return render(request,'index.html',{'obj':obj})
    elif request.method == 'POST':
        obj = UserInfoForm(request.POST,request.FILES)
        obj.is_valid()
    # return HttpResponse('index')

def register(request):
    # from app01.forms import RegisterForm
    # obj = RegisterForm(request.POST)
    # if obj.is_valid():
    #     obj.cleaned_data
    # else:
    #     obj.errors
    #     {
    #         '__all__':[],  #整体错误信息
    #         'user':[{'code':'required','message':'xxx'}],
    #         'pwd':[{'code':'required','message':'xxxx'}],
    #     }
    # from django.core import serializers
    # v = models.UserType.objects.all()
    # data = serializers.serialize("json",v)    #序列化成json的对象
    # return HttpResponse(data)
    import json
    v = models.UserType.objects.values('id','name')
    v = list(v)
    return HttpResponse(json.dumps(v))