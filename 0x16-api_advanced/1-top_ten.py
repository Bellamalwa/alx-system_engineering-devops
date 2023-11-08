#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
NOTE: Get user agent:
            https://stackoverflow.com/questions/10606133/ -->
            sending-user-agent-using-requests-library-in-python
"""
import requests


def top_ten(subreddit):
    """
    Return top ten titles for a given subreddit
    Return None if invalid subreddit given
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Bellamalwa)"
    }
    params = {
        "limit": 10
        }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
