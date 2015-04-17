#!/usr/bin/env python
"""
usage: photos.py [-h] [-l]

Finds all photos in the Photos directory

optional arguments:
  -h, --help  show this help message and exit
  -l, --ls    list the images (default: False)
"""
from docopt import docopt
import inspect
import os
import re

def get_photos(ext='(jpg$)|(gif$)|(png)'):
    """Walk through the photos directory, return a file/directory dictionary."""

    photo_dict = {}

    for dir_name, _, files in os.walk(os.path.dirname(\
            os.path.abspath(inspect.getfile(inspect.currentframe()))), "Photos"):
        for file in files:
            if re.search(r'{0}'.format(ext), file):
                photo_dict[file] = dir_name

    return photo_dict


def print_ls():
    """List the files."""

    photos = get_photos()

    for photo, photo_dir in sorted(photos.items(), key=lambda x: (x[1], x[0])):
        print(photo_dir, photo)


if __name__ == "__main__":

    ARGS = docopt(__doc__)

    if ARGS['--ls']:
        print_ls()
