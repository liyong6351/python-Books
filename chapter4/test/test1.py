import time

def get_time_stamp(level=0):
    t = time.time()
    if level == 0:
        return int(t)
    elif level == 1:
        return int(round(t * 1000))  # 毫秒级时间戳
    elif level == 2:
        return int(round(t * 1000000)) # 微秒级时间戳

numbers=[value for value in range(1,21)]
print(numbers)

numbers=[value for value in range(1,1000001)]

level = 1
startTime = get_time_stamp(level)
print('min=' + str(min(numbers)))
print('max=' + str(max(numbers)))
print('sum=' + str(sum(numbers)))
endTime = get_time_stamp(level)

print(str(endTime - startTime) )

print("---------打印奇数---------")
print(list(range(1,21,2)))

print("---------打印被3整除的数---------")
numbers = list(range(3,31))
for value in numbers:
    if value%3==0:
        print(value)

print("---------打印立方---------")
numbers = list(range(1,11))
for value in numbers:
    print(str(value) + '立方=' + str(value**2*value))

print("---------解析立方---------")
numbers = [value**2*value for value in range(1,11)]
print(numbers)