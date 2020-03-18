def greet_user():
    """ 打印简单的问候语 """
    print("Hello!")

def greet_user_with(username):
    """ 打印简单的问候语 """
    print("Hello " + username.title() + "!")

def any_param(*tops):
    for param in tops:
        print(param)

greet_user()
greet_user_with('alice')

any_param("nihao","huanghun")