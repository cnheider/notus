#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 04-12-2020
           """

import time

from notus.gtk_dbus.gtk_toaster import GtkToast, init


def main():
    """
    """
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    init("Test")

    helper = Gtk.Button()
    a_icon = helper.render_icon(Gtk.STOCK_DIALOG_INFO, Gtk.IconSize.DIALOG)

    t = GtkToast("Title", "Body")
    t.set_icon_from_pixbuf(a_icon)
    for i in range(10):
        t.title = f"Title{i}"
        t.body = f"Body{i}"
        t.show()
        time.sleep(0.1)
        if i == 4:
            a_icon = helper.render_icon(Gtk.STOCK_DIALOG_QUESTION, Gtk.IconSize.DIALOG)
            t.set_icon_from_pixbuf(a_icon)


main()
