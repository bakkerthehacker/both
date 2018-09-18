# -*- coding: utf-8 -*-
import sys
from itertools import chain
# from lib2to3.refactor import RefactoringTool
# import libfuturize.fixes
# import libpasteurize.fixes

futurize_fixes = [
    fix for fix in chain(
        # libfuturize.fixes.libfuturize_fix_names_stage1,
        # libfuturize.fixes.lib2to3_fix_names_stage1,
        # libfuturize.fixes.libfuturize_fix_names_stage2,
        # libfuturize.fixes.lib2to3_fix_names_stage2,
    )
]

hook = None  # TODO


def add_api_hook():
    if hook not in sys.meta_path:
        pass
        # sys.meta_path.append(hook)
