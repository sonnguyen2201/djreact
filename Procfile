release: pipenv install
release: pipenv run python manage.py makemigrations
release: pipenv run python manage.py migrate
web: gunicorn djreact.wsgi --log-file -