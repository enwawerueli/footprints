import string
import random
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from bcrypt import hashpw, gensalt, checkpw

from . import Base, session
from ..money import Ksh
from ..exceptions import TransactionCodeError


class Product(Base):
    """Class mapping for the products table"""

    __tablename__ = 'products'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), unique=True, nullable=False, index=True)
    sku = sa.Column(sa.String(60), unique=True, nullable=False)
    _unit_cost = sa.Column(sa.String(30), default='0.00')
    _unit_price = sa.Column(sa.String(30), default='0.00')
    units = sa.Column(sa.Integer, default=0)
    category_id = sa.Column(sa.Integer, sa.ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
    description = sa.Column(sa.Text)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)
    sales = relationship('Sale', back_populates='product')
    __table_args__ = (sa.CheckConstraint(units >= 0),)

    def __init__(self, name, sku, unit_cost, unit_price, units, description):
        self.name = name
        self.sku = sku
        self.unit_cost = unit_cost
        self.unit_price = unit_price
        self.units = units
        self.description = description

    @hybrid_property
    def unit_cost(self):
        return Ksh(self._unit_cost)

    @unit_cost.expression
    def unit_cost(cls):
        return cls._unit_cost

    @unit_cost.setter
    def unit_cost(self, value):
        self._unit_cost = str(value.amount)

    @hybrid_property
    def unit_price(self):
        return Ksh(self._unit_price)

    @unit_price.expression
    def unit_price(cls):
        return cls._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = str(value.amount)

    value = property(lambda self: self.unit_cost * self.units)

    def __str__(self):
        return '<Product: %s>' % self.name


class Category(Base):
    """Class mapping for the categories table"""

    __tablename__ = 'categories'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, unique=True, index=True)
    description = sa.Column(sa.Text)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)
    deleted_at = sa.Column(sa.DateTime)
    products = relationship('Product', back_populates='category')

    def __str__(self):
        return '<Category: %s>' % self.name


class Transaction(Base):

    __tablename__ = 'transactions'
    id = sa.Column(sa.Integer, primary_key=True)
    _code = sa.Column(sa.String(30), nullable=False, unique=True, index=True)
    _gross_amount = sa.Column(sa.String(30), default='0.00', nullable=False)
    _discount = sa.Column(sa.String(30), default='0.00')
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    sales = relationship('Sale', back_populates='transaction')

    def __init__(self, code, total, discount):
        self._code = code
        self.gross_amount = total
        self.discount = discount

    @hybrid_property
    def code(self):
        return self._code

    @code.setter
    def transaction_code(self, value):
        self._code = value

    @hybrid_property
    def discount(self):
        return Ksh(self._discount)

    @discount.expression
    def discount(cls):
        return cls._discount

    @discount.setter
    def discount(self, value):
        self._discount = str(value.amount)

    @hybrid_property
    def gross_amount(self):
        return Ksh(self._gross_amount)

    @gross_amount.expression
    def gross_total(cls):
        return cls._gross_amount

    @gross_amount.setter
    def gross_amount(self, value):
        self._gross_amount = str(value.amount)

    net_amount = property(lambda self: self.gross_amount - self.discount)

    def __str__(self):
        return '<Sale: %s>' % (self.code)

    @classmethod
    def generate_transaction_code(cls, length=10, tries=3):
        chars = string.ascii_uppercase + string.digits
        while tries > 0:
            code = ''.join([random.choice(chars) for _ in range(length)])
            if session.query(cls).filter_by(code=code).one_or_none() is not None:
                tries -= 1
                continue
            return code
        raise TransactionCodeError('Could not generate unique code: %s tries' % tries)


class Sale(Base):

    __tablename__ = 'sales'
    product_id = sa.Column(sa.Integer, sa.ForeignKey('products.id'), primary_key=True)
    transaction_id = sa.Column(sa.Integer, sa.ForeignKey('transactions.id'), primary_key=True)
    qty = sa.Column(sa.Integer, nullable=False)
    product = relationship('Product', back_populates='sales')
    transaction = relationship('Transaction', back_populates='sales')
    __table_args__ = (sa.CheckConstraint(qty >= 1), sa.UniqueConstraint('product_id', 'transaction_id'))


class User(Base):
    """Class mapping for users table"""

    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), unique=True, nullable=False)
    _password = sa.Column(sa.String(255), nullable=False)
    admin = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now)

    def __init__(self, name, password):
        self.name = name
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

    def __str__(self):
        return '<User: %s>' % self.name

    def check(self, password):
        return checkpw(password.encode(), self._password)
