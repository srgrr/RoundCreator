from setuptools import setup, Extension, find_packages

setup(
  name = 'RoundCreator',
  packages = ['RoundCreator'],
  version = '1.2.1',
  description = 'A tool that creates a programming contest folder structure',
  long_description=open('README.md', 'r').read(),
  author = 'Sergio Rodriguez Guasch',
  author_email = 'sergio.r.g@yandex.com',
  classifiers= [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: C++',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.0',
    'Topic :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development',
    'Topic :: Utilities'
  ],
  entry_points = {
    'console_scripts': [
      'RoundCreator=RoundCreator.RoundCreator:main'
    ]
  },
  url = 'https://github.com/srgrr/RoundCreator'
)
