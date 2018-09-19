# -*- coding: utf-8 -*-
import sys
from itertools import chain

import libfuturize.fixes
import libpasteurize.fixes.fix_names
# from lib2to3.refactor import RefactoringTool

if sys.version_info[0] <= 2:
    from hook_py2 import hook
else:
    from hook_py3 import hook

futurize_fixes = {
    fix for fix in chain(
        libfuturize.fixes.libfuturize_fix_names_stage1,
        libfuturize.fixes.lib2to3_fix_names_stage1,
        libfuturize.fixes.libfuturize_fix_names_stage2,
        libfuturize.fixes.lib2to3_fix_names_stage2,
    )
}

pasteurize_fixes = libpasteurize.fixes.fix_names


def add_api_hook():
    if hook not in sys.meta_path:
        pass
        # sys.meta_path.append(hook)
