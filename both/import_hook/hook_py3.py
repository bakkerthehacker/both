# -*- coding: utf-8 -*-
from lib2to3.refactor import RefactoringTool

import libpasteurize.fixes

pasteurize_fixes = libpasteurize.fixes.fix_names


pasteurize_tool = RefactoringTool(pasteurize_fixes)


class BothPython3FinderLoader(object):

    def find_module(fullname, path=None):
        pass

    def load_module(fullname):
        pass


hook = BothPython3FinderLoader()
