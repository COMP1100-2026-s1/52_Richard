# Running SkillPath Locally

## Prerequisites

- Python 3.x installed
- Project cloned/downloaded to your machine

---

## 1. Navigate to the Project Root

Open a terminal and `cd` into the project folder:

```powershell
cd path\to\52_Richard
```

---

## 2. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

> If you get an execution policy error, run this first:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
> ```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux (Terminal):**
```bash
source .venv/bin/activate
```

Once activated, your terminal prompt will show `(.venv)`.

---

## 3. Install Dependencies

Install all required packages from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

---

## 4. Apply Migrations

Run this whenever you pull new changes or add new models:

```powershell
python manage.py migrate
```

---

## 5. Start the Development Server

```powershell
python manage.py runserver
```

The app will be available at: http://127.0.0.1:8000

The Django admin panel is at: http://127.0.0.1:8000/admin

---

## 6. Stop the Server

Press `Ctrl + C` in the terminal.

---

## 7. Deactivate the Virtual Environment

When you are done:

```powershell
deactivate
```

---

## Quick Reference

| Task                     | Command (Windows)                    | Command (macOS/Linux)              |
|--------------------------|--------------------------------------|------------------------------------|
| Activate environment     | `.venv\Scripts\Activate.ps1`         | `source .venv/bin/activate`        |
| Install dependencies     | `pip install -r requirements.txt`    | `pip install -r requirements.txt`  |
| Apply migrations         | `python manage.py migrate`           | `python manage.py migrate`         |
| Create new migrations    | `python manage.py makemigrations`    | `python manage.py makemigrations`  |
| Start server             | `python manage.py runserver`         | `python manage.py runserver`       |
| Create admin superuser   | `python manage.py createsuperuser`   | `python manage.py createsuperuser` |
| Run tests                | `python manage.py test`              | `python manage.py test`            |
| Deactivate environment   | `deactivate`                         | `deactivate`                       |

---

## Project Structure

```
52_Richard/
├── skillpath_project/   # Project config (settings, URLs, wsgi/asgi)
├── SkillPath/           # Main app (models, views, admin, tests)
├── manage.py            # Django management commands
├── db.sqlite3           # SQLite database
└── .venv/               # Python virtual environment
```
