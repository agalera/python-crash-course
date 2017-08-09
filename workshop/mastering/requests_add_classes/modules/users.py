import requests
import logging


logging.basicConfig(level=logging.DEBUG)


class User(object):
    base_url = "http://localhost"
    r = requests.Session()
    for attr in ['get', 'put', 'post', 'delete']:
        setattr(r, attr, lambda url, *args, **kwargs: (getattr(r, attr)('%s%s' % (base_url, url), *args, **kwargs)))

    @classmethod
    def get_users(cls):
        return cls.r.get('/users').json()
