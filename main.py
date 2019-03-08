#!/usr/bin/env python

import sys

from PySide2.QtWidgets import QApplication

from config import Config
from footprints.main_window import MainWindow
from footprints.user_form import UserForm
from footprints.auth_form import AuthForm
from footprints.db import session
from footprints.db.models import User


def run():
    app = QApplication(sys.argv)
    app.setOrganizationName(Config.ORG_NAME)
    app.setOrganizationDomain(Config.ORG_DOMAIN)
    app.setApplicationName(Config.APP_NAME)
    app.setApplicationVersion(Config.APP_VERSION)
    user = session.query(User).first()
    win = MainWindow(user)
    win.showMaximized()
    # auth = UserForm(win) if user is None else AuthForm(user, win)
    # auth.accepted.connect(win.showMaximized)
    # auth.rejected.connect(QApplication.quit)
    # auth.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
