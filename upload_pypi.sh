#!/usr/bin/expect -f
spawn twine upload -r pypi dist/*.tar.gz
expect "Enter your username:"
send "$env(PYPI_USER)\n"
expect "Enter your password:"
send "$env(PYPI_PASSWORD)\n"
interact
