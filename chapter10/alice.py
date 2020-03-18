filename = "alice.txt"

try:
    with open(filename,"r") as f:
        print(f.readlines())
except FileNotFoundError:
    print("file not found!")
else:
    print("all are ok")

title = "Alice in Wonderland"
titleArr = title.split()
print(titleArr)