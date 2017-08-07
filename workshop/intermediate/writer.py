#!/usr/bin/env python
import sys
import os
import urllib2
import json


def main(url, file_path):
    """
    Write content from url into file

    Implement in Python:
    $ curl url >> file_path

    :param url:
    :param file_path:
    """
    request = urllib2.Request(url=url)
    f = urllib2.urlopen(request)
    content = json.dumps(f.read())

    # This is a context manager. Implements __enter__, __exit__ protocols
    # out of the with indentation the file is closed
    with open(file_path, "wb") as f:
        f.write(content)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        url = "https://pokeapi.co/api/v2/pokemon/3/"
        file_path = os.path.abspath(sys.arg[1])
        main(url, file_path)
