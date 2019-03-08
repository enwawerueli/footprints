from functools import reduce
from datetime import date, datetime, time

import sqlalchemy as sa
from sqlalchemy.exc import DBAPIError

from .db import session
from .db.models import Product, Category, Transaction
from .utils import fuzzy_search
from .money import Ksh


class ContainerMeta(type):

    def __getattr__(self, name):
        attr = getattr(session.query(self._model), name, None)
        if attr is None:
            raise AttributeError(
                "type object '%s' has no attribute '%s'" % (self.__name__, name))
        return attr


class Container(metaclass=ContainerMeta):

    _model = None

    def __getattr__(self, name):
        attr = getattr(session.query(self._model), name, None)
        if attr is None:
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (self.__class__.__name__, name))
        return attr

    def __len__(self):
        return len(self.all())

    def all(self):
        raise NotImplementedError("Method not implemented")

    def delete(self, obj):
        if isinstance(obj, int):
            obj = self.get(obj)
        obj.deleted_at = datetime.now()
        try:
            session.flush()
        except DBAPIError:
            session.rollback()
            raise
        session.commit()


class ProductsContainer(Container):

    HEADER_LABELS = ('Item', 'SKU', 'Unit Cost', 'Unit Price', 'Units', 'Created', 'Modified', 'Value')
    NAME, SKU, COST, PRICE, UNITS, CREATED, UPDATED, VALUE = range(len(HEADER_LABELS))

    _model = Product

    def __init__(self):
        self._category = None
        self._search = None

    category = property(lambda self: self._category)
    search = property(lambda self: self._search)

    def add_filter(self, **kwargs):
        if 'category' in kwargs:
            c = kwargs['category']
            self._category = CategoriesContainer.get(c) if isinstance(c, int) else c
        if 'search' in kwargs:
            self._search = kwargs['search'] or None

    def all(self):
        qry = self.filter_by(deleted_at=None).order_by('name')
        if self._category is not None:
            qry = qry.filter_by(category=self._category)
        products = qry.all()
        if self._search is not None:
            matches = fuzzy_search(self._search, [product.name for product in products])
            products = [product for name in matches for product in products if product.name == name]
        return products

    def value(self):
        return reduce(lambda x, y: x + y.value, self.all(), Ksh('0.00'))


class CategoriesContainer(Container):

    _model = Category

    def __init__(self):
        self._search = None

    search = property(lambda self: self._search)

    def add_filter(self, **kwargs):
        if 'search' in kwargs:
            self._search = kwargs['search'] or None

    def all(self):
        categories = self.filter_by(deleted_at=None).order_by('name').all()
        if self.search is not None:
            matches = fuzzy_search(self.search, [category.name for category in categories])
            categories = [category for name in matches for category in categories if category.name == name]
        return categories


class CartItem(object):
    """Wrapper class for each product instance added to the cart"""

    def __init__(self, product, qty=1):
        self._product = product
        self._qty = qty

    def __str__(self):
        return '<CartItem: %s>' % self._product.name

    id = property(lambda self: self._product.id)
    product = property(lambda self: self._product)

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, value):
        self._qty = value

    total = property(lambda self: self._product.unit_price * self._qty)


class CartItemsContainer(object):
    """Container class for a list of CartItem instances"""

    HEADER_LABELS = ('Item', 'Quantity', 'Unit Price', 'Amount')
    NAME, QTY, PRICE, TOTAL = range(len(HEADER_LABELS))

    def __init__(self):
        self._items = []  # initially empty

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        id = item if isinstance(item, int) else item.id
        return id in [i.id for i in self._items]

    def all(self):
        return self._items

    def add(self, product):
        """Add an item to the container"""
        if isinstance(product, int):
            product = ProductsContainer.get(product)
        if product in self:
            item = self.get(product.id)
            item.qty += 1
        else:
            item = CartItem(product)
            self._items.append(item)
        return item

    def get(self, id):
        """Find item by product id"""
        for item in self._items:
            if item.id == id:
                return item

    def update(self, item, qty):
        """Update quantity for :item: to :qty:"""
        if isinstance(item, int):
            item = self.get(item)
        item.qty = qty
        return item

    def remove(self, item):
        """Remove item from the container"""
        if isinstance(item, int):
            item = self.get(item)
        try:
            self._items.remove(item)
        except ValueError:
            pass
        return item not in self

    def is_empty(self):
        return not self._items

    def clear(self):
        """Remove all items in the container"""
        del self._items[:]
        return not self._items

    def total(self):
        return reduce(lambda x, y: x + y.total, self._items, Ksh('0.00'))


class TransactionsContainer(Container):

    HEADER_LABELS = ('Timestamp', 'Transaction ID', 'Gross Amount', 'Discount', 'Net Amount')
    TIMESTAMP, CODE, GROSS_AMOUNT, DISCOUNT, NET_AMOUNT = range(len(HEADER_LABELS))

    _model = Transaction

    def __init__(self):
        today = date.today()
        self._from_date = today
        self._to_date = today

    from_date = property(lambda self: datetime.combine(self._from_date, time.min))
    to_date = property(lambda self: datetime.combine(self._to_date, time.max))

    def add_filter(self, **kwargs):
        if 'from_' in kwargs:
            self._from_date = kwargs['from_']
        if 'to' in kwargs:
            self._to_date = kwargs['to']

    def all(self):
        return self.filter(self._model.created_at >= self.from_date, self._model.created_at <= self.to_date).all()

    def total(self):
        return reduce(lambda x, y: x + y.net_amount, self.all(), Ksh('0.00'))
