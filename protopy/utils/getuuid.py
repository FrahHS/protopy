import requests
from uuid import UUID

def get_uuid(username: str) -> UUID:
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    response = requests.get(url)
    return UUID(response.json()['id'])
