from fastapi import FastAPI, UploadFile, File
from minio import Minio
import os

app = FastAPI()

minio_client = Minio(
    "minio:9000",
    access_key="minio",
    secret_key="minio123",
    secure=False
)


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_name = file.filename
    file_path = f"/tmp/{file_name}"

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    minio_client.fput_object("memes", file_name, file_path)

    os.remove(file_path)

    return {"url": f"http://minio:9000/memes/{file_name}"}


@app.delete("/delete/{file_name}")
async def delete_image(file_name: str):
    minio_client.remove_object("memes", file_name)
    return {"message": "Image deleted successfully"}