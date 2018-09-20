# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from itertools import chain
from lib2to3.refactor import RefactoringTool

import libfuturize.fixes

futurize_fixes = {
    fix for fix in chain(
        libfuturize.fixes.libfuturize_fix_names_stage1,
        libfuturize.fixes.lib2to3_fix_names_stage1,
        libfuturize.fixes.libfuturize_fix_names_stage2,
        libfuturize.fixes.lib2to3_fix_names_stage2,
    )
}

futurize_tool = RefactoringTool(futurize_fixes)

# tree = futurize_tool.refactor_string(source, self.pathname)


class BothPython2FinderLoader(object):

    def find_module(fullname, path=None):
        pass

    def load_module(fullname):
        pass


hook = BothPython2FinderLoader()
