#!/usr/bin/env python
import argparse as ap
import os
from PIL import Image, ImageColor, ImageDraw, ImageFont
import re

import config
import photos
import template

class SimplyAnimateMath:
    """
    A tool to take photos and make animations.
    """

    def __init__(self, test_mode = False):
        self.base_img = Image.new('RGBA', (config.width, config.height), (183, 189, 177, 256))
        self.photos = photos.get_photos()
        self.work_img = self.base_img.copy()
        self.font = ImageFont.truetype(config.font, config.font_size)


    def run(self):
        "Runs all."

        constants = ("t", "r", "m")

        for constant in constants:
            self.animate_plane(config.D2_constant_numbers[constant], "plane_{c}".format(c=constant))
            self.animate_plane_D1(config.D2_constant_numbers[constant], config.D1[constant]["numbers"], "dynamic_D1_{c}".format(c=constant))
            self.animate_plane_D1_D3(config.D2_constant_numbers[constant], config.D1[constant]["numbers"], config.D3[constant]["numbers"], "dynamic_D3_{c}".format(c=constant))

            for common_name in ("dynamic_D1", "dynamic_D3"):
                self.merge_2_gifs(common_name, constant, "plus", "times")
                self.merge_2_gifs(common_name, constant, "minus", "div")
                self.merge_box_gifs(common_name, constant, "plus_times", "minus_div")

    def create_background(self, line):
        """Create the initial background, stays the same."""

        self.work_img = self.base_img.copy()
        draw = ImageDraw.Draw(self.work_img)
        draw.line(line.pos, line.color, line.width)
        del draw

        self.work_img.save("/tmp/background.png")


    def draw_equation(self, equation):
        """Draws equation at the top."""

        photo_dir = self.photos[equation]
        eq_img = Image.open("{0}/{1}".format(photo_dir, equation))
        eq_info = template.thumb_box_info("equation", eq_img.size)
        eq_img.thumbnail(eq_info["thumb"])
        eq_info["box"][3] = eq_info["box"][1] + eq_img.size[1]
        self.work_img.paste(eq_img, eq_info["box"])
        self.work_img.save("/tmp/equation.png")


    def draw_numbers(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])
            self.work_img.paste(n_img, n_info["box"])
        self.work_img.save("/tmp/numbers.png")


    def draw_numbers_2d_1(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_1_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])
            self.work_img.paste(n_img, n_info["box"])
        self.work_img.save("/tmp/numbers_2d_1.png")


    def draw_numbers_2d_2(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_2_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])

            n_info["box"][3] = n_info["box"][1] + n_img.size[1]

            self.work_img.paste(n_img, n_info["box"])

        self.work_img.save("/tmp/numbers_2d_2.png")


    def draw_numbers_2d_3(self, number_files):
        """Puts number files on image."""

        for i, number_file in enumerate(number_files):
            photo_dir = self.photos[number_file]
            n_img = Image.open("{0}/{1}".format(photo_dir, number_file))
            n_info = template.number_2d_3_info(n_img.size, i)
            n_img.thumbnail(n_info["thumb"])

            n_info["box"][3] = n_info["box"][1] + n_img.size[1]

            self.work_img.paste(n_img, n_info["box"])

        self.work_img.save("/tmp/numbers_2d_3.png")


    def write_time_d1(self, time_string):
        """Writes time as a number."""

        draw = ImageDraw.Draw(self.work_img)
        draw.text(template.time_1d_pos, time_string, font=self.font, fill=(0, 0, 0, 255))
        del draw

        self.work_img.save("/tmp/time_d1.png")

    def write_time_d3(self, time_string):
        """Writes time as a number."""

        draw = ImageDraw.Draw(self.work_img)
        draw.text(template.time_3d_pos, time_string, font=self.font, fill=(0, 0, 0, 255))
        del draw

        self.work_img.save("/tmp/time_d3.png")


    def draw_operator(self, operator_file):
        """Draws operator on image."""

        photo_dir = self.photos[operator_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, operator_file))
        op_info = template.thumb_box_info("operator", op_img.size)
        op_img.thumbnail(op_info["thumb"])
        self.work_img.paste(op_img, op_info["box"])
        self.work_img.save("/tmp/operator.png")


    def draw_equal(self, equal_file):
        """Draws equals on image."""

        photo_dir = self.photos[equal_file]
        op_img = Image.open("{0}/{1}".format(photo_dir, equal_file))
        op_info = template.thumb_box_info("equal", op_img.size)
        op_img.thumbnail(op_info["thumb"])
        self.work_img.paste(op_img, op_info["box"])
        self.work_img.save("/tmp/equal.png")


    def animate_plane(self, D2_numbers, short_name="test", dir_name="Animations"):
        """Given 2D numbers triplets, shows plus, minus, times, and div animation."""

        for count, equation, operator, D2_number in zip(range(100, 104), config.equations, config.operators, D2_numbers):

            self.create_background(template.plane.line)
            self.draw_equation(equation)
            self.draw_operator(operator)
            self.draw_equal(config.equal)
            self.draw_numbers(D2_number)

            self.work_img.save("{dn}/{sn}.{ct}.png".format(dn=dir_name, sn=short_name, ct=count))

            os.system("{convert} -loop 0 -delay 350 {dn}/{sn}.*.png {dn}/{sn}.gif".format(\
                    convert=config.convert, dn=dir_name, sn=short_name))
        print("gif done: {dn}/{sn}.gif".format(dn=dir_name, sn=short_name))


    def animate_plane_D1(self, D2_numbers, D1_number_numbers, short_name="test", dir_name="Animations"):
        """Given a pair of 1D and 2D numbers, make plus, minus, times, and div animations."""

        for equation, operator, D2_number, D1_number_number in zip(config.equations, config.operators, D2_numbers, D1_number_numbers):

            for count, D1_number in enumerate(D1_number_number):
                self.create_background(template.dynamic_1d.line)
                self.draw_equation(equation)
                self.draw_operator(operator)
                self.draw_equal(config.equal)
                self.draw_numbers_2d_1(D2_number)
                self.draw_numbers_2d_2(D1_number)
                self.write_time_d1(str(count + 1))

                op_name = re.sub(r'....$', r'', operator)
                self.work_img.save("{dn}/{sn}_{on}.{ct}.png".format(dn=dir_name, sn=short_name, on=op_name, ct=str(100 + count)))

            os.system("{convert} -loop 0 -delay 60 {dn}/{sn}_{on}.*.png {dn}/{sn}_{on}.gif".format(\
                    convert=config.convert, dn=dir_name, sn=short_name, on=op_name))
            print("gif done: {dn}/{sn}_{on}.gif".format(dn=dir_name, sn=short_name, on=op_name))


    def animate_plane_D1_D3(self, D2_numbers, D1_number_numbers, D3_number_numbers, short_name="test", dir_name="Animations"):
        """Given a pair of 1D and 2D numbers, make plus, minus, times, and div animations."""

        for equation, operator, D2_number, D1_number_number, D3_number_number in zip(config.equations, config.operators, D2_numbers, D1_number_numbers, D3_number_numbers):

            for count, D1_number, D3_number in zip(range(0, len(D1_number_number)), D1_number_number, D3_number_number):
                self.create_background(template.dynamic_3d.line)
                self.draw_equation(equation)
                self.draw_operator(operator)
                self.draw_equal(config.equal)
                self.draw_numbers_2d_1(D2_number)
                self.draw_numbers_2d_2(D1_number)
                self.draw_numbers_2d_3(D3_number)
                self.write_time_d1(str(count + 1))
                self.write_time_d3(str(count + 1))

                op_name = re.sub(r'....$', r'', operator)
                self.work_img.save("{dn}/{sn}_{on}.{ct}.png".format(dn=dir_name, sn=short_name, on=op_name, ct=count + 100))

            os.system("{convert} -loop 0 -delay 60 {dn}/{sn}_{on}.*.png {dn}/{sn}_{on}.gif".format(\
                    convert=config.convert, dn=dir_name, sn=short_name, on=op_name))
            print("gif done: {dn}/{sn}_{on}.gif".format(dn=dir_name, sn=short_name, on=op_name))


    def merge_2_gifs(self, common_name, constant, operator_1, operator_2, dir_name="Animations"):
        """Merge two animations animations."""

        file_1 = "{dn}/{cn}_{con}_{op_1}.gif".format(dn=dir_name, cn=common_name, con=constant, op_1=operator_1)
        file_2 = "{dn}/{cn}_{con}_{op_2}.gif".format(dn=dir_name, cn=common_name, con=constant, op_2=operator_2)
        file_1_2 = "{dn}/{cn}_{con}_{op_1}_{op_2}.gif".format(dn=dir_name, cn=common_name, con=constant, op_1=operator_1, op_2=operator_2)

        command = "{convert} {f_1} -repage {w2}x{h} -coalesce null: \( {f_2} -coalesce \) -geometry +{w}+0 -layers Composite {f_1_2}".format(\
                convert=config.convert, f_1=file_1, f_2=file_2, f_1_2=file_1_2, w2=config.width * 2, w=config.width, h=config.height)
        print(command)
        os.system(command)
        print("merge done: {f_1_2}".format(f_1_2=file_1_2))


    def merge_box_gifs(self, common_name, constant, operator_1, operator_2, dir_name="Animations"):
        """Merge two animations animations."""

        file_1 = "{dn}/{cn}_{con}_{op_1}.gif".format(dn=dir_name, cn=common_name, con=constant, op_1=operator_1)
        file_2 = "{dn}/{cn}_{con}_{op_2}.gif".format(dn=dir_name, cn=common_name, con=constant, op_2=operator_2)
        file_1_2 = "{dn}/{cn}_{con}_{op_1}_{op_2}.gif".format(dn=dir_name, cn=common_name, con=constant, op_1=operator_1, op_2=operator_2)

        os.system("{convert} {f_1} -repage {w2}x{h2} -coalesce null: \( {f_2} -coalesce \) -geometry +0+{h} -layers Composite {f_1_2}".format(\
                convert=config.convert, f_1=file_1, f_2=file_2, f_1_2=file_1_2, w2=config.width * 2, h=config.height, h2=config.height * 2))
        print("merge done: {f_1_2}".format(f_1_2=file_1_2))


# Sphinx auto-doc can use these options.
PARSER = ap.ArgumentParser(description=\
        "Pulls images together to make an animation", \
        formatter_class=ap.ArgumentDefaultsHelpFormatter)


if __name__ == "__main__":

    ARGS = PARSER.parse_args()

    SAM = SimplyAnimateMath(test_mode = False)
    SAM.run()
