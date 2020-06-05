# Author: 73

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine("mysql+pymysql://seth:123456@localhost/test", encoding="utf-8", echo=True) # echo是否打印运行过程

Base = declarative_base() # 生成orm基类

class Host(Base):
    __tablename__ = 'host' # 表名
    id = Column(Integer, primary_key=True)
    ip = Column(String(32))
    hostname = Column(String(32))
    status = Column(Integer)
    flags = Column(Integer)
    description = Column(String(32))

class User(Base):
    __tablename__ = 'user' # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(32))

Base.metadata.create_all(engine) # 创建表结构