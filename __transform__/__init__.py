# -*- coding: utf-8 -*-
import six
from source_transform import BaseTransform

from both import futurize
from both import pasteurize


if six.PY2:
    class FuturizeTransform(BaseTransform):

        @staticmethod
        def trigger(mmaped_file, **kwargs):
            if six.PY2:
                if mmaped_file.find(b'from __both__ import py3') >= 0:
                    return True
            return False

        @staticmethod
        def transform(data, pathname, **kwargs):
            return pasteurize(data, pathname)


if six.PY3:
    class PasteurizeTransform(BaseTransform):

        @staticmethod
        def trigger(mmaped_file, **kwargs):
            if six.PY3:
                if mmaped_file.find(b'from __both__ import py2') >= 0:
                    return True
            return False

        @staticmethod
        def transform(data, pathname, **kwargs):
            return futurize(data, pathname)
