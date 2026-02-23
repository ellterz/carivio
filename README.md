# 🚗 Carivio

Carivio is a Django-based web application for managing cars, tracking maintenance history, and organizing parts inventory.

It is designed for car owners and small garages who want a simple and structured way to store vehicle information, maintenance records, and compatible parts — all in one unified system.

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

- **cars** – Manages vehicles, manufacturers, and categories
- **maintenance** – Handles maintenance records for cars
- **parts** – Manages parts inventory and compatibility
- **common** – Contains shared templates and home page
- **carivio** – Main project configuration

---

## 🚘 Features

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

---

## 🧱 Tech Stack

- Python
- Django
- PostgreSQL
- Bootstrap 5
- HTML / CSS
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

### 5️⃣ Run Development Server

```bash
python manage.py runserver
```

---

## 🧪 Sample Data (Optional)

To test the project quickly:

1. Add cars
2. Create manufacturers
3. Create categories
4. Add maintenance records
5. Add parts and assign them to cars


---

## 📂 Project Structure

```
carivio/
│
├── carivio/          # Main project configuration
├── cars/             # Cars app
├── maintenance/      # Maintenance app
├── parts/            # Parts app
├── common/           # Shared templates
├── static/           # CSS & image
├── templates/        # HTML templates
├── requirements.txt
└── README.md
```

