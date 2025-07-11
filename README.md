# SecureAuth

SecureAuth is a secure, modern authentication system built with Django. It helps developers integrate user login, registration, and session management into web applications quickly and safely.

---

## 🚀 Project Purpose

In many projects, authentication is either too basic or overly complex. SecureAuth aims to provide a simple yet robust authentication framework that:

- Follows security best practices (password hashing, session management)
- Is easy to set up and integrate
- Provides clean, customizable UI components



---

## 🛠 Tech Stack

- Backend: Django (Python)
- Database: SQLite (development) / PostgreSQL (production ready)
- Frontend: HTML, CSS, Bootstrap
- Authentication: Django auth system, sessions
- Optional: Django Rest Framework (for API-based apps)

---

## 💻 Installation & Local Setup

### Prerequisites

- Python 3.x
- pip
- Git

---

### Apply Database Migrations

We need to run Django migrations to create the necessary database tables:

```bash
python manage.py migrate
```

---

### Create a Superuser 

For accessing  the Django admin panel, we have created a superuser account:

```bash
python manage.py createsuperuser
```



---

### Start the Development Server

In order to run the development server,we have used this command :

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## ✅ Testing the Project

- Register a new user and test login and logout functionality.
- If you created a superuser, access the Django admin panel at:

  ```
  http://127.0.0.1:8000/admin/
  ```

- Check for proper form validation and error handling.
- Run automated tests (if included) with:

  ```bash
  python manage.py test
  ```

---

## ✅ Features

- User registration
- Secure login & logout
- Password hashing
- Session management
- Simple Bootstrap-based UI
- Easily extendable for:
  - Email verification
  - Social login integrations

---




