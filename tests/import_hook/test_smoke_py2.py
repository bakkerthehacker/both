# -*- coding: utf-8 -*-
# -*- python api: 2 -*-


def test_smoke():
    something = {}
    assert type(something.viewkeys()) is not list
