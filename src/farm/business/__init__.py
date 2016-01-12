#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append("..")
from farm.database.models import Seed
from farm.database import db_adapter


DISABLE_COUNT = -1


class FarmManager():
    def __init__(self, db):
        self.db = db

    def add_or_update(self, name, body):
        seed = self.db.find_first_object_by(Seed, name=name)
        if seed is None:
            seed = Seed(name=name, number=body["number"])
            self.db.add_object(seed)
            return seed
        else:
            self.db.update_object(seed, number=body["number"])
            if "name" in body:
                self.db.update_object(seed, name=body["name"])
            return seed

    def get_top_seeds(self, limit=10):
        return Seed.query.filter(Seed.number != DISABLE_COUNT).order_by(Seed.number).limit(limit).all()

    def get_seed_by_name(self, name):
        return self.db.find_first_object_by(Seed, name=name)

    def get_all_seeds(self):
        return self.db.find_all_objects(Seed)

    def disable_seed(self, name):
        return self.add_or_update(name, {"number": DISABLE_COUNT})

    def delete_seed(self, name):
        seed = self.db.find_first_object_by(Seed, name=name)
        if seed is not None:
            self.db.delete_object(seed)

        return "OK"

    def get_sell_list(self, limit=10):
        return Seed.query.filter(Seed.number != DISABLE_COUNT).order_by(Seed.number.desc()).limit(limit).all()
        # return self.db.find_all_objects(Seed, Seed.number != DISABLE_COUNT)


fm = FarmManager(db_adapter)