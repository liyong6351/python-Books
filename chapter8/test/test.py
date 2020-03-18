def make_shirt(size,msg="I love python"):
    print('size='+str(size) + " msg=" + str(msg))

def describe_city(cityName,countryName="china"):
    print(cityName + " is in the " + countryName)

make_shirt(14)
describe_city("重庆")
describe_city("北京","中国")
describe_city("伦敦","英国")