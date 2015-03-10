#!/usr/bin/env python
"""Data that matches a dictionary to files."""

import argparse as ap
import inspect
import os
import re

def get_photos(ext='jpg'):
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


# Sphinx auto-doc can use these options.
PARSER = ap.ArgumentParser(description=\
        "Finds all photos in the Photos directory", \
        formatter_class=ap.ArgumentDefaultsHelpFormatter)

PARSER.add_argument("-l", "--ls", action="store_true", \
        default=False, help="list the images")

if __name__ == "__main__":

    ARGS = PARSER.parse_args()

    if ARGS.ls:
        print_ls()
