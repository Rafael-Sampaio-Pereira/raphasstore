flake8 $(git diff --relative --name-only origin/develop | grep .py)

coverage run manage.py test -v 2 && coverage report && coverage html
python -m coverage run ./manage.py test

isort .

