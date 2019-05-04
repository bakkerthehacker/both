# -*- coding: utf-8 -*-


def test_metaclass_py2():
    import tests.test_metaclass.metaclass_py2 as metaclass_py2
    assert type(metaclass_py2.TestMetaAndBase) is metaclass_py2.TestMeta


def test_metaclass_py3():
    import tests.test_metaclass.metaclass_py3 as metaclass_py3
    assert type(metaclass_py3.TestMetaAndBase) is metaclass_py3.TestMeta
