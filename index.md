## both python 2 and python 3 in the same project

Use dictionary and metaclass styles from both in the same project. Mix and match your styles in both python 2 and 3 environments.  

```python
from __both__ import py2

stuff = {
    'a' : 123
}

stuff.keys() + ['z']
stuff.viewkeys() | {'z'}


class Form(BaseForm):
    __metaclass__ = FormType
    pass
```

```python
from __both__ import py3

stuff = {
    'a' : 123
}

stuff.keys() | {'z'}

class Form(BaseForm, metaclass=FormType):
    pass
```


## add your own fixes

Add your own list of fixes. Or use your custom fixes instead!  You can run any lib2to3 fixes before importing. These fixes will not be run when in the given python version.  

```python
from __both__.py2 import fixes

# fixes to run when not in py2
import __fixes__.lib2to3.fixes.fix_tuple_params

lambda (x, y): x + y
```

```python
# combine default fixes with others
from __both__ import py3
from __both__.py3 import fixes

# extra fixes to run when not in py3
import __fixes__.libpasteurize.fixes.fix_unpacking

a, *b, c = range(100)
```

```python
# run all fixes in all pythons
from __both__ import fixes

# any lib2to3 fixer can be used
import __fixes__.my.custom.fix.here
```
