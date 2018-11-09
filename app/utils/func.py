import re

from PySide2.QtWidgets import QAction, QApplication


def isiterable(obj):
    """ Check if an object supports iteration """
    try:
        iter(obj)  # Try to get its iterator
    except TypeError:
        return False  # Failed, NOT iterable
    return True


def fuzzy_search(chars, collection):
    """ Perform a fuzzy search for a set of characters against a string
    and filter out those where a match is found.

    :param chars: the characters to search.
    :param collection: a list of strings to search against, or other iterable
                       whose items are strings.
    :return: a list of those strings where a match was found.
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


def subwindow(klass):
    def wrapper(parent, *args, **kwargs):
        for w in parent.subwindows:
            if not isinstance(w, klass):
                continue
            w.activateWindow()
            w.raise_()
            return None
        w = klass(parent, *args, **kwargs)
        parent.subwindows.add(w)
        w.show()
        return None
    return wrapper


def close_subwindow(event_method):
    def wrapper(receiver, *args, **kwargs):
        parent = receiver.parent()
        parent.subwindows.remove(receiver)
        return event_method(receiver, *args, **kwargs)
    return wrapper


def center(window):
    """ Center window on the desktop """
    qrect = window.frameGeometry()
    qpoint = QApplication.desktop().availableGeometry().center()
    qrect.moveCenter(qpoint)
    window.move(qrect.topLeft())
