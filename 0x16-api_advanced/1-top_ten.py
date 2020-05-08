#!/usr/bin/python3
""" make requests """
import requests


def top_ten(subreddit):
    """ prints first 10 top hot posts """
    url = "https://api.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-agent': 'anything'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request.status_code != 200:
        print(None)
        return None

    try:
        js = request.json()
    except:
        return 0

    try:
        result = js.get("data")
        array = result.get("children")

        for post in array[:10]:
            hposts = post.get("data")
            title = hposts.get("title")
            print(title)

    except ValueError:
        return None
