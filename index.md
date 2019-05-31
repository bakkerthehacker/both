## both python 2 and python 3 in the same project

Use dictionary and metaclass styles from both in the same project:

```python
from __both__ import py2

stuff = {
    'a' : 123
}

stuff.keys() + ['z']
stuff.viewkeys() | {'z'}
```

```python
from __both__ import py3

stuff = {
    'a' : 123
}

stuff.keys() | {'z'}
```
