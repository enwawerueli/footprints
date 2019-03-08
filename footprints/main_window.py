from functools import partial

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_main_window import Ui_MainWindow
from .ui import images_rc
from .transactions_window import TransactionsWindow
from .product_form import ProductForm
from .product_details import ProductDetails
from .category_details import CategoryDetails
from .category_form import CategoryForm
from .checkout_form import CheckoutForm
from .about_app import AboutApplication
from .containers import ProductsContainer, CategoriesContainer, CartItemsContainer
from .utils import create_action


class MainWindow(QMainWindow, Ui_MainWindow):
    """Main application window"""

    categories_updated = Signal([], [int])
    products_updated = Signal([], [int])
    cartitems_updated = Signal([], [int])
    transactions_updated = Signal()

    def __init__(self, user, parent=None, *args, **kwargs):
        QMainWindow.__init__(self, parent, *args, **kwargs)
        self.user = user
        self.products = ProductsContainer()
        self.categories = CategoriesContainer()
        self.cartitems = CartItemsContainer()
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        self.setWindowIcon(QIcon(':/icons/footprints'))
        self.settings = QSettings(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_caption)
        self.update_caption()
        self.timer.start(1000)
        self.action_checkout.triggered.connect(lambda: CheckoutForm(self.cartitems, self).exec_())
        self.action_checkout.setIcon(QIcon(':/icons/cashier'))
        self.action_clear_cart.triggered.connect(self.cartitems.clear)
        self.action_clear_cart.triggered.connect(self.cartitems_updated.emit)
        self.action_clear_cart.setIcon(QIcon.fromTheme('edit-clear-all', QIcon(':/icons/trash')))
        self.action_add_product.triggered.connect(self.show_product_form)
        self.action_add_product.setIcon(QIcon.fromTheme('list-add', QIcon(':/icons/add')))
        self.action_add_category.triggered.connect(lambda: CategoryForm(parent=self).exec_())
        self.action_add_category.setIcon(QIcon.fromTheme('list-add', QIcon(':/icons/add')))
        self.action_preferences.setIcon(QIcon(':/icons/settings'))
        self.action_exit.triggered.connect(QApplication.quit)
        self.action_exit.setIcon(QIcon.fromTheme('application-exit', QIcon(':/icons/exit')))
        self.action_show_sales.triggered.connect(lambda: TransactionsWindow(self))
        self.action_about.triggered.connect(lambda: AboutApplication(self).exec_())
        self.action_about.setIcon(QIcon.fromTheme('help-about', QIcon(':/icons/info')))
        self.action_about_qt.triggered.connect(QApplication.aboutQt)
        self.clear_product_search_pb.setIcon(QIcon.fromTheme('edit-clear', QIcon(':/icons/backspace')))
        self.clear_category_search_pb.setIcon(QIcon.fromTheme('edit-clear', QIcon(':/icons/backspace')))
        self.home_pb.setIcon(QIcon.fromTheme('go-first-symbolic', QIcon(':/icons/first')))
        self.pg_up_pb.setIcon(QIcon.fromTheme('go-next-symbolic-rtl', QIcon(':/icons/back')))
        self.pg_down_pb.setIcon(QIcon.fromTheme('go-previous-symbolic-rtl', QIcon(':/icons/foward')))
        self.end_pb.setIcon(QIcon.fromTheme('go-last-symbolic', QIcon(':/icons/end')))
        self.categories_lw.customContextMenuRequested.connect(self.open_category_menu)
        self.products_tw.customContextMenuRequested.connect(self.open_product_menu)
        self.cartitems_tw.customContextMenuRequested.connect(self.open_cartitem_menu)
        self.detailview_ckb.stateChanged.connect(self.toggle_detailed_view)
        self.categories_lw.currentItemChanged.connect(
            lambda i: self.products.add_filter(category=i.data(Qt.UserRole)) if i is not None else None)
        self.categories_lw.currentItemChanged.connect(lambda: self.products_updated.emit())
        self.search_category_le.textChanged.connect(lambda s: self.categories.add_filter(search=s))
        self.search_category_le.textChanged.connect(lambda: self.categories_updated.emit())
        self.search_product_le.textChanged.connect(lambda s: self.products.add_filter(search=s))
        self.search_product_le.textChanged.connect(lambda: self.products_updated.emit())
        self.products_updated.connect(partial(self.populate_products, None))
        self.products_updated[int].connect(self.populate_products)
        self.categories_updated.connect(partial(self.populate_categories, None))
        self.categories_updated[int].connect(self.populate_categories)
        self.cartitems_updated.connect(partial(self.populate_cartitems, None))
        self.cartitems_updated[int].connect(self.populate_cartitems)
        self.cartitems_updated.connect(self.toggle_cart_actions)
        self.cartitems_updated[int].connect(self.toggle_cart_actions)
        self.pg_down_pb.clicked.connect(self.scroll_page_down)
        self.pg_up_pb.clicked.connect(self.scroll_page_up)
        self.subwindows = set()
        self.populate_categories()
        self.populate_cartitems()

    def showEvent(self, event):
        self.restoreGeometry(self.settings.value('MainWindow/geometry'))
        self.restoreState(self.settings.value('MainWindow/state'))
        self.action_toggle_categories.setChecked(self.categories_dkw.isVisible())
        self.action_toggle_cartitems.setChecked(self.cartitems_dkw.isVisible())
        return QMainWindow.showEvent(self, event)

    def closeEvent(self, event):
        self.settings.setValue('MainWindow/state', self.saveState())
        self.settings.setValue('MainWindow/geometry', self.saveGeometry())
        return QMainWindow.closeEvent(self, event)

    def update_caption(self):
        self.table_caption_lb.setText(
            'Products in stock today, ' + QDateTime.currentDateTime().toString('MMM dd yyyy, HH:mm:ss'))

    def scroll_page_down(self):
        rect = self.products_tw.rect()
        item = self.products_tw.itemAt(rect.left(), rect.bottom() - self.products_tw.horizontalHeader().height())
        self.products_tw.scrollToItem(item, QAbstractItemView.PositionAtTop)

    def scroll_page_up(self):
        rect = self.products_tw.rect()
        item = self.products_tw.itemAt(rect.left(), rect.top() - self.products_tw.horizontalHeader().height())
        self.products_tw.scrollToItem(item, QAbstractItemView.PositionAtBottom)

    def populate_categories(self, selected=None):
        self.categories_lw.clear()
        categories = self.categories.all()
        if not categories:
            if self.categories.search is not None:
                text = "No category matching '%s'." % self.categories.search
            else:
                text = 'No categories to display.'
            lwi = QListWidgetItem(text, self.categories_lw)
            lwi.setData(Qt.UserRole, 0)
            return None
        current_item = None
        if self.categories.search is None:
            lwi = QListWidgetItem('All Categories', self.categories_lw)
            lwi.setData(Qt.UserRole, 0)
            current_item = lwi
        if selected is None and self.products.category is not None:
            selected = self.products.category.id
        for category in categories:
            lwi = QListWidgetItem(category.name, self.categories_lw)
            lwi.setData(Qt.UserRole, category.id)
            if category.id == selected:
                current_item = lwi
        self.categories_lw.setCurrentItem(current_item)
        return None

    def populate_products(self, selected=None):
        self.products_tw.clear()
        self.products_tw.clearSpans()
        products = self.products.all()
        n_rows = len(products) + 1
        n_columns = len(self.products.HEADER_LABELS)
        self.products_tw.setColumnCount(n_columns)
        self.products_tw.setHorizontalHeaderLabels(self.products.HEADER_LABELS)
        self.products_tw.horizontalHeader().setSectionResizeMode(self.products.NAME, QHeaderView.Stretch)
        self.products_tw.setRowCount(n_rows)
        self.toggle_detailed_view(self.detailview_ckb.checkState())
        for row in range(n_rows):
            twi = QTableWidgetItem()
            twi.setData(Qt.UserRole, None)
            self.products_tw.setVerticalHeaderItem(row, twi)
        if not products:
            if self.products.category is not None and self.products.search is not None:
                text = ("No products from category '%s' matching '%s'."
                        % (self.products.category.name, self.products.search))
            elif self.products.category is not None:
                text = "No products from category '%s'." % self.products.category.name
            elif self.products.search is not None:
                text = "No products matching '%s'." % self.products.search
            else:
                text = 'No products to display.'
            self.products_tw.setItem(0, 0, QTableWidgetItem(text))
            self.products_tw.setSpan(0, 0, 1, n_columns)
            return None
        gen_rindex = (i for i in range(n_rows))
        for product in products:
            row = next(gen_rindex)
            twi = self.products_tw.verticalHeaderItem(row)
            twi.setData(Qt.UserRole, product.id)
            self.products_tw.setItem(row, self.products.NAME, QTableWidgetItem(product.name))
            self.products_tw.setItem(row, self.products.SKU, QTableWidgetItem(product.sku))
            twi = QTableWidgetItem(str(product.unit_cost))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.COST, twi)
            twi = QTableWidgetItem(str(product.unit_price))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.PRICE, twi)
            twi = QTableWidgetItem(str(product.units))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.UNITS, twi)
            self.products_tw.setItem(
                row, self.products.CREATED, QTableWidgetItem(product.created_at.strftime('%d/%m/%Y, %I:%M:%S %p')))
            self.products_tw.setItem(
                row, self.products.UPDATED, QTableWidgetItem(product.updated_at.strftime('%d/%m/%Y, %I:%M:%S %p')))
            twi = QTableWidgetItem(str(product.value))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.products_tw.setItem(row, self.products.VALUE, twi)
            if product.id == selected:
                self.products_tw.selectRow(row)
            self.products_tw.setRowHidden(row, False)  # incase it was previously hidden!
        row = next(gen_rindex)
        self.products_tw.setSpan(row, 0, 1, n_columns - 1)
        label_twi = QTableWidgetItem('Total Value :')
        value_twi = QTableWidgetItem(str(self.products.value()))
        value_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, value_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.products_tw.setItem(row, self.products.NAME, label_twi)
        self.products_tw.setItem(row, self.products.VALUE, value_twi)
        return None

    def toggle_detailed_view(self, show):
        for c in (self.products.COST, self.products.CREATED, self.products.UPDATED, self.products.VALUE):
            self.products_tw.setColumnHidden(c, not show)
        if self.products:
            self.products_tw.setRowHidden(self.products_tw.rowCount() - 1, not show)

    def populate_cartitems(self, selected=None):
        self.cartitems_tw.clear()
        self.cartitems_tw.clearSpans()
        items = self.cartitems.all()
        n_rows = len(items) + 1
        n_columns = len(self.cartitems.HEADER_LABELS)
        self.cartitems_tw.setColumnCount(n_columns)
        self.cartitems_tw.setHorizontalHeaderLabels(self.cartitems.HEADER_LABELS)
        self.cartitems_tw.horizontalHeader().setSectionResizeMode(self.products.NAME, QHeaderView.Stretch)
        self.cartitems_tw.setRowCount(n_rows)
        for row in range(n_rows):
            twi = QTableWidgetItem()
            twi.setData(Qt.UserRole, None)
            self.cartitems_tw.setVerticalHeaderItem(row, twi)
        if not items:
            self.cartitems_tw.setItem(0, 0, QTableWidgetItem('Cart is currently empty.'))
            self.cartitems_tw.setSpan(0, 0, 1, n_columns)
            return None
        gen_rindex = (i for i in range(n_rows))
        for item in items:
            row = next(gen_rindex)
            product = item.product
            twi = self.cartitems_tw.verticalHeaderItem(row)
            twi.setData(Qt.UserRole, item.id)
            self.cartitems_tw.setVerticalHeaderItem(row, twi)
            self.cartitems_tw.setItem(row, self.cartitems.NAME, QTableWidgetItem(product.name))
            sb = QSpinBox(self)
            sb.setFrame(False)
            sb.setValue(item.qty)
            sb.setMaximum(item.product.units)
            sb.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            sb.valueChanged.connect(partial(self.update_cartitem, item))
            self.cartitems_tw.setCellWidget(row, self.cartitems.QTY, sb)
            twi = QTableWidgetItem(str(product.unit_price))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cartitems_tw.setItem(row, self.cartitems.PRICE, twi)
            twi = QTableWidgetItem(str(item.total))
            twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cartitems_tw.setItem(row, self.cartitems.TOTAL, twi)
            if item.product.id == selected:
                self.cartitems_tw.selectRow(row)
        row = next(gen_rindex)
        self.cartitems_tw.setSpan(row, 0, 1, n_columns - 1)
        label_twi = QTableWidgetItem('Total Amount:')
        total_twi = QTableWidgetItem(str(self.cartitems.total()))
        total_twi.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        for twi in (label_twi, total_twi):
            font = twi.font()
            font.setBold(True)
            twi.setFont(font)
        self.cartitems_tw.setItem(row, self.cartitems.NAME, label_twi)
        self.cartitems_tw.setItem(row, self.cartitems.TOTAL, total_twi)
        return None

    def open_category_menu(self, pos):
        lwi = self.categories_lw.itemAt(pos)
        if lwi is None:
            return None
        id = lwi.data(Qt.UserRole)
        if id is None:
            return None
        category = self.categories.get(id)
        menu = QMenu(self)
        action_show = create_action(
            self, 'Details', icon=QIcon.fromTheme('view-more-symbolic', QIcon(':/icons/more')),
            slot=lambda: CategoryDetails(category, self).exec_(), statustip='Show category details')
        action_edit = create_action(
            self, 'Edit', icon=QIcon.fromTheme('document-edit-symbolic', QIcon(':/icons/edit')),
            slot=lambda: CategoryForm(category, self).exec_(), statustip='Edit this category')
        action_del = create_action(
            self, 'Delete', icon=QIcon.fromTheme('edit-delete', QIcon(':/icons/delete')),
            slot=partial(self.delete_category, category), statustip='Delete this category')
        menu.addActions((action_show, action_edit, action_del))
        menu.exec_(self.categories_lw.mapToGlobal(pos))
        return None

    def open_product_menu(self, pos):
        twi = self.products_tw.itemAt(pos)
        if twi is None:
            return None
        id = self.products_tw.verticalHeaderItem(twi.row()).data(Qt.UserRole)
        if id is None:
            return None
        product = self.products.get(id)
        menu = QMenu(self)
        action_add = create_action(
            self, 'Add to cart', icon=QIcon.fromTheme('list-add', QIcon(':/icons/add')),
            slot=partial(self.add_cartitem, product), statustip='Add this product to cart')
        action_show = create_action(
            self, 'Details', icon=QIcon.fromTheme('view-more-symbolic', QIcon(':/icons/more')),
            slot=lambda: ProductDetails(product, self).exec_(), statustip='Show product details')
        action_edit = create_action(
            self, 'Edit', icon=QIcon.fromTheme('document-edit-symbolic', QIcon(':/icons/edit')),
            slot=lambda: ProductForm(product, self).exec_(), statustip='Edit this product')
        action_del = create_action(
            self, 'Delete', icon=QIcon.fromTheme('edit-delete', QIcon(':/icons/delete')),
            slot=partial(self.delete_product, product), statustip='Delete this product')
        menu.addActions((action_add, action_show, action_edit, action_del))
        pos += QPoint(self.products_tw.verticalHeader().width(), self.products_tw.horizontalHeader().height())
        menu.exec_(self.products_tw.mapToGlobal(pos))
        return None

    def open_cartitem_menu(self, pos):
        if self.cartitems.is_empty():
            return None
        twi = self.cartitems_tw.itemAt(pos)
        id = self.cartitems_tw.verticalHeaderItem(twi.row()).data(Qt.UserRole)\
            if twi is not None else None
        menu = QMenu(self)
        if id is not None:
            action_remove = create_action(
                self, 'Remove', icon=QIcon.fromTheme('list-remove', QIcon(':/icons/remove')),
                statustip='Remove this item from cart')
            action_remove.triggered.connect(partial(self.cartitems.remove, id))
            action_remove.triggered.connect(self.cartitems_updated.emit)
            menu.addAction(action_remove)
        action_checkout = create_action(
            self, 'Checkout', icon=QIcon(':/icons/cashier'), slot=lambda: CheckoutForm(self.cartitems, self).exec_(),
            statustip='Go to checkout')
        menu.addAction(action_checkout)
        if id is None or len(self.cartitems) > 1:
            action_remove_all = create_action(
                self, 'Remove all', icon=QIcon.fromTheme('edit-clear-all', QIcon(':/icons/trash')),
                statustip='Remove all items from cart')
            action_remove_all.triggered.connect(self.cartitems.clear)
            action_remove_all.triggered.connect(self.cartitems_updated.emit)
            menu.addAction(action_remove_all)
        pos += QPoint(self.cartitems_tw.verticalHeader().width(), self.cartitems_tw.horizontalHeader().height())
        menu.exec_(self.cartitems_tw.mapToGlobal(pos))
        return None

    def show_product_form(self):
        while True:
            if self.categories.first() is None:
                if QMessageBox.information(
                        self, QApplication.applicationName(), 'Create a category first before adding products.',
                        QMessageBox.Ok | QMessageBox.Cancel) != QMessageBox.Ok:
                    return None
                if CategoryForm(parent=self).exec_() != QDialog.Accepted:
                    return None
            return ProductForm(parent=self).exec_()

    def delete_category(self, category):
        if QMessageBox.question(
                self, QApplication.applicationName(),
                ('Are you sure you wish to delete this category?\n'
                 'WARNING! All products in this category will also be deleted.'),
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return None
        updated = False
        for product in category.products:
            if product in self.cartitems:
                self.cartitems.remove(product.id)
                updated = True
        if updated is True:
            self.cartitems_updated.emit()
        self.categories.delete(category)
        self.categories_updated.emit()
        return None

    def delete_product(self, product):
        if QMessageBox.question(
                self, QApplication.applicationName(), 'Are you sure you wish to delete this product?',
                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return None
        if product in self.cartitems:
            self.cartitems.remove(product.id)
            self.cartitems_updated.emit()
        self.products.delete(product)
        self.products_updated.emit()
        return None

    def add_cartitem(self, product):
        if product.units < 1:
            return QMessageBox.information(
                self, QApplication.applicationName(), 'Units: %d, Item out of stock!' % product.units)
        if product in self.cartitems:
            item = self.cartitems.get(product.id)
            self.update_cartitem(item, item.qty + 1)
        else:
            self.cartitems.add(product)
        self.cartitems_updated[int].emit(product.id)
        return None

    def update_cartitem(self, item, units):
        if units == 0:
            self.cartitems.remove(item)
        elif units > item.product.units:
            return QMessageBox.information(
                self, QApplication.applicationName(), 'All available units already added to cart!')
        else:
            self.cartitems.update(item, units)
        self.cartitems_updated[int].emit(item.id)

    def toggle_cart_actions(self, *args):
        enabled = not self.cartitems.is_empty()
        for action in (self.action_checkout, self.action_clear_cart):
            action.setEnabled(enabled)
