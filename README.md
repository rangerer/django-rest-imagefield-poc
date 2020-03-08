# Django REST Framework - URI test

Proof of Concept on how to expose URI fields via Django REST Framework

## Usage

    pipenv install --dev
    pipenv shell
    cd todos
    python manage.py migrate
    python manage.py runserver

### Django Admin

    python manage.py createsuperuser --username admin
    python manage.py runserver

Visit http://localhost:8000/admin/
