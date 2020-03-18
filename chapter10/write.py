filename="programming.txt"
with open(filename,"r") as f:
    print(f.read())

with open(filename,"a") as f:
    f.write("I love python!")

with open(filename, "r") as f:
    print(f.read())