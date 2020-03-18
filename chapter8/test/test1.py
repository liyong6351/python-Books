def show_magicians(usernames):
    for user in usernames:
        print("Hello " + user)

def show_greate(usernames):
    for user in usernames:
        usernames[users.index(user)] = "Greate " + user
        print("Greate " + user)

users = ["tom","jimi","lucy","lily","lantern"]

show_magicians(users)
show_greate(users)
print(users)
users = ["tom","jimi","lucy","lily","lantern"]
show_greate(users[:])
print(users)