# -*- coding: utf-8 -*-
from __both__ import py2  # noqa


class TestMeta(type):
    pass


class TestBase(object):
    pass


class TestMetaAndBase(TestBase):
    __metaclass__ = TestMeta
    pass
