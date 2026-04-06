# 🚗 Carivio

Carivio is a Django-based web application for managing cars, tracking maintenance history, and organizing parts inventory.

It is designed for car owners and small garages who want a simple and structured way to store vehicle information, maintenance records, and compatible parts — all in one unified system.

---

## 🌐 Live Demo

The application is deployed and accessible at:

**https://carivio2026-f3huawccggh7dgc5.swedencentral-01.azurewebsites.net**


---

## 📌 Project Overview

Carivio allows users to:

- Manage vehicle information
- Track maintenance records and costs
- Organize parts inventory
- Link cars, maintenance, and parts together


---

## 🧩 Applications Structure

The project is organized into multiple Django apps:

- **accounts** – User registration, login, logout, profile management and groups
- **cars** – Manages vehicles, manufacturers, and categories
- **maintenance** – Handles maintenance records for cars
- **parts** – Manages parts inventory and compatibility
- **api** – RESTful API endpoints using Django REST Framework
- **common** – Contains shared templates and home page
- **carivio** – Main project configuration

---

## 🚘 Features

### Accounts
- User registration, login and logout
- Extended user model with bio and avatar
- Profile page with edit functionality
- Two user groups: Garage Owner and Mechanic
- Async welcome task via Celery on registration


### Cars
- Add, edit, delete, and view cars
- Store:
  - Vehicle model
  - Manufacturer
  - Year (validated)
  - VIN (validated and unique)
  - Categories (Many-to-Many relationship)
- Automatically calculate car age
- Calculate total maintenance cost per vehicle
- Custom template tags for car age display

### Manufacturers
- Add manufacturers
- Linked to cars (ForeignKey relationship)

### Categories
- Add vehicle categories
- Assign multiple categories to each car

### 🛠 Maintenance
- Add maintenance records per car
- Track:
  - Date
  - Description
  - Cost
- View, edit, and delete records
- Connected to cars via ForeignKey relationship

### ⚙ Parts
- Add, edit, delete, and view parts
- Store:
  - Part name
  - Manufacturer
  - Price (validated)
- Assign parts to compatible vehicles (Many-to-Many relationship)

### 🔌 REST API
- Car list and detail endpoints
- Maintenance and parts endpoints
- Custom permissions (IsOwnerOrReadOnly)
- DRF browsable API at `/api/`

### ⚡ Async Processing
- Celery task queue with Redis broker
- Welcome email task on user registration
- django-celery-results for task tracking

---

## 🧱 Tech Stack

- Python 3.12
- Django 6.0.1
- Django REST Framework
- Celery + Redis
- PostgreSQL
- Bootstrap 5
- HTML / CSS
- Whitenoise
- Gunicorn
- python-dotenv

---

## 🗄 Database Configuration

Carivio uses PostgreSQL as its database.

Environment variables are used for database credentials.

Example `.env` file:

```
SECRET_KEY=your-secret-key-here
DB_NAME=carivio_db
DB_USER=your_user
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://localhost:6379/0
```

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ellterz/carivio.git
cd carivio
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Mac/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run Redis (required for Celery)
```bash
brew services start redis  # Mac
```

---

### 6️⃣ Run Celery Worker (in a separate terminal)
```bash
celery -A carivio worker --loglevel=info
```

---

### 7️⃣ Run Development Server
```bash
python manage.py runserver
```

---

## 🧪 Running Tests
```bash
python manage.py test
```
---

## 📂 Project Structure

```
carivio/
│
├── carivio/          # Main project configuration + Celery
├── accounts/         # User auth, profile, groups, tasks
├── cars/             # Cars app
├── maintenance/      # Maintenance app
├── parts/            # Parts app
├── api/              # DRF REST API
├── common/           # Shared templates and error pages
├── static/           # CSS & image
├── templates/        # HTML templates
├── requirements.txt
└── README.md
```
---

## 🔌 API Endpoints

| Endpoint | Method | Auth Required |
|----------|--------|---------------|
| `/api/cars/` | GET | No |
| `/api/cars/<id>/` | GET | No |
| `/api/maintenance/` | GET | Yes |
| `/api/parts/` | GET | Yes |

