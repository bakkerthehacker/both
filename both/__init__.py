# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from both.import_hook.import_hook import add_api_hook


def register():
    add_api_hook()
