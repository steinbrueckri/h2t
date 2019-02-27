import requests

def get(url, ret="headers", redirects=True, user_agent=False):
    if user_agent:
        headers = {'user-agent': user_agent}
        r = requests.get(url, allow_redirects=redirects, headers=headers)
    else:
        r = requests.get(url, allow_redirects=redirects)
    if ret == "headers":
        return r.headers
