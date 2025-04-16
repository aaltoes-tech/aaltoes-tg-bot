import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def upload_file(file_path: str):
    """Upload a file to Pinata"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    # Get JWT token from environment
    jwt_token = os.getenv("PINATA_JWT")
    if not jwt_token:
        raise ValueError("PINATA_JWT environment variable is not set")
        
    # Prepare the file
    with open(file_path, 'rb') as file:
        # Prepare multipart form data
        files = {
            'file': (os.path.basename(file_path), file),
            'pinataMetadata': (None, '{"name": "' + os.path.basename(file_path) + '"}'),
            'pinataOptions': (None, '{"cidVersion": 1}')
        }
            
        # Make the request
        headers = {"Authorization": f"Bearer {jwt_token}"}
        response = requests.post(
            "https://api.pinata.cloud/pinning/pinFileToIPFS",
            files=files,
            headers=headers
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to upload file: {response.text}")


if __name__ == "__main__":
    df = pd.read_csv("books_instances.csv")
    files = "sample.png"
    result = upload_file(files)
    ipfs_link = f"https://amaranth-defiant-snail-192.mypinata.cloud/ipfs/{result.get('IpfsHash')}"
    print(ipfs_link)