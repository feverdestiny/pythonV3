# dic 字典
a = {'aaa': '1111', 'bbb': '2222', 'ccc': '3333'}
b = {'111': 'admin'}
a['dddd'] = 4444  # 新增字典数据
# del a['aaa']  # 删除字典键
# a.clear()  # 清空字典

# str(a)
# b = ('a', 'b', 'c')
# c = 10
# d = a.fromkeys(b, c)
# print(type(a))

# b = a.get('aaa')  # 获取键的值
# print(b)
# c = 'aaa' in a  # 某个键是否存在字典中
# print(c)

# print(a.keys())  # 返回字典key值列表
# print(a.values())  # 返回指点value值列表

# print(a.items())  # 返回可遍历的元组数组
# b.update(a)  # 把a字典添加到b字典中去
# print(b)
# a.pop('aaa')  # 删除字典中可以值
# print(a)
# a.popitem()  # 随机删除字典中一个键值对数据 默认删除最后一个
# print(a)
