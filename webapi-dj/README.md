# 🧪 Django Dummy API Service, PORT - 8001

This project is a simple Django backend exposing several **dummy APIs** (addition, multiplication, echo, health check) for testing and development purposes. APIs are available via **POST** and return JSON responses. You can run the service either directly with Python or using Docker.

---

## 🚀 How to Run the Project

### ▶️ Run Directly (Locally, for Development)

Make sure Python and pip are installed. Then:

```bash
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8001
```

### 🐳 Run with Docker
Make sure Docker is installed. Then: (go to the project root directory)

```bash
docker-compose up --build
```


