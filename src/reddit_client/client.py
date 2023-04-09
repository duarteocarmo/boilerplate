from typing import Any

import requests

from src.reddit_client.auth import get_auth_headers


class RedditClient:
    def __init__(self, config: dict) -> None:
        self.base_url = config["REDDIT_API_URL"]
        self.headers = get_auth_headers(
            token_url=config["REDDIT_AUTH_URL"],
            client_id=config["REDDIT_API_CLIENT_ID"],
            api_secret=config["REDDIT_API_SECRET"],
            username=config["REDDIT_USERNAME"],
            password=config["REDDIT_PASSWORD"],
        )

    def get(self, path: str, params: dict[str, str] | None, **kwargs) -> dict[str, Any]:
        resource = path.format(**kwargs)
        response = requests.get(f"{self.base_url}/{resource}", params=params, headers=self.headers)
        response.raise_for_status()
        return response.json()
