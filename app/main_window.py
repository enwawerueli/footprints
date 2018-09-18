from datetime import date

from PySide.QtGui import *
from PySide.QtCore import *

from .ui.ui_main_window import Ui_MainWindow
from .auth_form import AuthForm
from .sales_window import SalesWindow
from .product_form import ProductForm
from .product_details import ProductDetails
from .category_details import CategoryDetails
from .category_form import CategoryForm
from .checkout_form import CheckoutForm
from .user_form import UserForm
from .containers import Products, Categories, CartItems
from .utils.func import create_action
from .signals import AppSignals
from .db import session


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main application window"""

    signals = AppSignals()

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        icon = QIcon()
        icon.addPixmap(QPixmap(':/icons/footprints'), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.settings = QSettings()
        self.checkout_pb.setDisabled(True)
        self.table_caption_lb.setText('Products in stock today, %s' % date.today().strftime('%b %d, %Y'))
        self.action_add_product.activated.connect(lambda: ProductForm(self).exec_())
        self.action_add_category.activated.connect(lambda: CategoryForm(self).exec_())
        self.action_add_user.activated.connect(lambda: UserForm(self).exec_())
        self.action_exit.activated.connect(QApplication.quit)
        self.action_toggle_categories.activated.connect(
            lambda: self.categories_dkw.setVisible(not self.categories_dkw.isVisible()))
        self.action_toggle_cartitems.activated.connect(
            lambda: self.cartitems_dkw.setVisible(not self.cartitems_dkw.isVisible()))
        self.action_show_sales.activated.connect(lambda: SalesWindow(self))
        self.categories_lw.customContextMenuRequested.connect(self.open_category_menu)
        self.products_tw.customContextMenuRequested.connect(self.open_product_menu)
        self.cart_tw.customContextMenuRequested.connect(self.open_cartitem_menu)
        self.detailview_ckb.stateChanged.connect(self.signals.products_updated)
        self.categories_lw.itemActivated.connect(self.show_category)
        self.search_category_le.textChanged.connect(self.search_category)
        self.search_product_le.textChanged.connect(self.search_product)
        self.clear_category_search_pb.clicked.connect(self.search_category_le.clear)
        self.clear_product_search_pb.clicked.connect(self.search_product_le.clear)
        self.clear_cart_pb.clicked.connect(self.clear_cartitems)
        self.add_category_pb.clicked.connect(lambda: CategoryForm(self).exec_())
        self.add_product_pb.clicked.connect(lambda: ProductForm(self).exec_())
        self.signals.products_updated.connect(self.populate_products)
        self.signals.products_updated[int].connect(self.populate_products)
        self.signals.categories_updated.connect(self.populate_categories)
        self.signals.categories_updated[int].connect(self.populate_categories)
        self.signals.cartitems_updated.connect(self.populate_cartitems)
        self.signals.cartitems_updated.connect(self.allow_checkout)
        self.subwindows = set()
        self.products = Products()
        self.categories = Categories()
        self.cartitems = CartItems()
        self.populate_categories()
        self.populate_products()
        self.populate_cartitems()
        self.checkout_pb.clicked.connect(lambda: CheckoutForm(self.cartitems_dkw, self.cartitems).exec_())

    def showEvent(self, event):
        self.restoreGeometry(self.settings.value('MainWindow/geometry'))
        self.restoreState(self.settings.value('MainWindow/state'))
        return QMainWindow.showEvent(self, event)

    def closeEvent(self, event):
        self.settings.setValue('MainWindow/state', self.saveState())
        self.settings.setValue('MainWindow/geometry', self.saveGeometry())
        return QMainWindow.closeEvent(self, event)

    def populate_categories(self, selected=None):
        self.categories_lw.clear()
        if selected is None and self.products.category is not None:
            selected = self.products.category.uid
        categories = self.categories.all()
        if not categories:
            if self.categories.search is not None:
                text = 'No category matching \'%s\'' % self.categories.search
            else:
                text = 'No categories to display'
            QListWidgetItem(text, self.categories_lw)
            return None
        current_item = None
        if self.categories.search is None:
            all_ = QListWidgetItem('All Categories', self.categories_lw)
            all_.setData(Qt.UserRole, None)
            current_item = all_
        for category in categories:
            item = QListWidgetItem(category.name, self.categories_lw)
            item.setData(Qt.UserRole, category.uid)
            if category.uid == selected:
                current_item = item
        if current_item is not None:
            self.categories_lw.setCurrentItem(current_item)
            self.show_category(current_item)
        return None

    def populate_products(self, selected=None):
        self.products_tw.clear()
        self.products_tw.clearSpans()
        self.products_tw.setColumnCount(len(self.products.HEADERS))
        self.products_tw.setHorizontalHeaderLabels(self.products.HEADERS)
        for c in (self.products.COST, self.products.CREATED, self.products.UPDATED, self.products.VALUE):
            self.products_tw.setColumnHidden(c, self.detailview_ckb.checkState() == Qt.Unchecked)
        self.products_tw.horizontalHeader().setResizeMode(self.products.NAME, QHeaderView.Stretch)
        products = self.products.all()
        self.products_tw.setRowCount(len(products) or 1)
        if not products:
            self.products_tw.setVerticalHeaderItem(0, QTableWidgetItem('#'))
            if self.products.category is not None and self.products.search is not None:
                text = ('No products from category \'%s\' matching \'%s\''
                        % (self.products.category.name, self.products.search))
            elif self.products.category is not None:
                text = 'No products from category \'%s\'' % self.products.category.name
            elif self.products.search is not None:
                text = 'No products matching \'%s\'' % self.products.search
            else:
                text = 'No products to display'
            self.products_tw.setItem(0, 0, QTableWidgetItem(text))
            self.products_tw.setSpan(0, 0, 1, self.products_tw.columnCount())
            return None
        for row, product in enumerate(products):
            vhi = QTableWidgetItem(str(row + 1))
            vhi.setData(Qt.UserRole, product.uid)
            self.products_tw.setVerticalHeaderItem(row, vhi)
            self.products_tw.setItem(row, self.products.NAME, QTableWidgetItem(product.name))
            self.products_tw.setItem(row, self.products.SKU, QTableWidgetItem(product.sku))
            cost_twi = QTableWidgetItem('{:,}'.format(product.unit_cost))
            cost_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.COST, cost_twi)
            price_twi = QTableWidgetItem('{:,}'.format(product.unit_price))
            price_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.PRICE, price_twi)
            self.products_tw.setItem(row, self.products.UNITS, QTableWidgetItem(str(product.units)))
            self.products_tw.setItem(row, self.products.CREATED,
                                     QTableWidgetItem(product.created_at.strftime('%b %d %Y, %H:%M:%S')))
            self.products_tw.setItem(row, self.products.UPDATED,
                                     QTableWidgetItem(product.updated_at.strftime('%b %d %Y, %H:%M:%S')))
            value_twi = QTableWidgetItem('{:,}'.format(product.value))
            value_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.VALUE, value_twi)
            if product.uid == selected:
                self.products_tw.selectRow(row)
        if self.detailview_ckb.checkState() != Qt.Checked:
            return None
        end = self.products_tw.rowCount()
        self.products_tw.insertRow(end)
        self.products_tw.setVerticalHeaderItem(end, QTableWidgetItem('#'))
        self.products_tw.setSpan(end, self.products.NAME, 1, self.products.VALUE)
        label_twi = QTableWidgetItem('Total Value :')
        total_twi = QTableWidgetItem('{:,}'.format(self.products.value()))
        total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, total_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.products_tw.setItem(end, self.products.NAME, label_twi)
        self.products_tw.setItem(end, self.products.VALUE, total_twi)
        return None

    def populate_cartitems(self):
        self.cart_tw.clear()
        self.cart_tw.clearSpans()
        self.cart_tw.setColumnCount(len(self.cartitems.HEADERS))
        self.cart_tw.setHorizontalHeaderLabels(self.cartitems.HEADERS)
        self.cart_tw.horizontalHeader().setResizeMode(self.cartitems.NAME, QHeaderView.Stretch)
        items = self.cartitems.all()
        self.cart_tw.setRowCount(len(items) or 1)
        if not items:
            self.cart_tw.setVerticalHeaderItem(0, QTableWidgetItem('#'))
            self.cart_tw.setItem(0, 0, QTableWidgetItem('Cart is currently empty'))
            self.cart_tw.setSpan(0, 0, 1, self.cart_tw.columnCount())
            return None
        for row, item in enumerate(items):
            product = item.product
            vhi = QTableWidgetItem(str(row + 1))
            vhi.setData(Qt.UserRole, item.uid)
            self.cart_tw.setVerticalHeaderItem(row, vhi)
            self.cart_tw.setItem(row, self.cartitems.NAME, QTableWidgetItem(product.name))
            sb = QSpinBox()
            sb.setFrame(False)
            sb.setValue(item.qty)
            sb.setMaximum(item.product.units)
            sb.valueChanged.connect(lambda value, uid=item.uid: self.update_cartitem(uid, value))
            self.cart_tw.setCellWidget(row, self.cartitems.QTY, sb)
            price_twi = QTableWidgetItem('{:,}'.format(product.unit_price))
            price_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cart_tw.setItem(row, self.cartitems.PRICE, price_twi)
            sub_total_twi = QTableWidgetItem('{:,}'.format(item.total))
            sub_total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cart_tw.setItem(row, self.cartitems.TOTAL, sub_total_twi)
        end = self.cart_tw.rowCount()
        self.cart_tw.insertRow(end)
        self.cart_tw.setVerticalHeaderItem(end, QTableWidgetItem('#'))
        self.cart_tw.setSpan(end, self.cartitems.NAME, 1, self.cartitems.TOTAL)
        label_twi = QTableWidgetItem('Grand Total :')
        total_twi = QTableWidgetItem('{:,}'.format(self.cartitems.total()))
        total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, total_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.cart_tw.setItem(end, self.cartitems.NAME, label_twi)
        self.cart_tw.setItem(end, self.cartitems.TOTAL, total_twi)
        return None

    def open_category_menu(self, pos):
        item = self.categories_lw.itemAt(pos)
        if item is None:
            return None
        uid = item.data(Qt.UserRole)
        if uid is None:
            return None
        menu = QMenu(self)
        act_show = create_action(self, 'Details', statustip='Show category details')
        act_edit = create_action(self, 'Edit', statustip='Edit this category')
        act_del = create_action(self, 'Delete', statustip='Delete this category')
        menu.addActions((act_show, act_edit, act_del))
        action = menu.exec_(self.categories_lw.mapToGlobal(pos))
        category = self.categories.get(uid)
        if action == act_show:
            CategoryDetails(self, category).exec_()
        elif action == act_edit:
            CategoryForm(self, category).exec_()
        elif action == act_del:
            self.delete_category(category)
        return None

    def open_product_menu(self, pos):
        item = self.products_tw.itemAt(pos)
        if item is None:
            return None
        uid = self.products_tw.verticalHeaderItem(item.row()).data(Qt.UserRole)
        if uid is None:
            return None
        menu = QMenu(self)
        act_add = create_action(self, 'Add to cart', statustip='Add this product to cart')
        act_show = create_action(self, 'Details', statustip='Show product details')
        act_edit = create_action(self, 'Edit', statustip='Edit this product')
        act_del = create_action(self, 'Delete', statustip='Delete this product')
        menu.addActions((act_add, act_show, act_edit, act_del))
        pos += QPoint(self.products_tw.verticalHeader().width(), self.products_tw.horizontalHeader().height())
        action = menu.exec_(self.products_tw.mapToGlobal(pos))
        product = self.products.get(uid)
        if action == act_add:
            self.add_cartitem(uid)
        elif action == act_show:
            ProductDetails(self, product).exec_()
        elif action == act_edit:
            ProductForm(self, product).exec_()
        elif action == act_del:
            self.delete_product(product)
        return None

    def open_cartitem_menu(self, pos):
        item = self.cart_tw.itemAt(pos)
        if item is None:
            return None
        uid = self.cart_tw.verticalHeaderItem(item.row()).data(Qt.UserRole)
        if uid is None:
            return None
        menu = QMenu(self)
        act_remove = create_action(self, 'Remove', statustip='Remove this item from cart')
        menu.addAction(act_remove)
        pos += QPoint(self.cart_tw.verticalHeader().width(), self.cart_tw.horizontalHeader().height())
        action = menu.exec_(self.cart_tw.mapToGlobal(pos))
        if action == act_remove:
            self.remove_cartitem(uid)
        return None

    def delete_category(self, category):
        btn = QMessageBox.question(self, QApplication.applicationName(),
                                   ('Are you sure you wish to delete this category?\n'
                                    'WARNING! All products in this category will also be deleted.'),
                                   QMessageBox.Yes | QMessageBox.No)
        if btn != QMessageBox.Yes:
            return None
        session.delete(category)
        session.commit()
        self.signals.categories_updated.emit()
        return None

    def delete_product(self, product):
        btn = QMessageBox.question(self, QApplication.applicationName(),
                                   'Are you sure you wish to delete this product?', QMessageBox.Yes | QMessageBox.No)
        if btn != QMessageBox.Yes:
            return None
        session.delete(product)
        session.commit()
        self.signals.products_updated.emit()
        return None

    def add_cartitem(self, uid):
        available = self.products.get(uid).units
        if available < 1:
            QMessageBox.information(self, QApplication.applicationName(), 'Units: %d, Item out of stock!' % available)
        elif uid in self.cartitems:
            self.update_cartitem(uid, self.cartitems.get(uid).qty + 1)
        elif self.cartitems.add(uid):
            self.signals.cartitems_updated.emit()
        self.checkout_pb.setEnabled(not self.cartitems.is_empty())

    def update_cartitem(self, uid, value):
        available = self.products.get(uid).units
        if value == 0:
            self.cartitems.remove(uid)
        elif value > available:
            QMessageBox.information(self.cart_tw, QApplication.applicationName(),
                                    'All available units already added to cart!')
        else:
            self.cartitems.update(uid, value)
        self.signals.cartitems_updated.emit()

    def remove_cartitem(self, uid):
        self.cartitems.remove(uid)
        self.signals.cartitems_updated.emit()

    def clear_cartitems(self):
        self.cartitems.clear()
        self.signals.cartitems_updated.emit()

    def allow_checkout(self, *args):
        self.checkout_pb.setEnabled(not self.cartitems.is_empty())

    def show_category(self, item):
        self.products.category = item.data(Qt.UserRole)
        self.signals.products_updated.emit()

    def search_product(self, text):
        self.products.search = text
        self.signals.products_updated.emit()

    def search_category(self, text):
        self.categories.search = text
        self.signals.categories_updated.emit()

    def run(self):
        auth = AuthForm(self)
        auth.accepted.connect(self.showMaximized)
        auth.rejected.connect(QApplication.quit)
        auth.show()
