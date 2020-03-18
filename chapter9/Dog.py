class Dog():
    def __init__(self,name="tom",age=2):
        self.__name=name
        self.__age = age

    def sit(self):
        print("Dog " + self.__name + " is sitting now!")

    def roll_over(self):
        print("Dog " + self.__name + " is roll over now!")

    def update_age(self,age):
        self.__age = age

    def __str__(self):
        return "Dog name=" + self.__name + " age=" + str(self.__age)