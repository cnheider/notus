#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 04-12-2020
           """

from notus.win10 import Win10Toaster


def main():
    """
    """
    import time

    toaster = Win10Toaster()
    toaster.show_toast("Hello World!!!", "Python is 10 seconds awsm!", duration=10)

    while toaster.notification_active:  # Wait for threaded notification to finish
        time.sleep(0.1)


main()
