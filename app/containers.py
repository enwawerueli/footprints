from functools import reduce
from datetime import date, datetime as dt, time
from decimal import Decimal

from .db import session
from .db.models import Product, Category, Sale
from .utils.func import fuzzy_search


class Products(object):

    HEADERS = ('Item', 'SKU', 'Unit Cost', 'Unit Price', 'Units', 'Created', 'Modified', 'Value')
    NAME, SKU, COST, PRICE, UNITS, CREATED, UPDATED, VALUE = range(len(HEADERS))

    def __init__(self):
        self._category = None
        self._search = None

    @property
    def category(self):
        return self._category and session.query(Category).get(self._category)

    @category.setter
    def category(self, category):
        self._category = category.uid if isinstance(category, Category) else category

    @property
    def search(self):
        return self._search

    @search.setter
    def search(self, text):
        self._search = text or None

    def all(self):
        qry = session.query(Product).order_by('name')
        if self.category is not None:
            qry = qry.filter_by(category_uid=self._category)
        products = qry.all()
        if self.search is not None:
            matches = fuzzy_search(self.search, [product.name for product in products])
            products = [product for name in matches for product in products if product.name == name]
        return products

    @staticmethod
    def get(uid):
        return session.query(Product).get(uid)

    def value(self):
        return reduce(lambda x, y: x + y.value, self.all(), Decimal('0.00'))


class Categories(object):

    def __init__(self):
        self._search = None

    @property
    def search(self):
        return self._search

    @search.setter
    def search(self, text):
        self._search = text or None

    def all(self):
        categories = session.query(Category).order_by('name').all()
        if self.search is not None:
            matches = fuzzy_search(self.search, [category.name for category in categories])
            categories = [category for name in matches for category in categories if category.name == name]
        return categories

    @staticmethod
    def get(uid):
        return session.query(Category).get(uid)


class CartItem(object):
    """Wrapper class for each product instance added to the cart"""

    def __init__(self, uid, qty=1):
        self._uid = uid
        self._qty = qty

    def __str__(self):
        return '<CartItem: %s>' % self.product.name

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        if isinstance(uid, int):
            self._uid = uid

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, qty):
        if isinstance(qty, int):
            self._qty = qty

    @property
    def product(self):
        return session.query(Product).get(self.uid)

    @property
    def total(self):
        """Amount total for this item"""
        return self.product.unit_price * self.qty


class CartItems(object):
    """Container class for a list of CartItem instances"""

    HEADERS = ('Item', 'Quantity', 'Unit Price', 'Total')
    NAME, QTY, PRICE, TOTAL = range(len(HEADERS))

    def __init__(self):
        self._container = []  # Cart starts out empty

    def __contains__(self, item):
        uid = item.uid if isinstance(item, (Product, CartItem)) else item
        return uid in [i.uid for i in self._container]

    def all(self):
        return self._container

    def add(self, uid):
        """Add an item to the container"""
        if uid not in self:
            self._container.append(CartItem(uid))
        return uid in self

    def get(self, uid):
        """Find item by its product uid"""
        return [item for item in self._container if item.uid == uid][0]

    def update(self, item, qty):
        """Update quantity for :item to :qty"""
        item = item if isinstance(item, CartItem) else self.get(item)
        item.qty = qty
        return True

    def remove(self, item):
        """Remove item from the container"""
        item = item if isinstance(item, CartItem) else self.get(item)
        self._container.remove(item)
        return item not in self

    def is_empty(self):
        return not self._container

    def clear(self):
        """Remove all items in the container"""
        self._container = []
        return not self._container

    def total(self):
        return reduce(lambda x, y: x + y.total, self._container, Decimal('0.00'))


class Sales(object):

    HEADERS = ('Timestamp', 'Item', 'Qty', 'Amount')
    TIMESTAMP, NAME, QTY, AMOUNT = range(len(HEADERS))

    def __init__(self):
        t = date.today()
        self._from_date = t
        self._to_date = t

    @property
    def from_date(self):
        return dt.combine(self._from_date, time.min)

    @from_date.setter
    def from_date(self, date):
        self._from_date = date

    @property
    def to_date(self):
        return dt.combine(self._to_date, time.max)

    @to_date.setter
    def to_date(self, date):
        self._to_date = date

    def all(self):
        return session.query(Sale).filter(Sale.created_at >= self.from_date, Sale.created_at <= self.to_date).all()

    def total(self):
        return reduce(lambda x, y: x + y.amount, self.all(), Decimal('0.00'))
