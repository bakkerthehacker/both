# -*- coding: utf-8 -*-
import __fixes__.lib2to3.fixes.fix_dict  # noqa

from __both__.py2 import fixes  # noqa


thing = {}
keys = thing.keys()
keys + []
