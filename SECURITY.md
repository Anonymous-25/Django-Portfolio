# 🔐 Security Policy

## 📌 Supported Versions

This project is under active development. Security updates are currently applied to the latest version only.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ Yes             |
| Older   | ❌ No              |

---

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability, please **DO NOT open a public issue**.

Instead, follow these steps:

1. 📧 Email the maintainer directly  
2. Include a detailed description of the issue  
3. Provide steps to reproduce the vulnerability  
4. Attach screenshots or proof-of-concept if possible  

> This helps prevent exposing sensitive information publicly.

---

## ⏱ Response Time

- Initial response: **within 48 hours**
- Status update: **within 3–5 days**
- Fix timeline: depends on severity

---

## 🔒 Security Best Practices

If you are running this project locally or in production:

### Environment Variables
- Never commit secrets (API keys, passwords)
- Use a `.env` file
- Add `.env` to `.gitignore`

### Django Settings
- Set `DEBUG = False` in production
- Use a strong `SECRET_KEY`
- Configure `ALLOWED_HOSTS` properly

### Database
- Avoid using SQLite in production
- Use PostgreSQL or MySQL instead

### Dependencies
- Keep dependencies updated:
  ```bash
  pip install --upgrade -r requirements.txt
