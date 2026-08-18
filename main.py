from fastapi import FastAPI, UploadFile, File, HTTPException
import os

# Create an instance of the FastAPI application
app = FastAPI()

# directly creates a new folder
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to File Manager API!"
    }

@app.post("/upload")
# We use async because reading uploaded files is an asynchronous operation in FastAPI.
#  It allows the server to handle other requests while waiting for file operations
async def upload_file(file: UploadFile = File(...)):
    
    # Allow only text files
    if not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message": f"{file.filename} uploaded successfully!"
    }

@app.get("/read/{filename}")
def read_file(filename: str):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Check if file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    return {
        "filename": filename,
        "content": content
    }

@app.get("/files")
def list_files():

    files = os.listdir(UPLOAD_FOLDER)

    return {
        "files": files
    }

@app.delete("/delete/{filename}")
def delete_file(filename: str):

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )

    os.remove(file_path)

    return {
        "message": f"{filename} deleted successfully!"
    }