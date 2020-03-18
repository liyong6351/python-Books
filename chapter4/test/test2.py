cars = ['bmw','ford','audi','Lincoln','toyota','benz']

print("The first three items in the list are:" + str(cars[:3]))
middle = int(int(len(cars))/2)
print("The items from the middle are:" + str(cars[middle:]))
print("The last three items are:" + str(cars[-3:]))

friends_cars = cars[:]
cars.append('nissan')
friends_cars.append('subaru')
print('My cars are:' + str(cars))
print('My friends cars are:' + str(friends_cars))