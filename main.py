#!/usr/bin/env python

import sys

from PySide2.QtWidgets import QApplication

from app.main_window import MainWindow
from config import Config


app = QApplication(sys.argv)
app.setOrganizationName(Config.ORG_NAME)
app.setOrganizationDomain(Config.ORG_DOMAIN)
app.setApplicationName(Config.APP_NAME)
app.setApplicationVersion(Config.APP_VERSION)
myapp = MainWindow()
# myapp.showMaximized()
myapp.run()
sys.exit(app.exec_())
