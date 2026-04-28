<img width="1592" height="738" alt="image" src="https://github.com/user-attachments/assets/53bd85b7-8d40-43e3-af64-157929a21e34" />

# 🚀 Django Portfolio CMS

A fully dynamic personal portfolio CMS built with Django.
Easily manage your profile, skills, projects, and articles through the admin panel — no hardcoding required.

🎨 UI & Design
🧛 Dracula Theme inspired color palette
🧾 vCard-style portfolio layout
📱 Fully responsive modern UI
✨ Glassmorphism + smooth animations
⚡ Features
Dynamic portfolio (no static content)
Admin-controlled data (Django Admin)
Skills, Experience, Education modules
Project portfolio with categories & filters
Blog / Articles system
Social links grid
Contact form
Smart onboarding (auto welcome page if DB is empty)
🧠 Smart Rendering Logic
If no data in database → shows onboarding guide page
If any data exists → loads main portfolio UI

Handled efficiently using .exists() in views.

📦 Installation Guide
1. Clone Repository
git clone https://github.com/Anonymous-25/Django-Portfolio.git
cd Django-Portfolio
2. Create Virtual Environment
python -m venv venv

Activate:

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Setup Database
python manage.py migrate
5. Create Admin User
python manage.py createsuperuser
6. Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/
🔐 Admin Panel

Access:

http://127.0.0.1:8000/admin/

Login using your superuser credentials.

🧩 How to Use

Add data in this recommended order:

Profile (important)
Skills
Experience
Education
Projects
Articles
Social Links

👉 Once any data is added, the main UI will automatically appear.

📁 Project Structure
models.py → Database models
views.py → Rendering logic
templates/ → UI templates
static/ → CSS, JS, assets
🛠 Tech Stack
Backend: Django
Frontend: HTML, CSS, JS
Database: SQLite (default)
📌 .gitignore (important)

Make sure you don’t push unnecessary files:

__pycache__/
*.pyc
db.sqlite3
.env
venv/
media/
🎯 Future Improvements
REST API (Django REST Framework)
Multi-user portfolio system
Theme switcher (dark/light)
Markdown blog editor
Analytics dashboard
🎨 Credits
Dracula color palette inspiration
vCard-style portfolio UI inspiration from GitHub community

Special thanks to the open-source community for design inspiration.

👨‍💻 Author

Anonymous-25

⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub.Yeah, that shouldn’t happen — and you’re right to question it.

What you’re seeing (`id="xxxxx"` appearing outside or breaking the code block) is caused by the **writing block formatting system**, not actual Markdown. It injected metadata into places where it doesn’t belong, so the code block looks “broken.”

### ✅ Clean version (proper README — copy this)

```markdown
# 🎨 Django Portfolio CMS

A modern **Portfolio Content Management System (CMS)** built with **Django**, featuring a clean UI inspired by **vCard layouts** and styled using the **Dracula theme**.

This project allows you to manage your personal portfolio dynamically — including profile, skills, projects, articles, and more — all from the Django admin panel.

---

## 🚀 Features

- 🧑 Profile Management
- 💼 Experience & Education
- 🛠 Skills with progress bars
- 📂 Portfolio Projects with categories
- ✍️ Blog / Articles system
- 🔗 Social Links Grid
- 📬 Contact Form
- 🗺 Location Map Integration
- 🎨 Dracula-inspired modern UI
- ⚙️ Fully dynamic (No hardcoding required)

---

## 📁 Project Structure

```markdown
Django-Portfolio/
│
├── portfolio/
├── templates/
├── static/
├── db.sqlite3
├── manage.py
└── requirements.txt
```
---

## 🛠 Installation Guide

### 1. Clone Repo
```bash
git clone https://github.com/Anonymous-25/Django-Portfolio.git
cd Django-Portfolio
````

### 2. Create Virtual Env

```bash
python -m venv venv
```

Activate:

* Linux/Mac:

```bash
source venv/bin/activate
```

* Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Migrate DB

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Admin

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

---

## ⚙️ Usage

1. Go to `/admin/`
2. Add:

   * Profile
   * Skills
   * Experience
   * Projects
   * Articles

---

## 🧠 Smart Logic

* No data → shows **Welcome Guide Page**
* Any data exists → shows **Portfolio UI**

---

## 📌 Git Push

```bash
git add .
git commit -m "first commit"
git push origin main
```

Fix error:

```bash
git pull origin main --rebase
git push origin main
```

---

## 🎨 Credits

* Dracula Theme Community
* vCard UI inspiration

---

## 👨‍💻 Author

Anonymous-25
[https://github.com/Anonymous-25](https://github.com/Anonymous-25)

```

---

### 💡 What went wrong earlier?

- The system accidentally mixed **UI metadata (`id="..."`) into Markdown**
- That’s **not valid GitHub README syntax**
- It caused your code block to “leak”

---

If you want, I can next:
- :contentReference[oaicite:0]{index=0}  
- Or :contentReference[oaicite:1]{index=1} 🚀
```
Here’s a **clean, professional, GitHub-ready README.md** tailored for your project (with your logic, Dracula UI, onboarding system, etc.) 👇

---

# 🚀 Django Portfolio CMS

A fully dynamic **personal portfolio CMS** built with Django.
Easily manage your profile, skills, projects, and articles through the admin panel — no hardcoding required.

---

## 🎨 UI & Design

* 🧛 Dracula Theme inspired color palette
* 🧾 vCard-style portfolio layout
* 📱 Fully responsive modern UI
* ✨ Glassmorphism + smooth animations

---

## ⚡ Features

* Dynamic portfolio (no static content)
* Admin-controlled data (Django Admin)
* Skills, Experience, Education modules
* Project portfolio with categories & filters
* Blog / Articles system
* Social links grid
* Contact form
* Smart onboarding (auto welcome page if DB is empty)

---

## 🧠 Smart Rendering Logic

* If **no data in database** → shows onboarding guide page
* If **any data exists** → loads main portfolio UI

Handled efficiently using `.exists()` in views.

---

## 📦 Installation Guide

### 1. Clone Repository

```bash
git clone https://github.com/Anonymous-25/Django-Portfolio.git
cd Django-Portfolio
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Database

```bash
python manage.py migrate
```

---

### 5. Create Admin User

```bash
python manage.py createsuperuser
```

---

### 6. Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

Access:

```
http://127.0.0.1:8000/admin/
```

Login using your superuser credentials.

---

## 🧩 How to Use

Add data in this recommended order:

1. Profile (important)
2. Skills
3. Experience
4. Education
5. Projects
6. Articles
7. Social Links

👉 Once any data is added, the main UI will automatically appear.

---

## 📁 Project Structure

* `models.py` → Database models
* `views.py` → Rendering logic
* `templates/` → UI templates
* `static/` → CSS, JS, assets

---

## 🛠 Tech Stack

* Backend: Django
* Frontend: HTML, CSS, JS
* Database: SQLite (default)

---

## 📌 .gitignore (important)

Make sure you don’t push unnecessary files:

```
__pycache__/
*.pyc
db.sqlite3
.env
venv/
media/
```

---

## 🎯 Future Improvements

* REST API (Django REST Framework)
* Multi-user portfolio system
* Theme switcher (dark/light)
* Markdown blog editor
* Analytics dashboard

---

## 🎨 Credits

* Dracula color palette inspiration
* vCard-style portfolio UI inspiration from GitHub community

Special thanks to the open-source community for design inspiration.

---

## 👨‍💻 Author

Anonymous-25

---

## ⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub.

---
