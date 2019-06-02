# -*- coding: utf-8 -*-


def test_fixes():
    import tests.test_fixes.dict_fixes
    assert type(tests.test_fixes.dict_fixes) is not list
