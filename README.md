## 🚀 Flask RESTful User API

A robust Python Flask CRUD (Create, Read, Update, Delete) API for managing user data. This project leverages SQLAlchemy for ORM management and provides an automatically documented interface via Flask-RESTX and Flasgger. 

* * *

## 🛠 Tech Stack

*   Framework: Flask
*   Database ORM: Flask-SQLAlchemy
*   API Documentation: [Flask-RESTX](https://flask-restx.readthedocs.io/) & [Flasgger](https://github.com/flasgger/flasgger)
*   Database: SQLite (default) / PostgreSQL / MySQL 

* * *

## 📦 Installation & Setup 

1.  Clone the repository:
    
        git clone https://github.com
        cd flask-user-api
        
    
2.  Create a virtual environment:
    
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        
    
3.  Install dependencies:
    
        pip install flask flask-sqlalchemy flask-restx flasgger
        
    
4.  Initialize the database:
    
        python -c "from app import db; db.create_all()"
        
    
5.  Run the application:
    
        python app.py
        
    
    \

* * *

## 📖 API Documentation (Swagger)

Once the server is running, access the interactive documentation at:

*   Flask-RESTX UI: `http://localhost:5000/`
*   Flasgger UI: `http://localhost:5000/apidocs` \

* * *

## 🛣 API Endpoints

## 👤 User Management CRUD

| Method  | Endpoint | Description |
| --- | --- | --- |
| 📥 GET | /users | Get All: Retrieve a list of all registered users |
| 🔍 GET | /users/<id> | Get One: Retrieve details for a specific user by ID |
| ✨ POST | /users | Create: Register a new user with JSON payload |
| 🔄 PUT | /users/<id> | Update: Modify existing user information |
| 🗑️ DELETE | /users/<id> | Delete: Remove a user from the system |

* * *

## 📄 Project Structure

```
📂 flask-user-api/ (Root)
├── 📂 .venv/                   # 🐍 Python Virtual Environment (Dependencies)
├── 📂 .idea/                   # ⚙️ IDE configuration (PyCharm/JetBrains)
│   └── 📂 inspectionProfiles/
├── 📂 instance/                # 🗄️ Database files (e.g., users.db)
├── 📂 models/                  # 🏗️ SQLAlchemy User database schemas
│   └── 📄 user.py              # 👤 User model definition
├── 📂 routes/                  # 🛣️ Flask-RESTX & Swagger API endpoints
│   └── 📄 user_routes.py       # 🛠️ CRUD logic (GET, POST, etc.)
├── 📂 static/                  # 🎨 Static assets (CSS, JS, Images)
├── 📄 .env                     # 🔑 Environment variables (PRIVATE)
├── 📄 .gitignore               # 🚫 Files to exclude from Git (.venv, .env)
├── 📄 app.py                   # 🚀 Application entry point & setup
├── 📄 README.md                # 📖 Project documentation & instructions
└── 📄 requirements.txt         # 📦 List of Python dependencies

 ```