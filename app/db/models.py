from datetime import datetime as dt
from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from bcrypt import hashpw, gensalt, checkpw

from . import Base


class Product(Base):
    """Class mapping for the products table"""

    __tablename__ = 'products'
    uid = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(255), unique=True, nullable=False, index=True)
    sku = sa.Column(sa.String(60), unique=True, nullable=False)
    _unit_cost = sa.Column(sa.String(30), default='0.00')
    _unit_price = sa.Column(sa.String(30), default='0.00')
    units = sa.Column(sa.Integer(), default=0)
    category_uid = sa.Column(sa.Integer(), sa.ForeignKey('categories.uid'))
    description = sa.Column(sa.Text())
    created_at = sa.Column(sa.DateTime(), default=dt.now)
    updated_at = sa.Column(sa.DateTime(), default=dt.now, onupdate=dt.now)
    category = relationship('Category', back_populates='products')
    sales = relationship('Sale', back_populates='product')
    __table_args__ = (sa.CheckConstraint('units' >= 0),)

    def __init__(self, name, sku, unit_cost, unit_price, units, category, description):
        self.name = name
        self.sku = sku
        self.unit_cost = unit_cost
        self.unit_price = unit_price
        self.units = units
        if isinstance(category, int):
            self.category_uid = category
        else:
            self.category = category
        self.description = description

    @hybrid_property
    def unit_cost(self):
        return Decimal(self._unit_cost)

    @unit_cost.expression
    def unit_cost(self):
        return self._unit_price

    @unit_cost.setter
    def unit_cost(self, value):
        self._unit_cost = str(value)

    @hybrid_property
    def unit_price(self):
        return Decimal(self._unit_price)

    @unit_price.expression
    def unit_price(self):
        return self.unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = str(value)

    @property
    def value(self):
        return self.unit_cost * self.units

    def __str__(self):
        return '<Product: %s>' % self.name


class Category(Base):
    """Class mapping for the categories table"""

    __tablename__ = 'categories'
    uid = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    description = sa.Column(sa.Text())
    created_at = sa.Column(sa.DateTime(), default=dt.now)
    updated_at = sa.Column(sa.DateTime(), default=dt.now, onupdate=dt.now)
    products = relationship('Product', back_populates='category', cascade='all, delete-orphan')

    def __str__(self):
        return '<Category: %s>' % self.name


class Sale(Base):

    __tablename__ = 'sales'
    uid = sa.Column(sa.Integer(), primary_key=True)
    product_uid = sa.Column(sa.Integer(), sa.ForeignKey('products.uid'))
    qty = sa.Column(sa.Integer(), nullable=False)
    created_at = sa.Column(sa.DateTime(), default=dt.now)
    product = relationship('Product', back_populates='sales')
    __table_args__ = (sa.CheckConstraint('qty' >= 1),)

    @property
    def amount(self):
        return self.product.unit_price * self.qty

    def __str__(self):
        return '<Sale: %s - %s>' % (self.created_at, self.product)


class User(Base):
    """Class mapping for users table"""

    __tablename__ = 'users'
    uid = sa.Column(sa.Integer(), primary_key=True)
    username = sa.Column(sa.String(255), unique=True, nullable=False)
    _password = sa.Column(sa.String(255), nullable=False)
    created_at = sa.Column(sa.DateTime(), default=dt.now)
    updated_at = sa.Column(sa.DateTime(), default=dt.now)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @hybrid_property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.expression
    def password(cls):
        return cls._password

    @password.setter
    def password(self, value):
        self._password = hashpw(value.encode(), gensalt())

    def check(self, password):
        return checkpw(password.encode(), self._password.encode())

    def __str__(self):
        return '<User: %s>' % self.username
