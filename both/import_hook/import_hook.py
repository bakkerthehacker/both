# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

if sys.version_info[0] <= 2:
    from .hook_py3 import hook
else:
    from .hook_py2 import hook


def add_api_hook():
    if hook not in sys.meta_path:
        # sys.meta_path.insert(0, hook)
        sys.meta_path = [hook] + sys.meta_path
