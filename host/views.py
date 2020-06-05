from django.shortcuts import render, HttpResponse

from sqlalchemy.orm import sessionmaker
from host import sqlal

Session_class = sessionmaker(bind=sqlal.engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# Create your views here.

def select_user():
    data = Session.query(sqlal.User).filter().all()
    return data

def select_host():
    data = Session.query(sqlal.Host).filter().all()
    return data

def insert_host(ip,hostname,status,flags,description):
    host_obj = sqlal.Host(ip=ip, hostname=hostname, status=status, flags=flags, description=description)
    Session.add(host_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
    Session.commit()  # 现此才统一提交，创建数据

def delete_host(id):
    Session.query(sqlal.Host).filter_by(id=id).delete()
    Session.commit()  # 现此才统一提交，创建数据

def login(request):
    if request.method == "POST":
        flag = 0
        usr = request.POST.get("usr", None)
        pwd = request.POST.get("pwd", None)
        users = select_user()
        hosts = select_host()
        for user in users:
            if usr == user.name:
                flag = 1
                if pwd == user.password:
                    return render(request, "home.html", {'hosts':hosts})
                else:
                    return HttpResponse("密码错误")
        if flag == 0:
            return HttpResponse("用户不存在")
    elif request.method == "GET":
        return render(request, "login.html")

def detail(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        nid = request.GET.get("nid")
        data = Session.query(sqlal.Host).filter(sqlal.Host.id == nid).all()
        return render(request, "detail.html", {'data': data})

def home(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        hostname = request.POST.get("hostname")
        status = int(request.POST.get("status"))
        flags = int(request.POST.get("flags"))
        description = request.POST.get("description")
        insert_host(ip,hostname,status,flags,description)
        hosts = select_host()
        return render(request,"home.html",{'hosts':hosts})
    elif request.method == "GET":
        pass

def delete(request):
    if request.method == "POST":
        nid = request.POST.get("nid", None)
        delete_host(nid)
        hosts = select_host()
        return render(request, "home.html", {'hosts': hosts})
    elif request.method == "GET":
        pass