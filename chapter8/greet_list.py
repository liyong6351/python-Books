def greet_users(users):
    users[0] = 'tomcat'
    for value in users:
        print("Hello " + value)

users = ['tom','hack','lucy','lily']
print(users)
#greet_users(users)
# 禁止函数修改数据
greet_users(users[:])
print(users)