# -*- coding: utf-8 -*-
from __future__ import print_function
from ._version import get_versions

__author__  = "Anthony Rey"
__email__   = "anthonyrey.simonnot@gmail.com"
__version__ = get_versions()["version"]

del get_versions


def smile():
    return ":)"

def frown():
    return ":("


