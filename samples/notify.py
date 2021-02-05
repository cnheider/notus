#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 27-12-2020
           """

from notus import JobNotificationSession, notify

if __name__ == "__main__":
    notify("test")

    with JobNotificationSession("test2"):
        pass
