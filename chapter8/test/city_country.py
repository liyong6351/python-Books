def city_country(city_name,country_name):
    return city_name+", " + country_name

def make_album(singerName,albumName="爱在西元前"):
    return  singerName + " in " + albumName

cityCountries= [city_country('chongqing', 'China'), city_country('beijing', 'China'), city_country('Santiago', 'Chile')]

for value in cityCountries:
    print(value)

albums= [make_album('zhoujielun', '爱在西元前'), make_album('xuwei', '曾经的你'), make_album('李健', '风吹麦芒'), make_album('以父之名')]

for value in albums:
    print(value)