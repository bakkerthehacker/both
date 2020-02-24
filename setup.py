# -*- coding: utf-8 -*-
import distutils
import os.path

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install as setuptools_install


# PTH = """
# try:
#     import both
# except ImportError as e:
#     print(e)
#     pass
# else:
#     both.register()
# """

PTH = """
import both
both.register()
"""


class install(setuptools_install):

    def initialize_options(self):
        setuptools_install.initialize_options(self)

        contents = 'import sys; exec({!r})\n'.format(PTH)
        self.extra_path = (self.distribution.metadata.name, contents)

    def finalize_options(self):
        setuptools_install.finalize_options(self)

        install_suffix = os.path.relpath(
            self.install_lib, self.install_libbase,
        )
        if install_suffix == '.':
            distutils.log.info('skipping install of .pth during easy-install')
        elif install_suffix == self.extra_path[1]:
            self.install_lib = self.install_libbase
            distutils.log.info(
                "will install .pth to '%s.pth'",
                os.path.join(self.install_lib, self.extra_path[0]),
            )
        else:
            raise AssertionError(
                'unexpected install_suffix',
                self.install_lib, self.install_libbase, install_suffix,
            )


setup(
    name='both',
    version='0.0.1',
    author='Grant Bakker',
    author_email='grant@bakker.pw',
    description='Python compatibility layer',
    url='https://bakkerthehacker.github.io/both/',
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ),
    packages=find_packages(),
    cmdclass={'install': install},
    install_requires=[
        'future',
    ],
)
