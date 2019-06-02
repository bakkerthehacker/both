# -*- coding: utf-8 -*-
from lib2to3.refactor import RefactoringTool

import six
from source_transform import BaseTransform

from both.fixes import futurize_fixes
from both.fixes import pasteurize_fixes

futurize_tool = RefactoringTool(futurize_fixes)
pasteurize_tool = RefactoringTool(pasteurize_fixes)


if six.PY2:
    class PasteurizeTransform(BaseTransform):

        @staticmethod
        def trigger(mmaped_file, **kwargs):
            if six.PY2:
                if mmaped_file.find(b'from __both__ import py3') >= 0:
                    return True
            return False

        @staticmethod
        def transform(data, pathname, **kwargs):
            return str(pasteurize_tool.refactor_string(data, pathname))


if six.PY3:
    class FuturizeTransform(BaseTransform):

        @staticmethod
        def trigger(mmaped_file, **kwargs):
            if six.PY3:
                if mmaped_file.find(b'from __both__ import py2') >= 0:
                    return True
            return False

        @staticmethod
        def transform(data, pathname, **kwargs):
            return str(futurize_tool.refactor_string(data, pathname))
