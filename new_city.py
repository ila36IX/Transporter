#!/bin/python3


from models import *
from datetime import date
# from models.city import City
# from models.location import Location
# from models.imags import Location

c = City(name="agadir")
c.save()
l = Location(name="amzil", city_id=c.id)
l.save()
i = Image(img_url="https://files.com/marara5", img_path="/tmp/images/cat.png")
i.save()
user = User(email="king@thewarroot.tech", password="check-in", birthday=date.today())
user.save()
user.password ="tesitng"
user.save()
cc = Customer(user_id=user.id)
cc.save()
v = Vehicle(year=2100)
v.save()
print(v)
