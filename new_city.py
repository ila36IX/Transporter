#!/bin/python3
from models import *
from datetime import date, time
# cities [loc1, loc2]
# locations
# images
# users
# customers
# vehicles
# drivers
# items
# items_images
# deliveries
# ratings
city = City(name="city1")
location1 = Location(name="location1")
location2 = Location(name="location2")
location3 = Location(name="location3")
city.locations.extend([location1, location2, location3])
city.save()
location1.save()
location2.save()
location3.save()
image = Image(img_path="/tmp/images/cat.png")
image.save()
user1 = User(email="testing@google.com", password="notaveasypassowrd")
user1.image = image
user1.save()
customer = Customer(company="car")
customer.user = user1
customer.save()
vehicle = Vehicle(model="Volvo", year=2005, capacity=520)
image1 = Image(img_path="/tmp/images/truck1.png")
image2 = Image(img_path="/tmp/images/truck2.png")
image3 = Image(img_path="/tmp/images/truck3.png")
image1.save()
image2.save()
image3.save()
vehicle.images.extend([image1, image2, image3])
vehicle.save()
driver = Driver(license_num="ST4539")
user2 = User(email="trucker@google.com", password="ilovetrucks")
image4 = Image(img_path="/tmp/images/truck3.png")
image4.save()
user2.image = image4
user2.save()
driver.location = location1
driver.vehicle = vehicle
driver.user = user1
driver.save()
item = Item(description="I need this to be deliverd ASAP!", size_x=15, size_y=11, weight=125)
item.owner = customer
item.pickup = location2
item.dropoff = location3
image1 = Image(img_path="/tmp/images/truck1.png")
image2 = Image(img_path="/tmp/images/truck2.png")
image3 = Image(img_path="/tmp/images/truck3.png")
image1.save()
image2.save()
image3.save()
item.images.extend([image1, image2, image3])
item.save()
delivery = Delivery(pickup_time=time(15, 14), delivery_time=time(19, 00))
delivery.item = item
delivery.driver = driver
print("OK")
