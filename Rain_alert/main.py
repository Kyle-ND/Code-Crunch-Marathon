import os 
from dotenv import load_dotenv
import requests ,json

def get_data():
    api_url = os.getenv('API_url')
    response = requests.get(url=api_url)
    data_str = response.text
    data = json.loads(data_str)
    response.raise_for_status()
    
    print(data)

def main():
    load_dotenv()
    get_data()

if __name__ == '__main__':
    main()