from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

LOCAL_FILE_PATH = "saved_models/R_hat2.zip"
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
MINIO_BUCKET_NAME = "test-bucket"
if __name__ == "__main__":
    found = MINIO_CLIENT.bucket_exists(MINIO_BUCKET_NAME)
    if not found:
       MINIO_CLIENT.make_bucket(MINIO_BUCKET_NAME)
    else:
       print("Bucket already exists") 

    MINIO_CLIENT.fput_object(MINIO_BUCKET_NAME, "R_hat2.zip", LOCAL_FILE_PATH)    
    print("It is successfully uploaded to bucket")
