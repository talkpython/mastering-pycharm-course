import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read_readme(filename):
    try:
        filename = os.path.join(os.path.dirname(__file__), filename)
        text_type = type(u"")
        with io.open(filename, mode="r", encoding='utf-8') as fd:
            return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())
    except:
        return ''


def read_version():
    try:
        filename = os.path.join(os.path.dirname(__file__), 'jinja_partials', '__init__.py')
        with open(filename, mode="r", encoding='utf-8') as fin2:
            for line in fin2:
                if line and line.strip() and line.startswith('__version__'):
                    return line.split('=')[1].strip().strip("'").strip('"')

        return "0.0.0.0"
    except:
        return "0.0.0.0"


setup(
    name="jinja_partials",
    version=read_version(),
    url="https://github.com/mikeckennedy/jinja_partials",
    license='MIT',

    author="Michael Kennedy",
    author_email="michael@talkpython.fm",

    description="Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks.",
    long_description=read_readme("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests', 'example', 'readme_resources', 'build', 'dist',)),

    install_requires=['jinja2'],
    exclude=['build', 'dist', '.github', 'example', 'tests'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
