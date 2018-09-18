from PySide.QtCore import QObject, Signal

from .utils.singleton import Singleton


@Singleton
class AppSignals(QObject):
    """Wrapper class for application signals"""

    categories_updated = Signal((), (int,))
    products_updated = Signal((), (int,))
    cartitems_updated = Signal()
    sales_updated = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.categories_updated.connect(self.products_updated.emit)
