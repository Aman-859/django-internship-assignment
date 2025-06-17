
# Django Internship Assignment

A Django backend project demonstrating API development, user authentication, Celery integration, and Telegram Bot interaction — built using Django REST Framework.

---

## 📁 Features

- ✅ Django REST Framework (DRF)
- 🔐 Token/JWT-based Authentication
- 🌐 Web-based Login and Protected Views
- ✉️ Celery with Redis for background email tasks
- 🤖 Telegram Bot to store username and chat ID on `/start`
- 📦 Environment variable support using `python-decouple`

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Aman-859/django-internship-assignment.git
cd django-internship-assignment
```

### 2. Create Virtual Environment & Install Dependencies
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file:
```bash
cp .env.example .env
```

Then fill in your actual credentials.

### 4. Run Migrations & Create Superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start Redis Server (for Celery)
```bash
# Linux/Mac
redis-server
# Windows (use Redis Desktop or install via WSL/Chocolatey)
```

### 6. Start Celery Worker
```bash
celery -A your_project_name worker -l info
```

Replace `your_project_name` with the actual Django project directory (e.g., `myproject`).

### 7. Start the Django Server
```bash
python manage.py runserver
```

---

## 🔐 Authentication

- **Web-based** login (`/login/`, `/logout/`)
- **DRF Token Auth** or **JWT Auth** for API access
- Protected view: `/private-api/`
- Public view: `/public-api/`

---

## 🤖 Telegram Bot Setup

1. Start a conversation with your bot: [**@coolamanbot**](https://t.me/coolamanbot)
2. Send `/start` to the bot — your Telegram username and ID will be stored in the database.
3. The bot will reply to confirm successful registration.
4. Add your Telegram bot token to `.env`:
   ```env
   Token=your_telegram_bot_token
   ```
5. Set webhook to your endpoint (e.g., using `ngrok` during local dev):
   ```
   https://api.telegram.org/bot<Your_Token>/setWebhook?url=https://yourdomain.com/telegram-webhook/
   ```

---

## 📄 API Documentation (Sample)

### 🔓 Public API
```http
GET /public-api/
```
Response:
```json
{
  "message": "This Is Public Api !"
}
```

### 🔐 Private API (Token Required)
```http
GET /private-api/
Authorization: Token your_token_here
```
Response:
```json
{
  "message": "Welcome username, you are in private api !"
}
```

---

## 🔐 Environment Variables Used

| Variable Name         | Purpose                            |
|-----------------------|-------------------------------------|
| `SECRET_KEY`          | Django secret key                   |
| `DEBUG`               | Production mode (should be False)   |
| `Token`               | Telegram Bot token                  |
| `DB_NAME`             | Database name                       |
| `DB_USER`             | Database user                       |
| `DB_PASSWORD`         | Database password                   |
| `EMAIL_HOST`          | Email server                        |
| `EMAIL_HOST_USER`     | Email sender                        |
| `EMAIL_HOST_PASSWORD` | Email password                      |

---

## 🧑‍💻 Author

**Aman Mishra**  
[GitHub](https://github.com/Aman-859)

---

## 📌 Notes

- Keep your `.env` private (never upload it to GitHub).
- Ensure Redis is running before using Celery tasks.
- You can deploy using services like Heroku, Railway, or Render, though not required for this task.

---

## ✅ Checklist

- [x] Clean & working Django project
- [x] DRF API with public & protected endpoints
- [x] Celery with Redis to send email
- [x] Telegram bot integration with webhook
- [x] Environment variables support
- [x] `.env.example` included
- [x] Detailed README.md
