# MyBlog — Django Blog Website

## Setup Instructions

### Step 1 — Install Django
```
pip install -r requirements.txt
```

### Step 2 — Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Step 3 — Create Admin User
```
python manage.py createsuperuser
```

### Step 4 — Run Server
```
python manage.py runserver
```

### Step 5 — Open in Browser
- Homepage:   http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Register:   http://127.0.0.1:8000/register/
- Login:      http://127.0.0.1:8000/login/

## Features
- User Registration & Login
- Create, Edit, Delete Blog Posts
- Comment System
- Like / Unlike Posts
- Django Admin Panel
- Responsive Bootstrap Design
