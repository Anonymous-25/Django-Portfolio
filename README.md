<img width="1592" height="738" alt="image" src="https://github.com/user-attachments/assets/53bd85b7-8d40-43e3-af64-157929a21e34" />

# 🚀 Django Portfolio CMS

A fully dynamic personal portfolio CMS built with **Django**. 
Easily manage your profile, skills, projects, and articles through the admin panel—no hardcoding required.

---

## 🎨 UI & Design
* **🧛 Dracula Theme:** Inspired color palette for a sleek, dark aesthetic.
* **🧾 vCard Style:** Modern vCard-style portfolio layout.
* **📱 Responsive:** Fully mobile-friendly UI.
* **✨ Glassmorphism:** Features smooth animations and glassmorphic elements.

## ⚡ Features
* **Dynamic Content:** Entirely database-driven (no static content).
* **Admin-Controlled:** Full management via Django Admin.
* **Modular Sections:** Dedicated modules for Skills, Experience, and Education.
* **Project Portfolio:** Includes categories and dynamic filtering.
* **Blog/Articles System:** Integrated writing platform.
* **Onboarding Logic:** Smart detection—if the database is empty, a welcome/setup guide is displayed; otherwise, the main portfolio loads.

---

## 📦 Installation Guide

### 1. Clone Repository
```bash
git clone https://github.com/Anonymous-25/Django-Portfolio.git
cd Django-Portfolio
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```
Visit: `http://127.0.0.1:8000/`

---

## 🔐 Admin Panel
Access the backend at: `http://127.0.0.1:8000/admin/`

### 🧩 Recommended Setup Order
To ensure the UI renders correctly, add data in this order:
1.  **Profile** (Crucial for the header)
2.  **Skills**
3.  **Experience / Education**
4.  **Projects**
5.  **Articles**
6.  **Social Links**

---

## 🧠 Smart Rendering Logic
The app uses `.exists()` checks in the views to determine the state of the application:
* **Empty DB:** Renders `onboarding.html` (Setup Guide).
* **Populated DB:** Renders `index.html` (Main UI).

---

## 🛠 Tech Stack
* **Backend:** Django
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (Default)

## 📌 Important Notes
Ensure your `.gitignore` includes the following to avoid pushing sensitive or bulky data:
```text
__pycache__/
*.pyc
db.sqlite3
.env
venv/
media/
```

---

## 🎯 Future Improvements
* [ ] **REST API:** Integration with Django REST Framework.
* [ ] **Multi-user:** Support for multiple user accounts.
* [ ] **Markdown:** Support for Markdown in the blog editor.
* [ ] **Analytics:** Dashboard to track project views.

## 👨‍💻 Author
**Anonymous-25** [GitHub Profile](https://github.com/Anonymous-25)

## ⭐ Support
If you find this project useful, please consider giving it a **star**! ⭐
