#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Charles Chang'
from sqlalchemy import create_engine,Table,func
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
Base = declarative_base()
engine=create_engine("mysql+mysqldb://jumpserver:jumpserver@localhost:3006/jumpserver")


class Host1(Base):

    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)


class User(Base):

    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    books = relationship('Book')


class Book(Base):

    __tablename__ = 'book'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20),ForeignKey('user.id'))


class Parent(Base):

    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String(64),unique=True,nullable=False)
    children = relationship("Child", back_populates="parent")


class Child(Base):

    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(64),unique=True,nullable=False)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("Parent", back_populates="children")
Base.metadata.create_all(engine)

Host2Group = Table('host_2_group',Base.metadata,
               Column('host_id',ForeignKey('hosts.id'),primary_key=True),
               Column('group_id',ForeignKey('group.id'),primary_key=True),
               )
engine = create_engine("mysql+mysqldb://liuyao:liuyao@121.42.195.15:3306/liuyao", max_overflow=5)
class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)
    groups = relationship('Group',
                      secondary= Host2Group,
                      backref = 'host_list')
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)

if __name__ == '__main__':
    SessionCls = sessionmaker(bind=engine)
    session = SessionCls()
    # h1 = Host(hostname='charles', ip_addr='1.1.1.1')
    # h2 = Host(hostname='redhat', ip_addr='2.2.2.2')
    # h3 = Host(hostname='centos', ip_addr='3.3.3.3')
    # session.add_all([h1,h2,h3])
    # session.rollback()
    # session.query(Host).filter(Host.id>2).delete()
    # session.query(Host).filter(Host.id == 2).update({'id': 4, 'hostname': "wahaha"})
    # ret = session.query(Host).filter_by(hostname='charles').all()
    # ret = session.query(Host).filter(Host.hostname.in_(['charles','wahaha'])).all()
    # ret = session.query(Host.hostname.label('')).all()
    # ret = session.query(Host).order_by(Host.id).all()
    # ret = session.query(Host).filter(Host.id == 4).one()
    # print ret,ret.hostname
    # for i in ret:
    #     print(i.id,i.hostname)
    # charles = User(id='1',name='charles')
    # eric = User(id='2',name='eric')
    # session.add_all([charles,eric])
    # session.commit()
    # python1 = Book(id=1,name='python1',user_id=1)
    # shell1 = Book(id=2,name='python2',user_id=2)
    # session.add_all([python1,shell1])
    # mama = Parent(id='1', name='mamaxx')
    # baba = Parent(id='2', name='babaoo')
    # session.add_all([mama,baba])
    g1 = Group(name='g1')
    g2 = Group(name='g2')
    g3 = Group(name='g3')
    g4 = Group(name='g4')
    session.add_all([g1,g2,g3,g4])
    session.commit()
