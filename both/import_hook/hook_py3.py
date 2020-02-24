# -*- coding: utf-8 -*-
import imp
import re
from lib2to3.refactor import RefactoringTool
from mmap import ACCESS_READ
from mmap import mmap
from os.path import join

import libpasteurize.fixes

pasteurize_fixes = libpasteurize.fixes.fix_names

pasteurize_tool = RefactoringTool(pasteurize_fixes)

pasteurize_regex = re.compile(r'(?m)^[ \t\f]*#.*?'
                              r'python[ \t]+version'
                              r'[:=][ \t]*3')


class BothPython3FinderLoader(object):
    def find_module(self, fullname, path=None):
        parent = None
        name = fullname
        if '.' in fullname:
            parent, name = fullname.rsplit('.', 1)
            if path is None:
                loader = imp.find_module(parent, path)
                mod = loader.load_module(parent)
                path = mod.__path__

        if imp.is_builtin(name) or imp.is_frozen(name):
            return

        try:
            self.found_module = imp.find_module(name, path)
            (self.file, self.path, (self.suffix, self.mode,
                                    self.type)) = self.found_module
        except Exception:
            return

        print(fullname)

        if self.type in {
                imp.PY_COMPILED, imp.C_EXTENSION, imp.C_BUILTIN, imp.PY_FROZEN
        }:
            return

        return self

        if self.type == imp.PKG_DIRECTORY:
            self.pathname = join(self.path, '__init__.py')
        elif self.type == imp.PY_SOURCE:
            self.pathname = self.path

        if not self.file:
            self.file = open(self.pathname, 'U')

        try:
            self.mmap_file = mmap(self.file.fileno(), 0, access=ACCESS_READ)
            if pasteurize_regex.search(self.mmap_file):
                print('FOUND FOR {}'.format(self.pathname))
                return self
        except ValueError:
            # empty file
            return
        finally:
            self.mmap_file.close()

    def load_module(self, fullname):
        return imp.load_module(fullname, *self.found_module)

    #     try:
    #         if fullname not in sys.modules:
    #
    #             ##################################################
    #             code = self.get_code(fullname)
    #             mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
    #             # mod.__file__ = "<%s>" % self.__class__.__name__
    #             mod.__file__ = self.pathname
    #             mod.__loader__ = self
    #             if self.type == imp.PKG_DIRECTORY:
    #                 mod.__path__ = []
    #                 mod.__package__ = fullname
    #             else:
    #                 mod.__package__ = fullname.rpartition('.')[0]
    #             exec(code, mod.__dict__)
    #         return sys.modules[fullname]
    #     except Exception:
    #         if fullname in sys.modules:
    #             del sys.modules[fullname]
    #         raise
    #     finally:
    #         pass
    #         # TODO close the file
    #
    # def load_module_future(self, fullname):
    #     print('LOAD MODULE')
    #     print('{}'.format(fullname))
    #
    #     try:
    #         if fullname in sys.modules:
    #             return sys.modules[fullname]
    #         else:
    #             mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
    #             mod.__file__ = self.pathname
    #             mod.__loader__ = self
    #             if self.type == imp.PKG_DIRECTORY:
    #                 mod.__path__ = []
    #                 mod.__package__ = fullname
    #             else:
    #                 mod.__package__ = fullname.rpartition('.')[0]
    #
    #             # TODO add stuff here to get code
    #             exec(code, mod.__dict__)
    #
    #             cachename = imp.cache_from_source(self.pathname)
    #             if not os.path.exists(cachename):
    #                 update_cache = True
    #             else:
    #                 sourcetime = os.stat(self.pathname).st_mtime
    #                 cachetime = os.stat(cachename).st_mtime
    #                 update_cache = cachetime < sourcetime
    #             # # Force update_cache to work around a problem with it being treated as Py3 code???
    #             # update_cache = True
    #             # if not update_cache:
    #             #     with open(cachename, 'rb') as f:
    #             #         data = f.read()
    #             #         try:
    #             #             code = marshal.loads(data)
    #             #         except Exception:
    #             #             # pyc could be corrupt. Regenerate it
    #             #             update_cache = True
    #             # if update_cache:
    #             #     if self.found[0]:
    #             #         source = self.found[0].read()
    #             #     elif self.type == imp.PKG_DIRECTORY:
    #             #         with open(self.pathname) as f:
    #             #             source = f.read()
    #             #
    #             #     if detect_python2(source, self.pathname):
    #             #         source = self.transform(source)
    #             #         with open('/tmp/futurized_code.py', 'w') as f:
    #             #             f.write('### Futurized code (from %s)\n%s' %
    #             #                     (self.pathname, source))
    #             #
    #             #     code = compile(source, self.pathname, 'exec')
    #             #
    #             #     dirname = os.path.dirname(cachename)
    #             #     try:
    #             #         if not os.path.exists(dirname):
    #             #             os.makedirs(dirname)
    #             #         with open(cachename, 'wb') as f:
    #             #             data = marshal.dumps(code)
    #             #             f.write(data)
    #             #     except Exception:   # could be write-protected
    #             #         pass
    #             # exec(code, mod.__dict__)
    #     except Exception:
    #         del sys.modules[fullname]
    #         raise
    #     finally:
    #         pass


hook = BothPython3FinderLoader()
