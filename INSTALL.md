# Installation

This guide explains how to set up and run Django Portfolio locally.

## Requirements

* Python 3.10+
* Git
* Virtual Environment (`venv`)
* SQLite (included with Python)

---

## 1. Clone Repository

```bash
git clone https://github.com/Anonymous-25/Django-Portfolio.git
cd Django-Portfolio
```

---

## 2. Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv portfolio-env
source portfolio-env/bin/activate
```

### Windows

```powershell
python -m venv portfolio-env
portfolio-env\Scripts\activate
```

---

## 3. Install Dependencies

Upgrade pip first:

```bash
python -m pip install --upgrade pip
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 4. Database Setup

Apply migrations:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

---

## 5. Run Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

## 6. Collect Static Files

For production deployments:

```bash
python manage.py collectstatic
```

---

## 7. Configuration

Update settings before production deployment:

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Configure email settings if required
* Configure static and media paths
* Set a secure `SECRET_KEY`

---

## 8. PythonAnywhere Deployment

Create a virtual environment:

```bash
mkvirtualenv --python=/usr/bin/python3.10 portfolio-env
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Collect static files:

```bash
python manage.py collectstatic --noinput
```

Reload the web application from the PythonAnywhere dashboard.

---

## Updating

Pull latest changes:

```bash
git pull origin main
```

Install new dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Collect static files:

```bash
python manage.py collectstatic --noinput
```

---

## Troubleshooting

### Migration Issues

```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading

```bash
python manage.py collectstatic --clear
python manage.py collectstatic
```

### Check Django Configuration

```bash
python manage.py check
```

---

## License

See the LICENSE file included with this repository.
