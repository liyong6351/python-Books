names=['mr.huang','mr.zhang']
print(names)
names.reverse()
print(names)

for name in names:
    print("Welcome here " + name.title())

names.append('Ms.Chen')
print(names)
names.insert(0,'Mr.wu')
print(names)

del names[0]
print(names)

names.pop(0)
print(names)

print("-------排序相关---------")
cars = ['bmw','audi','toyota','subaru']
# 临时排序
print(sorted(cars))
print(cars)
# 永久排序
cars.sort()
print(cars)