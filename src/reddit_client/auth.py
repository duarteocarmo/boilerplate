import requests


def get_auth_headers(
    token_url: str,
    client_id: str,
    api_secret: str,
    username: str,
    password: str,
):
    auth = requests.auth.HTTPBasicAuth(client_id, api_secret)

    data = {"grant_type": "password", "username": username, "password": password}
    headers = {"User-Agent": "pyplaylist/0.1.0"}

    res = requests.post(token_url, auth=auth, data=data, headers=headers)
    res.raise_for_status()
    token = res.json()["access_token"]

    return {**headers, **{"Authorization": f"bearer {token}"}}
