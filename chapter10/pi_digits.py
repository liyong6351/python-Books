data = ''
birthday='41592'
with open('resource/py_digits.txt') as f:
    for line in f:
        data+=(line.strip())

print(data)

if birthday in data:
    print("in it")
else:
    print("not in it")