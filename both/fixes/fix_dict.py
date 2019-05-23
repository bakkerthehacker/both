# -*- coding: utf-8 -*-
# Copyright 2007 Google, Inc. All Rights Reserved.
# Licensed to PSF under a Contributor Agreement.
from lib2to3 import fixer_base
from lib2to3.fixer_util import Name


class FixDict(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = """
    power< head=any+
         trailer< '.' method=('keys'|'items'|'values') >
         parens=trailer< '(' ')' >
         tail=any*
    >
    """

    def transform(self, node, results):
        method = results['method'][0]

        method_name = method.value
        method_name = u'view' + method_name

        method.replace(Name(method_name, prefix=method.prefix))
