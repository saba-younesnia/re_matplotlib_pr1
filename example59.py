import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="IthinkIgotit**01",
    database="dbtest"
)
mycursor=db.cursor()

query1="select name, (jan+feb+mar+apr+may+jun+jul+aug+sep+oct+nov+dece)/12 from cities inner join amount_of_rain on cities.city_id=amount_of_rain.city_id"
mycursor.execute(query1)
infos=mycursor.fetchall()

citynames=[]
rainamount=[]
for mytuple in infos:
    citynames.append(mytuple[0])
    rainamount.append(float(mytuple[1]))

citynames_ar=np.array(citynames)
rainamount_ar=np.array(rainamount)

myfont={'family':"tahoma",'color':"blue","size":30}
plt.title("Cities and Rain",fontdict=myfont)
plt.bar(citynames_ar,rainamount_ar,color="green")
plt.show()

query2="select name , population from cities"
mycursor.execute(query2)
infos=mycursor.fetchall()
citynames=[]
population=[]
for mytuple in infos:
    citynames.append(mytuple[0])
    population.append(int(mytuple[1]))
population_ar=np.array(population)
plt.pie(population_ar,labels=citynames)
plt.show()