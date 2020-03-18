foods=('tomcat','jetty','jboss','webspere','weblogic')
for food in foods:
    print(food)

try:
    foods[0]='java'
except TypeError:
    print('Cannot modify tuple')
else:
    print('can modify tuple')

foods1=('tomcat','jetty','jboss','webspere1','weblogic1')
for food in foods1:
    print(food)