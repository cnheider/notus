#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 27-12-2020
           """

import time

from notus import JobNotificationSession, notify

if __name__ == "__main__":
  notify("test")

  with JobNotificationSession("test2") as jns:
    time.sleep(1)
    jns('test3')
    for i in range(4, 9):
      time.sleep(1)
      jns(f'{"".join(["*"] * i)}')
    time.sleep(2)
