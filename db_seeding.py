#!/bin/env python3
"""
Seed a dummy data to the database
"""
from models import *
from random import randrange, choice
from faker import Faker
import os
import requests
import json

f = Faker()
cities_endpoint = "https://madina.ysnirix.xyz/api/cities?format=json"
locations_endpoint = "https://madina.ysnirix.xyz/api/districts/{}?format=json"
avatar = "https://api.dicebear.com/8.x/icons/svg?icon={}"
class Seed():
    """Seed testing data for every model
    """
    def __init__(self, reset=False):
        self.reset = reset
        if reset:
            with open("env.json", "r") as f:
                info = json.load(f) 
            with open("env.json", "w") as f:
                info["WORKING_ENV"] = "test"
                json.dump(info, f, indent=4)

    def seed_cities_locations(self, many=30):
        """seed the cities and locations
            - many: many citeis to create
        """
        r = requests.get(cities_endpoint)
        cities = r.json().get("results")
        for city in cities[:many]:
            id = city.get("code")
            city_db = City(name=city.get("name"))
            r = requests.get(locations_endpoint.format(id))
            locations = r.json().get("results", [])
            for location in locations[:randrange(5, 15)]:
                location_db = Location(name=location.get("name"))
                city_db.locations.append(location_db)
                location_db.save()
                print(".", end="")
        print("\n")
        print("cites, OK")
        print("locations, OK")
    
    def seed_vehcle_image(self, many=50):
        """Get a random truck image, to assign it to a truck"""
        images = os.listdir(r"./static/images/trucks/")
        rand_img = choice(images)
        img = Image(img_path="./static/images/trucks/{}".format(rand_img))
        img.save()
        print(".", end="")
        return img

    def seed_user(self):
        """Seed a user"""
        avatars = [
            "boxes",
            "archive",
            "award",
            "bag",
            "bandaid",
            "box",
            "clocks"
        ]
        img_url = avatar.format(choice(avatars))
        email = f.free_email()
        password = f.password(special_chars=False)
        first_name = f.first_name()
        last_name = f.last_name()
        phone = "06" + f.msisdn()[:8]
        birthday = f.date()
        avatar_img = Image(img_url=img_url)
        user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            birthday=birthday
        )
        user.image = avatar_img
        avatar_img.save()
        user.save()
        print(".", end="")
        return user

    def seed_customers(self, many=69):
        """Seed desired 'many' customer"""
        print("Seeding Customers")
        for _ in range(many):
            customer = Customer(company=f.company())
            customer.user = self.seed_user()
            customer.save()
        print("\nCustomers, OK")

    def seed_vehicle(self, many=69):
        """Seed a one vehicle to db"""
        truck_models = [
            "Daimler",
            "Volvo",
            "Volkswagen",
            "PACCAR",
            "Iveco",
            "MAN",
            "Scania",
            "Mercedes-Benz",
            "Kenworth",
            "Fuso",
            "BharatBenz",
            "Mack",
            "Western",
        ]
        vehicle = Vehicle(
            model = choice(truck_models),
            year = f.year(),
            capacity = randrange(1500, 150000)
        )
        for _ in range(randrange(0, 15)):
            vehicle.images.append(self.seed_vehcle_image())
        vehicle.save()
        print(".", end="")
        return vehicle
    
    def seed_drivers(self, many=69):
        """Create 'many' drivers"""
        print("Seeding drivers")
        for _ in range(many):
            location = storage.random("location")
            driver = Driver(
                license_num = f.license_plate(),
                status = choice(['enroute', 'inactive', 'available'])
            )
            driver.user = self.seed_user()
            driver.location = location
            vehicle = self.seed_vehicle()
            driver.vehicle = vehicle
            driver.save()
            print(".", end="")
        print("\nDrivers, OK")

    def seed_item(self):
        """Seed one item"""
        item = Item(
            description=f.paragraph(),
            weight=randrange(20, 15000),
            size_x=randrange(1, 6),
            size_y=randrange(1, 6),
        )
        item.pickup = storage.random("Location")
        item.dropoff = storage.random("Location")
        item.owner = storage.random("Customer")
        for _ in range(randrange(0, 15)):
            item.images.append(self.seed_vehcle_image())
        item.save()
        print(".", end="")
        return item

    def seed_deliveries(self, many=69):
        print("Seeding deliveries")
        for _ in range(many):
            delivery = Delivery(
                pickup_time = f.time_object(),
                delivery_time = f.time_object(),
                status = choice(['pending', 'transiting', 'delivered'])
            )
            delivery.item = self.seed_item()
            driver = storage.random("Driver")
            driver.deliveries.append(delivery)
            delivery.save()
            driver.save()
        print("\nOK")

    def seed_ratings(self, many=69):
        print("Seeding ratings")
        for _ in range(many):
            rate = Rating(
                comment = f.text(),
                rating = randrange(0, 5)
            )
            driver = storage.random("Driver")
            rate.driver = driver
            customer = storage.random("Customer")
            rate.customer = customer
            rate.save()

        print("\nOK")

    def up(self, customers=2, drivers=3, deliveries=10, ratings=30):
        """Seed all the antities"""
        self.seed_cities_locations()
        self.seed_customers(customers)
        self.seed_drivers(drivers)
        self.seed_deliveries(deliveries)
        self.seed_ratings(ratings)


if __name__ == "__main__":
    s = Seed()
    s.seed_deliveries(50)
