#!/bin/env python3
from models import *
from random import randrange, choice
import requests
import os
from faker import Faker

f = Faker()
cities_endpoint = "https://madina.ysnirix.xyz/api/cities?format=json"
locations_endpoint = "https://madina.ysnirix.xyz/api/districts/{}?format=json"
avatar = "https://api.dicebear.com/8.x/icons/svg?icon={}"
class Seed():
    def seed_cities_locations(self, many=30):
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
        images = os.listdir(r"./static/images/trucks/")
        rand_img = choice(images)
        img = Image(img_path="./static/images/trucks/{}".format(rand_img))
        img.save()
        print(".", end="")
        return img

    def seed_user(self):
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
        print("Seeding Customers")
        for _ in range(many):
            customer = Customer(company=f.company())
            customer.user = self.seed_user()
            customer.save()
        print("\nCustomers, OK")

    def seed_vehicle(self, many=69):
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
        item = Item(
            description=f.paragraph(),
            weight=randrange(20, 15000),
            size_x=randrange(1, 6),
            size_y=randrange(1, 6),
        )
        item.pickup = storage.random("Location")
        item.dropoff = storage.random("Location")
        item.owner = storage.random("Customer")
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

    def up(self):
        """Seed all the antities"""
        s.seed_cities_locations()
        s.seed_customers(700)
        s.seed_drivers(70)
        s.seed_deliveries(9000)


s = Seed()
if __name__ == "__main__":
    s.seed_cities_locations()
    s.seed_customers(700)
    s.seed_drivers(70)
    s.seed_deliveries(9000)
