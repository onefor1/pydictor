#!/usr/bin/env python
# coding:utf-8
# ename + birth rule
"""
Copyright (c) 2016-2017 pydictor developers (https://github.com/LandGrey/pydictor)
License: GNU GENERAL PUBLIC LICENSE Version 3
"""

from __future__ import unicode_literals
from rules.CBrule import CBrule


def EBrule(ename, birth):
    for _ in CBrule(ename, birth):
        yield _
    # You can continue to add new and useful rules
    #
