data = []
with open('resource/data.txt') as f:
    print(f.read())

with open('resource/data.txt') as f:
    for line in f:
        print(line.rstrip())

with open('resource/data.txt') as f:
    data = f.readlines();
print(data)

with open('resource/data.txt') as f:
    for line in f:
        print(line.replace("python","Python123").rstrip())
