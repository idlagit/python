import requests
import json
from os import environ
from dotenv import load_dotenv

def okta_api_get(url: str):
    ''' Function to return api response, accepts 'url' as argument'''
    headers = {'Authorization': f'SSWS {os.environ.get("okta_api_token")}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Could not fetch response. Status code >: {response.status_code}')

# load the .env enviroment file
load_dotenv()

# define url variable
url = f'{os.environ.get("okta_url")}/api/v1/groups/{os.environ.get("okta_group_id")}/users'

# function call
okta_api_get(url)
