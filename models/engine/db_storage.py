#!/usr/bin/python3
"""
This will include the storage connection abstraction.
Information that will be used to connect to db will be read from the "env.json"
file (should be located in / path).
You can see its structure in "env.backup" file.
Be aware that setting the WORKING_ENV key in the json file will cause dropping
all the tables in db.
"""
from models import *
from models.base_model import Base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy
import json

classes = {
    "City" : City,
    "Image" : Image,
    "Location": Location,
    "User": User,
    "Customer": Customer,
    "Vehicle": Vehicle,
    "Driver": Driver,
    "Delivery": Delivery,
    "Item": Item,
    "Rating": Rating
}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        URL = 'mysql+pymysql://{}:{}@{}/{}'.format(*self.get_vars())
        self.__engine = create_engine(URL)
        if self.env_type() == "test":
            print("This is a testing envirnment")
            print("All the date will be destoryed!")
            user_answer = input("Are you sure? [y/n]")
            if user_answer == "y":
                Base.metadata.drop_all(self.__engine)
            else:
                exit()

    def get_vars(self):
        "Get the config values to connect to database"
        with open("env.json", "r") as f:
            ENV_JSON = json.load(f)
            envs = [
                ENV_JSON["MYSQL_USER"],
                ENV_JSON["MYSQL_PWD"],
                ENV_JSON["MYSQL_HOST"],
                ENV_JSON["MYSQL_DB"],
                ENV_JSON.get("API_HOST", "0.0.0.0"),
                ENV_JSON.get("API_PORT", "5000")
            ]
            return envs

    def env_type(self):
        "Get the currnet working envirnement type (prod or dev or test)"
        import os

        with open("env.json", "r") as f:
            ENV_JSON = json.load(f)
            return ENV_JSON.get("WORKING_ENV", None)

    def all_key_id(self, cls=None):
        """Select all from database if cls is None, Or select all the entities
        in the class and return a dict representaion of it
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def all(self, model=None):
        """Get list of all model records"""
        model = self.get_model(model)
        Q = self.__session.query(model)
        records = self.dictify(Q.all())
        print(records)
        return records

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def save_all(self, obj_list:list):
        """commit all changes of the current database session"""
        for obj in obj_list:
            obj.save()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def get(self, cls, id):
        """retrieves an object"""
        # It's more efficient to use the database search tool
        classname = cls
        if type(cls) is str:
            cls = classes.get(cls.capitalize())
        if cls not in classes.values():
            raise TypeError("Unkonwn type {}".format(classname))
        obj = self.__session.query(cls).filter_by(id=id).first()
        return obj

    def count(self, cls=None):
        """counts the number of objects in storage"""
        classname = cls
        if type(cls) is str:
            cls = classes.get(cls.capitalize())
        if cls not in classes.values() or cls is None:
            raise TypeError("Unkonwn type {}".format(classname))
        if cls:
            return self.__session.query(cls).count()
        return sum([self.__session.query(c).count() for c in classes.values()])

    def random(self, cls=None):
        """counts the number of objects in storage"""
        classname = cls
        if type(cls) is str:
            cls = classes.get(cls.capitalize())
        if cls not in classes.values() or cls is None:
            raise TypeError("Unkonwn type {}".format(classname))
        if cls:
            return self.__session.query(cls).order_by(func.rand()).first()
        else:
            return None

    def starts_with(self, model=None, attr="", prefix=""):
        """Get all records that thier attr is starts with prefix
        Exemple:
            - model is city
            - attr is name
            - prefix is a
            will return all the cities with  name starting with prefix
        """
        model = self.get_model(model)
        Q = self.__session.query(model)
        if not hasattr(model, attr):
            e = "{} has no attribute {}".format(model.__name__, attr)
            raise AttributeError(e) 
        exp = getattr(model, attr).ilike("{}%".format(prefix))
        objs = Q.filter(exp).all()
        objs = self.dictify(objs)
        return objs

    # def contains(self, model=None, attr="", exp_str=""):
    #     model = self.get_model(model)
    #     QUERY = self.__session.query(model)
    #     if not hasattr(model, attr):
    #         e = "{} has no attribute {}".format(model.__name__, attr)
    #         raise AttributeError(e) 
    #     exp = getattr(City, "name").ilike("{}%".format(prefix))
    #     objs = QUERY.filter(exp).all()
    #     objs = self.dictify(objs)
    #     return objs

    def get_model(self, model=None):
        """Get model class by string or by model"""
        classname = model
        if type(model) is str:
            model = classes.get(model.capitalize())
        if model not in classes.values():
            raise TypeError("Unkonwn type {}".format(classname))
        return model

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False,
            autoflush=False
        )
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        The session instance will no longer be part of the Session's pending
        objects, and any changes made to the instance will not be persisted to
        the database when the Session is committed or flushed
        """
        self.__session.remove()

    def dictify(self, obj_list:list):
        return [obj.to_dict() for obj in obj_list]
