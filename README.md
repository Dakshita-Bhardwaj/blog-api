# Blog API

A Django REST Framework blog backend featuring JWT authentication, authorization, and CRUD operations for blog posts.

## Features

* User Registration
* User Login
* JWT Authentication (Access & Refresh Tokens)
* Create Blog Posts
* View All Blog Posts
* View Single Blog Post
* Update Blog Posts
* Delete Blog Posts
* Ownership-Based Authorization

## Tech Stack

* Python 3.12
* Django
* Django REST Framework
* SimpleJWT
* SQLite

## API Endpoints

### Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /api/register/ |
| POST   | /api/login/    |

### Posts

| Method | Endpoint                |
| ------ | ----------------------- |
| GET    | /api/posts/             |
| GET    | /api/posts/<id>/        |
| POST   | /api/posts/create/      |
| PUT    | /api/posts/<id>/update/ |
| DELETE | /api/posts/<id>/delete/ |

## Example Request

POST /api/posts/create/

```json
{
  "title": "My First Blog",
  "content": "Backend is finally making sense."
}
```

## Example Response

```json
{
  "id": 1,
  "title": "My First Blog",
  "content": "Backend is finally making sense.",
  "author": "dakshita"
}
```

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
