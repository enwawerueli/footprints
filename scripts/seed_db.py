#!/usr/bin/env python
import os
import sys
import random

import faker

sys.path.append(os.getcwd())

from app.db import session
from app.db.models import Category, Product


fake = faker.Faker()


def seed_categories_table():
    for i in range(10):
        c = Category(name=fake.word(), description=fake.text())
        session.add(c)
    session.commit()


def seed_products_table():
    categories = session.query(Category.uid).all()
    for i in range(100):
        p = Product(
            name=fake.sentence(),
            sku=fake.pystr(),
            unit_cost=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            unit_price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
            units=fake.pyint(),
            category=session.query(Category).get(random.choice(categories)),
            description=fake.text()
        )
        session.add(p)
    session.commit()


if __name__ == '__main__':
    # seed_categories_table()
    seed_products_table()
