# 🌸 Ayol Uchun Clone Project

[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![Django](https://img.shields.io/badge/django-4.2+-green)]()
[![DRF](https://img.shields.io/badge/drf-3.x-red)]()
[![PostgreSQL](https://img.shields.io/badge/postgresql-15+-blue)]()

A fully featured **Ayol Uchun clone project** deployed under the domain `your-domain-here.com`.  
This platform provides **course management, payment integration, and live event features** using modern Django tooling.

---

## ✨ Key Features

### Core Functionality
- **JWT-based authentication** with email verification for user activation  
- **Users can buy courses and pay for them (real payment integration)**  
- Built with **Django REST Framework** and lightweight **HTML/CSS styling**  
- **Jazzmin** for a clean, modern admin interface  
- **Celery + custom signals** for background tasks and notifications  
- Organized into modular apps: `users`, `payment`, `news`, `courses`, and `common`  

### User Interaction
- Organize **live events**  
- Conduct **surveys within courses**  
- Allow **users to write posts**  
- Course **comments and ratings system**  

---

## 🛠 Tech Stack

- **Backend:** Django 4.2+, Django REST Framework  
- **Database:** PostgreSQL  
- **Authentication:** JWT + email activation  
- **Admin Panel:** Jazzmin  
- **Task Queue:** Celery  
- **Package Management:** `uv` / `ruff` instead of pip  

---

## 🚀 Getting Started

### 1. Install dependencies using uv/ruff (first, you should install uv if you have never used it before)

```bash
uv sync
```

### 2. Activate the virtual environment  
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

### 3. Run database migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```
