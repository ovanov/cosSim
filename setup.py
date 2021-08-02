from distutils.core import setup
from setuptools import find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'cosSim',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'This CLI tool compares files or directories with cosine similarity.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'ovanov',
  author_email = 'ovanov@protonmail.com',
  url = 'https://github.com/ovanov/cosSim',
  keywords = ['cosine Similarity', 'file comparison', 'nltk', 'CLI programm', 'vectorisation'],
  platforms='any',
  install_requires=[
          'nltk>=3.6.2',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  python_requires=">=3.6",
  entry_points={
    'console_scripts': [
      'cosSim=cosSim.cli:main'
    ]
  }
)