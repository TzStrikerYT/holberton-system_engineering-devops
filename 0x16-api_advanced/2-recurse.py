#!/usr/bin/python3
""" make requests """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ prints first 10 top hot posts """
    url = "https://api.reddit.com/r/{}/hot.json?after={}".format(
        subreddit, after)
    header = {'User-agent': 'anything'}
    request = requests.get(url, headers=header, allow_redirects=False)

    if request:
        js = request.json()
        child = js.get("data").data.get("children")
        [hot_list.append(i.get("data").get("title")) for i in child]
        after = js.get("after")

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list

    return None
