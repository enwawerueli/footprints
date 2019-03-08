import re

from PySide2.QtWidgets import QAction, QApplication


def fuzzy_search(chars, collection):
    """Filter a sequence of strings by matching a set of characters

    :param chars: the set of characters to search.
    :param collection: a sequence (list or other iterable) of strings to search against.
    :return: a sorted subset of the original sequence containing strings in which a match is found.
    """
    chars = re.escape(chars)
    pattern = r''
    for c in chars:
        pattern += c if c == "\\" else '%s.*?' % c
    matches = []
    for string in collection:
        match = re.search(pattern, string, flags=re.I)
        if match:
            matches.append((len(match.group()), match.start(), string))
    return [s for _, _, s in sorted(matches)]


def isiterable(obj):
    """ Check if an object supports iteration """
    try:
        iter(obj)  # Try to get its iterator
    except TypeError:
        return False  # Failed, NOT iterable
    return True


def create_action(parent, label, slot=None, shortcut=None, icon=None, statustip=None):
    action = QAction(label, parent)
    if slot is not None:
        action.triggered.connect(slot)
    if shortcut is not None:
        action.setShortcut(shortcut)
    if icon is not None:
        action.setIcon(icon)
    if statustip is not None:
        action.setStatusTip(statustip)
    return action


def subwindow(ChildWindow):
    def wrapper(parent, *args, **kwargs):
        for w in parent.subwindows:
            if isinstance(w, ChildWindow):
                w.activateWindow()
                w.raise_()
                return None
        w = ChildWindow(parent, *args, **kwargs)
        parent.subwindows.add(w)
        w.show()
        return None
    return wrapper


def close_subwindow(close_event):
    def wrapper(instance, *args, **kwargs):
        instance.parentWidget().subwindows.remove(instance)
        return close_event(instance, *args, **kwargs)
    return wrapper


def center(window):
    """Center window on the desktop"""
    qrect = window.frameGeometry()
    qpoint = QApplication.desktop().availableGeometry().center()
    qrect.moveCenter(qpoint)
    window.move(qrect.topLeft())
