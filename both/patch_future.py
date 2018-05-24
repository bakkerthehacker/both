# -*- coding: utf-8 -*-
import __future__

something = (
    'my_future'
)


def add_futures():
    for future_name in something:
        feature = __future__._Feature(None, None, None)  # TODO
        __future__.all_feature_names.append(future_name)
        __future__.__all__.append(future_name)
        setattr(__future__, future_name, feature)
