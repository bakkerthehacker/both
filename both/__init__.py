# -*- coding: utf-8 -*-
from lib2to3.refactor import RefactoringTool

from .fixes import futurize_fixes
from .fixes import pasteurize_fixes
# from .fixes import lib2to3_fixes

futurize_tool = RefactoringTool(futurize_fixes)
pasteurize_tool = RefactoringTool(pasteurize_fixes)


def futurize(code_string, pathname):
    return str(futurize_tool.refactor_string(code_string, pathname))


def pasteurize(code_string, pathname):
    return str(pasteurize_tool.refactor_string(code_string, pathname))
