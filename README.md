# File Manager API

A simple RESTful File Manager API built using **Python and FastAPI**. This project provides API endpoints to upload, read, list, and delete text files.

## 🚀 Features

* Upload `.txt` files
* Read uploaded file contents
* List all uploaded files
* Delete uploaded files
* File type validation
* Error handling using HTTP status codes
* Interactive API documentation with Swagger UI
* RESTful API architecture

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **Python Multipart**

## 📁 Project Structure

```text
file-manager-api/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── uploads/
    └── .gitkeep
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/file-manager-api.git
```

### 2. Navigate to the project directory

```bash
cd file-manager-api
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📚 API Documentation

FastAPI automatically provides interactive Swagger documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can also access the ReDoc documentation at:

```text
http://127.0.0.1:8000/redoc
```

## 🔗 API Endpoints

| Method | Endpoint             | Description                      |
| ------ | -------------------- | -------------------------------- |
| GET    | `/`                  | Check whether the API is running |
| POST   | `/upload`            | Upload a `.txt` file             |
| GET    | `/read/{filename}`   | Read the contents of a file      |
| GET    | `/files`             | List all uploaded files          |
| DELETE | `/delete/{filename}` | Delete a file                    |

## 📤 Upload a File

Use:

```http
POST /upload
```

The API accepts only `.txt` files.

Example response:

```json
{
  "message": "example.txt uploaded successfully!"
}
```

## 📖 Read a File

Use:

```http
GET /read/{filename}
```

Example:

```text
GET /read/example.txt
```

Example response:

```json
{
  "filename": "example.txt",
  "content": "Hello from the File Manager API!"
}
```

## 📂 List Files

Use:

```http
GET /files
```

Example response:

```json
{
  "files": [
    "example.txt",
    "notes.txt"
  ]
}
```

## 🗑️ Delete a File

Use:

```http
DELETE /delete/{filename}
```

Example:

```text
DELETE /delete/example.txt
```

Example response:

```json
{
  "message": "example.txt deleted successfully!"
}
```

## ❌ Error Handling

The API handles common errors such as:

* Invalid file type
* File not found
* Invalid requests

For example, uploading a non-text file returns a `400 Bad Request` response.

## 🧪 Testing

The API can be tested using:

* Swagger UI
* Postman
* Browser for GET endpoints
* Any REST API client

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## 🎯 Learning Objectives

This project demonstrates:

* FastAPI application development
* REST API design
* HTTP methods
* File upload handling
* File system operations
* API validation
* Exception handling
* Interactive API documentation

## 🔮 Future Improvements

Possible improvements include:

* Support for multiple file formats
* Multiple file uploads
* File size restrictions
* Authentication and authorization
* File download endpoint
* Database integration
* Cloud storage integration
* Improved file security
* File metadata management

## 👩‍💻 Author

**Sejal Patole**

---

⭐ If you found this project useful, consider giving the repository a star!
