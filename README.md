# 🥷 Warrior Dojo API

A FastAPI-powered backend for managing legendary warriors and their deadly skills.  
Built with authentication, full CRUD, and scalable structure — ready to deploy and slay.

---

## 🚀 Features

- 🔐 JWT Auth (Login/Register)
- 🧙 Full CRUD for Warriors
- 🗡 Role-based access (each user sees only their warriors)
- 🐍 FastAPI + SQLAlchemy
- 🧪 Built-in Swagger docs
- ☁️ Deploy-ready (Railway, Render, etc.)

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite (dev) / PostgreSQL (prod)
- JWT Auth
- Alembic for migrations

---

## 📂 Project Structure
warrior-dojo/
├── app/
│ ├── main.py # Entry point
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── auth.py # JWT logic
│ ├── routes/
│ │ └── warriors.py # Warrior routes
│ └── database.py # DB config
├── .env # Secrets (ignored)
├── requirements.txt
└── README.md


---

## ⚙️ Setup

```bash
git clone https://github.com/WISH-CODES/warrior-dojo.git
cd warrior-dojo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

##Add a .env file:

ini
Copy code
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./warrior.db

▶️ Run it
bash
Copy code
uvicorn app.main:app --reload
Swagger docs available at:
http://localhost:8000/docs

## TODO
✅ Auth system

✅ CRUD for Warriors

⏳ Unit tests

⏳ PostgreSQL for production

⏳ CI/CD setup

 License
MIT — use it, remix it, level up with it.

Made with ❤️ by @WISH-CODES

yaml
Copy code

---

### ✅ 3. Save, commit & push

```bash
git add README.md
git commit -m "📝 Added  README"
git push



