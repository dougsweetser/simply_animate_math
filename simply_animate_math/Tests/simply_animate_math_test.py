import inspect
import nose
import os
from PIL import Image, ImageChops
import sys
import unittest

sys.path.insert(0, '..')
import simply_animate_math
import template

class SimplyAnimateMathTests(unittest.TestCase):

    ref_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    def test_create_background(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.create_background(template.plane.line)
        new_img = Image.open("/tmp/background.png")
        ref_img = Image.open("{0}/ref.background.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_equation(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_equation("3_plus_3.jpg")
        new_img = Image.open("/tmp/equation.png")
        ref_img = Image.open("{0}/ref.equation.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_numbers(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_numbers(("N1n1.jpg", "N1n1.jpg", "N1n1.jpg"))
        new_img = Image.open("/tmp/numbers.png")
        ref_img = Image.open("{0}/ref.numbers.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_numbers_2d_1(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_numbers_2d_1(("N1n1.jpg", "N1n1.jpg", "N1n1.jpg"))
        new_img = Image.open("/tmp/numbers_2d_1.png")
        ref_img = Image.open("{0}/ref.numbers_2d_1.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_numbers_2d_2(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_numbers_2d_2(("N1.jpg", "N1.jpg", "N1.jpg"))
        new_img = Image.open("/tmp/numbers_2d_2.png")
        ref_img = Image.open("{0}/ref.numbers_2d_2.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_write_time(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.write_time("2")
        new_img = Image.open("/tmp/time_123.png")
        ref_img = Image.open("{0}/ref.time_123.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_operator(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_operator("plus.jpg")
        new_img = Image.open("/tmp/operator.png")
        ref_img = Image.open("{0}/ref.operator.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_equal(self):
        sam = simply_animate_math.SimplyAnimateMath(skip=[])
        sam.draw_equal("equal.jpg")
        new_img = Image.open("/tmp/equal.png")
        ref_img = Image.open("{0}/ref.equal.png".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)


if __name__ == '__main__':
    nose.runmodule()
