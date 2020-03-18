msg = input('Please input the msg:')
print(msg)

condition = True
msg = 'Please input your age:'
age = input(msg)
while condition:
    age = input(msg)
    try:
        age = int(age)
    except ValueError:
        msg = 'Your input is not a number,please input again:'
    else:
        condition = False

if age>=18:
    print('You are older than 18')