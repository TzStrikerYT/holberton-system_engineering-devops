#!/usr/bin/python3
""" make requests """
import requests


def number_of_subscribers(subreddit):
    """ request number of suscribers for a subreddit """
    url = "https://api.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-agent': 'anything'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        return 0

    try:
        js = request.json()
    except:
        return 0

    result = js.get("data")

    if result:
        subs = result.get("subscribers")
        if subs:
            return subs
    return 0
