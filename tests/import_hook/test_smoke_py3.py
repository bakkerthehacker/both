# -*- coding: utf-8 -*-
# -*- python version: 3 -*-
import both

print('running test_smoke_py3')


def test_smoke():
    something = {}
    assert type(something.keys()) is not list
