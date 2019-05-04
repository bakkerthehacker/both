# -*- coding: utf-8 -*-


def test_dict_py2():
    import tests.test_dict.dict_py2
    assert type(tests.test_dict.dict_py2.keys) is list


def test_dict_py3():
    import tests.test_dict.dict_py3
    assert type(tests.test_dict.dict_py3.keys) is not list
