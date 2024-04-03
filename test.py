# from Tools.scripts.finddiv import process
#
#
# def get_lines():
#     l = []
#     with open('123.txt', 'rb') as f:
#         for eachline in f:
#             l.append((eachline))
#     return l
# if __name__ == '__main__':
#     for e in get_lines():
#         process(e)


#
# def get_lines():
#     l = []
#     with open('123.txt', 'rb') as f:
#         data = f.readlines(60000)
#     l.append(data)
#     yield l
#
# a = get_lines()
# print(next(a))


# import datetime
# def dayofyear():
#     year = input('年：')
#     month = input('月：')
#     day = input('日：')
#     date1 = datetime.date(year=int(year), month=int(month), day=int(day))
#     date2 = datetime.date(year=int(year), month=1, day=1)
#     print((date1 - date2).days + 1)
#     return (date1 - date2).days + 1
# dayofyear()

# str1 = '12.3'
# print(int(str1))

# d = {"a":24, "g":52, "i":12, "k":33}
#
# new_d1 = sorted(d.values())
# new_d2 = sorted(d.items(),  key=lambda d: d[1], reverse=False)
# print(new_d2)
# print(d.values())
# print(d.items())


# a={'a':24,'g':52,'i':12,'k':33}
# b =[]
# for i in a.values():
#     b.append(i)
# b.sort()
# c ={}
# for i in b:
#     for j in a.keys():
#         if i ==a.get(j):
#             c[j]=i
# print(c)


# str = "aStr"
# a = str[::-1]
# print(a)

# str = "k:1|k1:2|k2:3|k3:4"
# def strDict(str):
#     dict1 = {}
#     for items in str.split('|'):
#         key,value = items.split(':')
#         dict1[key] = value
#     return dict1
# res = strDict(str)
# print(res)

# dict_result = {pair.split(":")[0]: int(pair.split(":")[1]) for pair in str.split("|")}
# print(dict_result)
#
# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])

# list = [a*11 for a in range(10)]
# print(list)


# a=[1,2,3,4]
# b=[1,5,6]
# c=[x for x in a if x in b]
# d=[y for y in (a+b) if y not in c]
# print(c)
# print(d)
# print(set(a)&set(b))
# print(set(a)^set(b))
# print(list(set(a)^set(b)))

# def extendlist(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendlist(10)
# list2 = extendlist(123, [])
# list3 = extendlist('a')
# print("list1 = %s" % list1)
# print("list2 = %s" % list2)
# print("list3 = %s" % list3)

# for i in range(1,100):
#     if i%6==0:
#         print(i)

# alist = []
# for i in range(1,100):
#     if i % 6 == 0:
#         alist.append(i)
#     last_num = alist[-3:]
#     print(last_num)


# str = '123'
# list = str.split()
# print(list)


# print(list(map(lambda x:x*x,[y for y in range(3)])))

# from functools import reduce
# reduce(lambda x,y:x*y,range(1,9))

# def multioliers():
#     return [lambda x:i*x for i in range(4)]
# print([lambda x:i*x for i in range(4)])
# print([m(2) for m in multioliers()])

# class A(object):
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance

# import time
# def timeit(func):
#     def wrapper():
#         start = time.perf_counter()
#         func()
#         end = time.perf_counter()
#         print('程序耗时：', end-start)
#     return wrapper
# @timeit
# def foo():
#     print('chenggong')
# foo()


a = 257
b = 257
print(a is b)