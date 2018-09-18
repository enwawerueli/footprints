#!/usr/bin/env python2.7

import os
import sys
from decimal import Decimal

sys.path.append(os.getcwd())

from app.db import session
from app.db.models import Product, Category, Sale, User


def seed_categories_table():
    with open('_bak/categories.csv') as f:
        columns = f.readline().strip().split(',')[1:3]
        for ln in f:
            values = ln.strip().split(',')[1:3]
            category = Category(**{k: v for k, v in zip(columns, values)})
            session.add(category)


def seed_products_table():
    with open(os.path.join(os.getcwd(), '_bak/products.csv')) as f:
        columns = f.readline().strip().split(',')[1:8]
        for ln in f:
            values = ln.strip().split(',')[1:8]
            hash_ = {k: v for k, v in zip(columns, values)}
            print hash_
            # hash_['_unit_cost'] = Decimal(hash_['_unit_cost']).quantize(Decimal('0.00'))
            # hash_['_unit_price'] = Decimal(hash_['_unit_price']).quantize(Decimal('0.00'))
            # hash_['units'] = int(hash_['units'])
            # hash_['category_uid'] = int(hash_['category_uid'])
            # product = Product(**{k: v for k, v in zip(columns, hash_)})
            # session.add(product)


def save():
    try:
        session.flush()
    except Exception:
        session.rollback()
        raise
    session.commit()


if __name__ == '__main__':
    # seed_categories_table()
    seed_products_table()
    save()
