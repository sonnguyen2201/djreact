<<<<<<< HEAD
release: pipenv install
=======
>>>>>>> bdc0c8c0a18878dff8d1358e7b686364b8e1fbe1
release: pipenv run python manage.py makemigrations
release: pipenv run python manage.py migrate
web: gunicorn djreact.wsgi --log-file -