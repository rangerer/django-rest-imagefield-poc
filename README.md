# Django REST Framework - ImageField Test

Proof of Concept on how to expose the URI from an `models.ImageField` fields via Django REST Framework

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

### API

    python manage.py runserver

Visit http://localhost:8000/api/