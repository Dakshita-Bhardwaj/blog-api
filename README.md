# Blog API

A Django REST Framework blog backend with JWT authentication.

## Features

- User Registration
- User Login
- JWT Authentication
- Create Blog Post
- Read Blog Posts
- Update Blog Posts
- Delete Blog Posts
- Ownership-based Authorization

## Tech Stack

- Python
- Django
- Django REST Framework
- SimpleJWT
- SQLite

## API Endpoints

### Authentication

POST /api/register/

POST /api/login/

### Posts

GET /api/posts/

POST /api/posts/create/

PUT /api/posts/<id>/

DELETE /api/posts/<id>/delete/

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```