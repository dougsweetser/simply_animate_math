#!/usr/bin/env python

import argparse as ap
from PIL import Image, ImageColor, ImageDraw, ImageFont

import config
import photos
import template

class SimplyAnimateMath:
    """
    A tool to take photos and make animations.
    """

    def __init__(self, test_mode = False):
        self.base_img = Image.new('RGB', (config.width, config.height), (183, 189, 177))
        self.photos = photos.get_photos()
        self.work_img = self.base_img.copy()


    def run(self):
        "Runs all."

        self.create_background()
        self.draw_equation(config.plane_t.equation)
        self.draw_numbers(config.plane_t.numbers)
        self.draw_operator(config.plane_t.operator)
        self.draw_equal(config.equal)

        self.work_img.show()


    def create_background(self):
        """Create the initial background, stays the same."""

        draw = ImageDraw.Draw(self.work_img)
        draw.line(template.plane.line.pos, template.plane.line.color, \
                template.plane.line.width)
        del draw
        self.work_img.save("/tmp/background.bmp")


    def draw_equation(self, equation):
        """Draws equation at the top."""

        photo_dir = self.photos[equation]
        eq_img = Image.open("{0}/{1}".format(photo_dir, equation))
        eq_info = template.equation_info(eq_img.size)
        eq_img.thumbnail(eq_info["thumb"])
        self.work_img.paste(eq_img, eq_info["box"])
        self.work_img.save("/tmp/equation.bmp")


    def draw_numbers(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])
            self.work_img.paste(n_img, n_info["box"])
        self.work_img.save("/tmp/numbers.bmp")


    def draw_operator(self, operator_file):
        """Draws operators on image."""

        photo_dir = self.photos[operator_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, operator_file))
        op_info = template.operator_info(op_img.size)
        op_img.thumbnail(op_info["thumb"])
        self.work_img.paste(op_img, op_info["box"])
        self.work_img.save("/tmp/operator.bmp")


    def draw_equal(self, equal_file):
        """Draws equals on image."""

        photo_dir = self.photos[equal_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, equal_file))
        op_info = template.equal_info(op_img.size)
        op_img.thumbnail(op_info["thumb"])
        self.work_img.paste(op_img, op_info["box"])
        self.work_img.save("/tmp/equal.bmp")



# Sphinx auto-doc can use these options.
PARSER = ap.ArgumentParser(description=\
        "Pulls images together to make an animation", \
        formatter_class=ap.ArgumentDefaultsHelpFormatter)

PARSER.add_argument("--test_mode", action = "store_true", \
        default=False, help="use for testing")


if __name__ == "__main__":

    ARGS = PARSER.parse_args()

    SAM = SimplyAnimateMath(test_mode = False)
    SAM.run()
