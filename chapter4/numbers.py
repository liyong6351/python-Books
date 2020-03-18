# 使用range生成一个数据列表
for value in range(0,5):
    print(value)

# 使用range和list生成数组
# 使用**表示平方
numbers = list(range(0,10,2))
for value in numbers:
    print(str(value) + ",pow(" + str(value) + ")=" + str(value**2))