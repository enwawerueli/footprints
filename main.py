#!/usr/bin/env python2.7

import sys

from PySide.QtGui import QApplication

from app.main_window import MainWindow

# decimal.getcontext().prec = 2

ORG_NAME = 'footprints'
ORG_DOMAIN = 'dev.footprints.local'
APP_NAME = 'Footprints'
APP_VERSION = 'v0.3.0'

app = QApplication(sys.argv)
app.setOrganizationName(ORG_NAME)
app.setOrganizationDomain(ORG_DOMAIN)
app.setApplicationName(APP_NAME)
app.setApplicationVersion(APP_VERSION)
myapp = MainWindow()
myapp.showMaximized()
# myapp.run()
sys.exit(app.exec_())
