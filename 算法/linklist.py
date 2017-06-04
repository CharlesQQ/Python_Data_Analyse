#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = "charles"

class Node(object):
    def __init__(self,item=None):
        self.item = item
        self.next = None

head = Node()
head.next = Node(20)
head.next.next = Node(30)


#链表遍历
def traversal(head):
    curNode = head   #临时用指针
    while curNode is not None:
        print(curNode.item)
        curNode = curNode.next

traversal(head)


#插入
p.next = curNode.next    #插入的复杂度为o(1)
curNode.next = p

#删除
p = curNode.next         #删除的复杂度为o(1)
curNode.next = curNode.next.next = p.next
del p

#建立链表
#头插法:每次插到head后面

def createLinkList(li):
    l = Node()    #head
    for num in li:
        s = Node(num)    #创建一个节点
        s.next = l.next     #新节点的的指针指向头节点的指针
        l.next = s          #再将头加点的指针指向节点自己
    return l

#尾插法
def createLinkListR(li):
    l = Node()
    r = l #r指向尾节点    一开始，头结点==尾节点
    for num in li:
        s = Node(num)
        r.next = s
        r = s           #更新尾节点

#链表:插入删除比列表快，查找比较慢(o(n))



#双链表
