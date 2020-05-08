#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """ request number of suscribers for a subreddit """
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-agent': 'anything'}
    try:
        js = requests.get(url, headers=header, allow_redirects=False).json()
    except ValueError:
        print("Not Valid JSON")
        return 0

    result = js.get("data")
    subs = result.get("subscribers")

    return subs
