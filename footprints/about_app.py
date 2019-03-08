from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from .ui.ui_about_app import Ui_AboutApplication
from .ui import images_rc


class AboutApplication(QDialog, Ui_AboutApplication):

    def __init__(self, parent, *args, **kwargs):
        QDialog.__init__(self, parent, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName())
        pixmap = QPixmap(':/icons/footprints')
        self.appicon_lb.setPixmap(pixmap.scaled(QSize(48, 48), Qt.KeepAspectRatio))
        self.appname_lb.setText('<h2>' + QApplication.applicationName() + '</h2>')
        self.appversion_lb.setText('<b>Version:</b> ' + QApplication.applicationVersion())
        try:
            with open('ABOUT') as f:
                about = f.read()
        except FileNotFoundError:
            pass
        else:
            self.about_te.setText(about)
        try:
            with open('LICENSE') as f:
                license = f.read()
        except FileNotFoundError:
            pass
        else:
            self.license_te.setPlainText(license)
