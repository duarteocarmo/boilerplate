import re
from dataclasses import dataclass
from datetime import datetime

from dotenv import dotenv_values
from reddit_client.client import RedditClient
from reddit_client.config import SUBREDDITS


@dataclass
class Songpost:
    title: str
    source: str
    source_id: str
    upvotes: int
    upvote_ratio: float
    subreddit: str
    subreddit_subscribers: int
    permalink: str
    total_awards_received: int
    created_utc: datetime


def extract_youtube_id(url: str) -> str:
    URL_REGEX = r"http(s?):\/\/((www|m)\.)?youtube\.com\/watch\?.*v=(.{11}).*"
    match = re.search(URL_REGEX, url)
    if match:
        return match.group(4)
    
    TINYURL_REGEX = r"http(s?):\/\/(www\.)?youtu\.be\/(.{11}).*"
    match = re.search(TINYURL_REGEX, url)
    if match:
        return match.group(3)
    
    raise RuntimeError(f"Could not extract youtube id from {url}")


def main():
    config = dotenv_values()
    client = RedditClient(config)
    songs = []

    for subreddit in SUBREDDITS:
        posts = client.get(
            path="r/{subreddit}/top",
            params={"limit": 100, "t": "month"},
            subreddit=subreddit,
        )

        for post in posts["data"]["children"]:
            post_data = post["data"]
            url = post_data["url"]
            if post_data["domain"] in ("youtube.com", "youtu.be", "m.youtube.com"):
                song = Songpost(
                    title=post["data"]["title"],
                    source_id=extract_youtube_id(url),
                    source="youtube",
                    upvotes=post_data["ups"],
                    upvote_ratio=post_data["upvote_ratio"],
                    subreddit=post_data["subreddit"],
                    subreddit_subscribers=post_data["subreddit_subscribers"],
                    permalink=post_data["permalink"],
                    total_awards_received=post_data["total_awards_received"],
                    created_utc=datetime.utcfromtimestamp(post_data["created_utc"]),
                )

                songs.append(song)
            else:
                print(f"Skipping unrecognised domain url: ({post_data['domain']}) {url}")

    print(f"Found {len(songs)} songs")


if __name__ == "__main__":
    main()
