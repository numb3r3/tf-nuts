from os import path

from setuptools import setup, find_packages

try:
    pkg_name = 'tf_nuts'
    libinfo_py = path.join(pkg_name, '__init__.py')
    libinfo_content = open(libinfo_py, 'r', encoding='utf8').readlines()
    version_line = [l.strip() for l in libinfo_content if l.startswith('__version__')][0]
    exec(version_line)  # produce __version__
except FileNotFoundError:
    __version__ = '0.0.0'

base_dep = [
    'numpy',
    'termcolor',
    'ruamel.yaml',
    'GPUtil'
]


setup(
    name=pkg_name,
    packages=find_packages(),
    version=__version__,
    include_package_data=True,
    description='',
    author='numb3r3',
    author_email='wangfelix87@gmail.com',
    install_requires=base_dep,
    setup_requires=[
        'setuptools>=18.0',
        'pytest-runner',
    ],
    tests_require=["pytest"],
)
