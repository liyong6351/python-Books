cars = ['bmw','audi','subaru','toyota']

for car in cars:
    if car == 'audi':
        print(car.upper())
    elif car != 'bmw':
        print(car.lower())
    else:
        print(car.title())

if 'bmw' in cars:
    print('bmw is in the list')

if 'ford' not in cars:
    print('ford is not in the list')