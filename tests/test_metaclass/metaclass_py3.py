# -*- coding: utf-8 -*-
from __both__ import py3  # noqa


class TestMeta(type):
    pass


class TestBase(object):
    pass


class TestMetaAndBase(TestBase, metaclass=TestMeta):
    pass
