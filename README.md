# Django Portfolio Website

A responsive portfolio website built with Django and Bootstrap 5.

## Features

- Responsive Bootstrap design
- Home, About, Skills, Projects and Contact sections
- Database-driven projects
- Django admin dashboard for managing projects
- Project images
- Project detail pages
- Contact form stored in SQLite
- GitHub and live-demo links
- WhiteNoise static-file support
- Ready for Render deployment

## 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 2. Install packages

```powershell
pip install -r requirements.txt
```

## 3. Create the database

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 4. Create your admin account

```powershell
python manage.py createsuperuser
```

Enter your username, email and password.

## 5. Start the website

```powershell
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

## 6. Add your projects

Login to `/admin/`, choose **Projects**, and add:

- Title
- Slug
- Description
- Technologies
- Project image
- GitHub URL
- Live URL
- Featured status

Suggested projects from your work:

- Weather App
- Memory Game
- Rock Paper Scissors
- Student Result System
- AI Blog

## Render deployment

Build command:

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
```

Start command:

```bash
gunicorn portfolio.wsgi:application
```

Set these environment variables in Render:

```text
SECRET_KEY=your-long-random-secret
DEBUG=False
ALLOWED_HOSTS=your-service.onrender.com
CSRF_TRUSTED_ORIGINS=https://your-service.onrender.com
```

For production image uploads, use persistent/object storage rather than relying on an ephemeral server filesystem.
