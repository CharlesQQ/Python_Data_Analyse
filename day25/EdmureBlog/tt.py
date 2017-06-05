__author__ = 'Administrator'

dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# print(dic.keys())
# for k,v in dic.items():
#     if k == 'k2':
#         del dic[k]     #在迭代过程中，不能删除被迭代的序列的元素

for k in list(dic.keys()):   #在python3中,.keys()是一个迭代器
    if k == 'k2':
        del dic[k]
print(dic)