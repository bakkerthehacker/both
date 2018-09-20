# -*- coding: utf-8 -*-
# -*- python version: 2 -*-


def test_smoke():
    something = {}
    assert type(something.viewkeys()) is not list
