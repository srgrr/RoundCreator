#!/bin/bash
python3 setup.py install --user
python3 TestRoundCreator/TestMain.py
if [ "$?" = "0" ]; then
	rm -rf dist
	python3 setup.py sdist
	./upload_pypi.sh
	exit 0
else
  echo "Skipping deployment"
  exit 1
fi
