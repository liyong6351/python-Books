class Car():
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year

    def fill_gas_tank(self):
        print("Need to fill gas and oil")

    def __str__(self):
        return "Car make=" + str(self.__make) + " model=" + str(self.__model) + " year=" + str(self.__year)


class EleCar(Car):
    def __init__(self, make, model, year, ext):
        super().__init__(make, model, year)
        self.__ext = ext

    def fill_gas_tank(self):
        print("No Need to fill gas and oil")

    def __str__(self):
        return super().__str__() + " ext=" + str(self.__ext)

my_tesla = EleCar('tesla','model3',2016,'haoyang')
my_tesla.fill_gas_tank()
print(str(my_tesla))