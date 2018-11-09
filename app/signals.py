from PySide2.QtCore import QObject, Signal

from .utils.singleton import Singleton


@Singleton
class AppSignals(QObject):
    """Wrapper class for signals emitted by the application"""

    categories_updated = Signal([], [int])
    products_updated = Signal([], [int])
    cartitems_updated = Signal([], [int])
    sales_updated = Signal([], [int])
