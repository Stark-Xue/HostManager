# Author: 73
from sqlalchemy.orm import sessionmaker
from host import sqlal

Session_class = sessionmaker(bind=sqlal.engine) #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class() #生成session实例

host_obj1 = sqlal.Host(ip="10.0.0.2", hostname="qwer", status=1, flags=1, description="seth's computer") #生成你要创建的数据对象
host_obj2 = sqlal.Host(ip="10.0.0.3", hostname="asdf", status=2, flags=0, description="bob's computer")
host_obj3 = sqlal.Host(ip="10.0.0.4", hostname="zxcv", status=3, flags=1, description="peter's computer")
host_obj4 = sqlal.Host(ip="10.0.0.5", hostname="uiop", status=2, flags=0, description="rain's computer")
host_obj5 = sqlal.Host(ip="10.0.0.6", hostname="hjkl", status=3, flags=1, description="seven's computer")
host_obj6 = sqlal.Host(ip="10.0.0.7", hostname="vbnm", status=1, flags=0, description="one's computer")
host_obj7 = sqlal.Host(ip="10.0.0.8", hostname="abcd", status=2, flags=0, description="hello's computer")
print(host_obj1.hostname, host_obj1.id) #此时还没创建对象呢，不信你打印一下id发现还是None

Session.add_all([host_obj1,host_obj2,host_obj3,host_obj4,host_obj5,host_obj6,host_obj7]) #把要创建的数据对象添加到这个session里， 一会统一创建
Session.commit() #现此才统一提交，创建数据