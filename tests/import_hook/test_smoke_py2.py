# -*- coding: utf-8 -*-
# -*- python version: 2 -*-
import both


def test_smoke():
    something = {}
    assert type(something.viewkeys()) is not list
