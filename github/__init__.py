# coding: utf-8

import requests

ROOT_ENDPOINT = "https://api.github.com"


def get_user(username):
    url = "{}/users/{}".format(ROOT_ENDPOINT, username)
    r = requests.get(url)
    return r.json()
