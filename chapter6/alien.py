alien_0={'color':'green','point':5,'position':{'x_position':0,'y_position':50}}

print(alien_0['color'])
print(alien_0['point'])

print(alien_0.keys())

alien_0['a_position']=25
print(alien_0.keys())

# print( alien_0.pop('color'))
print(alien_0.keys())

sorted(alien_0.keys())
print(sorted(alien_0.items()))


for key,value in alien_0.items():
    if isinstance(value,dict):
        print('is dict')