#!/usr/bin/env python

import argparse as ap
import os
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

        count = 100

        for equation, operator, number_2d, D1_numbers, D3_numbers in zip(config.equations, config.operators, config.D2_constant_time_numbers, config.D1.t.numbers, config.D3.t.numbers):
            self.create_background(template.dynamic_3d.line)
            self.draw_equation(equation)
            self.draw_numbers_2d_1(number_2d)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            for D1_number, D3_number in zip(D1_numbers, D3_numbers):
                self.draw_numbers_2d_2(D1_number)
                self.draw_numbers_2d_3(D3_number)

                self.work_img.save("Animations/dynamic_3d_t.{0}.png".format(count))
                count += 1

        os.system("/opt/local/bin/convert -loop 0 -delay 60 Animations/dynamic_3d_t.*png Animations/dynamic_3d_t.gif")

        count = 100

        for equation, operator, number_2d, D1_numbers in zip(config.equations, config.operators, config.D2_constant_time_numbers, config.D1.t.numbers):
            self.create_background(template.dynamic_1d.line)
            self.draw_equation(equation)
            self.draw_numbers_2d_1(number_2d)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            for D1_number in D1_numbers:
                self.draw_numbers_2d_2(D1_number)

                self.work_img.save("Animations/dynamic_1d_t.{0}.png".format(count))
                count += 1

        os.system("/opt/local/bin/convert -loop 0 -delay 60 Animations/dynamic_1d_t.*png Animations/dynamic_1d_t.gif")


        count = 100

        for equation, operator, number_2d, D1_numbers in zip(config.equations, config.operators, config.D2_constant_motion_numbers, config.D1.m.numbers):
            self.create_background(template.dynamic_1d.line)
            self.draw_equation(equation)
            self.draw_numbers_2d_1(number_2d)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            for D1_number in D1_numbers:
                self.draw_numbers_2d_2(D1_number)

                self.work_img.save("Animations/dynamic_1d_m.{0}.png".format(count))
                count += 1

        os.system("/opt/local/bin/convert -loop 0 -delay 60 Animations/dynamic_1d_m.*png Animations/dynamic_1d_m.gif")


        count = 100

        for equation, operator, number_2d, D1_numbers in zip(config.equations, config.operators, config.D2_constant_space_numbers, config.D1.r.numbers):
            self.create_background(template.dynamic_1d.line)
            self.draw_equation(equation)
            self.draw_numbers_2d_1(number_2d)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            for D1_number in D1_numbers:
                self.draw_numbers_2d_2(D1_number)

                self.work_img.save("Animations/dynamic_1d_r.{0}.png".format(count))
                count += 1

        os.system("/opt/local/bin/convert -loop 0 -delay 60 Animations/dynamic_1d_r.*png Animations/dynamic_1d_r.gif")


        count = 100

        for equation, operator, number in zip(config.equations, config.operators, config.D2_constant_time_numbers):
            self.create_background(template.plane.line)
            self.draw_equation(equation)
            self.draw_numbers(number)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            self.work_img.save("Animations/plane_t.{0}.png".format(count))
            count += 1
        os.system("/opt/local/bin/convert -loop 0 -delay 350 Animations/plane_t.*png Animations/plane_t.gif")


        count = 100

        for equation, operator, number in zip(config.equations, config.operators, config.D2_constant_space_numbers):
            self.create_background(template.plane.line)
            self.draw_equation(equation)
            self.draw_numbers(number)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            self.work_img.save("Animations/plane_r.{0}.png".format(count))
            count += 1
        os.system("/opt/local/bin/convert -loop 0 -delay 350 Animations/plane_r.*png Animations/plane_r.gif")

        for equation, operator, number in zip(config.equations, config.operators, config.D2_constant_motion_numbers):
            self.create_background(template.plane.line)
            self.draw_equation(equation)
            self.draw_numbers(number)
            self.draw_operator(operator)
            self.draw_equal(config.equal)

            self.work_img.save("Animations/plane_m.{0}.png".format(count))
            count += 1
        os.system("/opt/local/bin/convert -loop 0 -delay 350 Animations/plane_m.*png Animations/plane_m.gif")


    def create_background(self, line):
        """Create the initial background, stays the same."""

        self.work_img = self.base_img.copy()
        draw = ImageDraw.Draw(self.work_img)
        draw.line(line.pos, line.color, line.width)
        del draw
        self.work_img.save("/tmp/background.bmp")

    def draw_equation(self, equation):
        """Draws equation at the top."""

        photo_dir = self.photos[equation]
        eq_img = Image.open("{0}/{1}".format(photo_dir, equation))
        eq_info = template.thumb_box_info("equation", eq_img.size)
        eq_img.thumbnail(eq_info["thumb"])
        print("eq thumb: {0}, {1}".format(eq_info["thumb"][0], eq_info["thumb"][1]))
        print("eq size: {0}, {1}".format(eq_img.size[0], eq_img.size[1]))
        print("eq box: {0}, {1}, {2}, {3}".format(eq_info["box"][0], eq_info["box"][1], eq_info["box"][2], eq_info["box"][3]))
        eq_info["box"][3] = eq_info["box"][1] + eq_img.size[1]
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

    def draw_numbers_2d_1(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_1_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])
            self.work_img.paste(n_img, n_info["box"])
        self.work_img.save("/tmp/numbers_2d_1.bmp")

    def draw_numbers_2d_2(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_2_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])

            n_info["box"][3] = n_info["box"][1] + n_img.size[1]

            self.work_img.paste(n_img, n_info["box"])

        self.work_img.save("/tmp/numbers_2d_2.bmp")


    def draw_numbers_2d_3(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_3_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])
            print("sam 2d_3 thumb: {0}, {1}".format(n_info["thumb"][0], n_info["thumb"][1]))
            print("sam 2d_3 box: {0}, {1}, {2}, {3}".format(n_info["box"][0], n_info["box"][1], n_info["box"][2], n_info["box"][3]))
            print("sam size: {0}, {1}".format(n_img.size[0], n_img.size[1]))

            n_info["box"][3] = n_info["box"][1] + n_img.size[1]

            self.work_img.paste(n_img, n_info["box"])

        self.work_img.save("/tmp/numbers_2d_3.bmp")


    def draw_operator(self, operator_file):
        """Draws operator on image."""

        photo_dir = self.photos[operator_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, operator_file))
        op_info = template.thumb_box_info("operator", op_img.size)
        op_img.thumbnail(op_info["thumb"])
        self.work_img.paste(op_img, op_info["box"])
        self.work_img.save("/tmp/operator.bmp")


    def draw_equal(self, equal_file):
        """Draws equals on image."""

        photo_dir = self.photos[equal_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, equal_file))
        op_info = template.thumb_box_info("equal", op_img.size)
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
