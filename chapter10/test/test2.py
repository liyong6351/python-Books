filename = "guest.txt"
with open(filename,"a") as f:
    name = input("please in put your name,q for exit:")
    while name != 'q':
        f.write(name+"\n");
        name = input("please in put your name,q for exit:")

with open(filename, "r") as f:
    print(f.read())

