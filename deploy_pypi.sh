#!/bin/bash
rm -rf dist
python setup.py sdist
cd dist
twine upload -r pypi *.tar.gz
cd ..
