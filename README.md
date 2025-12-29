# 📝 Notes Taking API (FastAPI)

A secure and scalable **Notes Taking REST API** built using **Python & FastAPI**.  
This project provides user authentication, authorization, and full CRUD operations for notes.

---

## 🚀 Features

- 🔐 User Authentication & Authorization (JWT-based)
- 👤 User Registration & Login
- 📝 Create, Read, Update, Delete Notes
- 🔒 Notes are user-specific (ownership enforced)
- 🗂 Clean and scalable project structure
- ⚡ FastAPI with automatic API documentation
- 🧠 SQLAlchemy ORM
- 🛡 Password hashing using secure algorithms
- 📦 Ready for Dockerization & future scaling

---

## 🗂 Project Structure

```
app/
├── routers/
│   ├── users.py       # User-related endpoints
│   ├── auth.py        # Authentication (login, token)
│   └── notes.py       # Notes CRUD operations
├── models.py          # Database models
├── schemas.py         # Pydantic schemas
├── database.py        # Database configuration
├── oauth2.py          # JWT token logic
├── utils.py           # Utility functions (hashing, helpers)
└── main.py            # Application entry point
```

---

## 🛠 Tech Stack

- **Backend:** Python, FastAPI
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **ORM:** SQLAlchemy
- **Auth:** JWT (OAuth2 Password Flow)
- **Validation:** Pydantic
- **Server:** Uvicorn

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/notes-api.git
cd notes-api
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv env
source env/bin/activate   # Linux / Mac
env\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

---

## 📄 API Documentation

FastAPI provides interactive documentation:

- **Swagger UI:** 👉 http://127.0.0.1:8000/docs
- **ReDoc:** 👉 http://127.0.0.1:8000/redoc

---

## 🔐 Authentication Flow

1. User registers
2. User logs in with email & password
3. JWT access token is returned
4. Token is used to access protected endpoints
5. Each note is linked to its owner

---

## 📝 Example Endpoints

### Auth
- `POST /login` – Login user

### Users
- `POST /users/` – Create user
- `GET /users/{id}` – Get user info

### Notes
- `POST /notes/` – Create note
- `GET /notes/` – Get all user notes
- `GET /notes/{id}` – Get single note
- `PUT /notes/{id}` – Update note
- `DELETE /notes/{id}` – Delete note

---

## 🔒 Security

- Passwords are hashed, never stored in plain text
- JWT tokens are used for authentication
- Users can only access their own notes

---

## 🧪 Future Improvements (Planned)

- 🐳 Docker & Docker Compose support
- 🐘 PostgreSQL integration
- ⚡ Redis caching
- 🔁 Background tasks (Celery)
- 🚦 Rate limiting
- 🧪 Unit & integration testing
- 📊 Logging & monitoring
- 👥 Role-based access control (RBAC)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

