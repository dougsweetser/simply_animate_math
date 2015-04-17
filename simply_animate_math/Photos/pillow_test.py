#!/usr/bin/env python

import argparse as ap
from Pillow import Image

class PillowTest:
    """
    A tool to
    """

    def __init__(self, test_mode = False):


    def run(self):
        "Runs all."

        self.get_needed_downloads()

    def get_needed_downloads(self):
        pass

# Sphinx auto-doc can use these options.
PARSER = ap.ArgumentParser(description=\
        "Aid to ",
        formatter_class = ap.ArgumentDefaultsHelpFormatter)

PARSER.add_argument("--test_mode", action = "store_true",
        default=False,
        help = "use for testing")


if __name__ == "__main__":

    ARGS = PARSER.parse_args()

    with WhatEver(test_mode = ARGS.test_mode) as WE:
        WE.run()
