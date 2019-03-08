from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_auth_form import Ui_AuthForm
from .ui import images_rc
from .exceptions import AuthenticationError


class AuthForm(QDialog, Ui_AuthForm):

    def __init__(self, user=None, parent=None, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self._user = user
        self.setupUi(self)
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(QApplication.applicationName())
        self.login_pb.setIcon(QIcon(':/icons/login'))
        if self._user is not None:
            self.username_lb.setText(self._user.name.capitalize())
        self.login_pb.setDisabled(True)
        pixmap = QPixmap(':/icons/user')
        self.avatar_lb.setPixmap(pixmap.scaled(QSize(120, 120), Qt.KeepAspectRatio))
        self.password_le.textChanged.connect(
            lambda: self.login_pb.setEnabled(True if self.password else False))

    password = property(lambda self: self.password_le.text())

    def accept(self):
        try:
            self.authenticate()
        except AuthenticationError as e:
            # TODO: error logging
            QMessageBox.critical(self, QApplication.applicationName(), str(e))
            self.password_le.clear()
            self.password_le.setFocus()
        else:
            return QDialog.accept(self)

    def authenticate(self):
        if self._user is not None and self._user.check(self.password):
            return True
        raise AuthenticationError('Wrong password, try again.')
