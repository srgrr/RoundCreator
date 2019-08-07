#!/bin/bash
python3 TestRoundCreator/TestMain.py
if [ "$?" = "0" ]; then
	rm -rf dist
	python setup.py sdist
	cd dist
	twine upload -r pypi *.tar.gz
	cd ..
else
  echo "Skipping deployment"
fi
