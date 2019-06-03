# -*- coding: utf-8 -*-
import re
from lib2to3.refactor import RefactoringTool

import six
from source_transform import BaseTransform

from both.fixes import futurize_fixes
from both.fixes import pasteurize_fixes

futurize_tool = RefactoringTool(futurize_fixes)
pasteurize_tool = RefactoringTool(pasteurize_fixes)
fixes_regex = re.compile(
    r'^ *import +__fixes__\.([\w\.]+) *(#.*)?$', re.MULTILINE)


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


class FixesTransform(BaseTransform):

    @staticmethod
    def trigger(mmaped_file, **kwargs):
        if mmaped_file.find(b'from __both__ import fixes') >= 0:
            return True
        if mmaped_file.find(b'from __both__.py3 import fixes') >= 0:
            return True
        if mmaped_file.find(b'from __both__.py2 import fixes') >= 0:
            return True
        return False

    @staticmethod
    def transform(data, pathname, **kwargs):
        if six.PY2:
            if data.find('from __both__.py2 import fixes') >= 0:
                return fixes_regex.sub('', data)
        if six.PY3:
            if data.find('from __both__.py3 import fixes') >= 0:
                return fixes_regex.sub('', data)

        fixes = {
            match.group(1)
            for match in fixes_regex.finditer(data)
        }

        if not fixes:
            return fixes_regex.sub('', data)

        custom_tool = RefactoringTool(fixes)

        fixed_data = str(custom_tool.refactor_string(data, pathname))

        return fixes_regex.sub('', fixed_data)
