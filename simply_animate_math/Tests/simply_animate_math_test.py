import inspect
import nose
import os
from PIL import Image, ImageChops
import sys
import unittest

sys.path.insert(0, '..')
import simply_animate_math

class SimplyAnimateMathTests(unittest.TestCase):

    ref_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    def test_create_background(self):
        sam = simply_animate_math.SimplyAnimateMath()
        sam.create_background()
        new_img = Image.open("/tmp/background.bmp")
        ref_img = Image.open("{0}/ref.background.bmp".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_equation(self):
        sam = simply_animate_math.SimplyAnimateMath()
        sam.create_background()
        sam.draw_equation("3_plus_3.jpg")
        new_img = Image.open("/tmp/equation.bmp")
        ref_img = Image.open("{0}/ref.equation.bmp".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_numbers(self):
        sam = simply_animate_math.SimplyAnimateMath()
        sam.create_background()
        sam.draw_numbers(("N1n1.jpg", "N1n1.jpg", "N1n1.jpg"))
        new_img = Image.open("/tmp/numbers.bmp")
        ref_img = Image.open("{0}/ref.numbers.bmp".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_operator(self):
        sam = simply_animate_math.SimplyAnimateMath()
        sam.create_background()
        sam.draw_operator("plus.jpg")
        new_img = Image.open("/tmp/operator.bmp")
        ref_img = Image.open("{0}/ref.operator.bmp".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)

    def test_draw_equal(self):
        sam = simply_animate_math.SimplyAnimateMath()
        sam.create_background()
        sam.draw_equal("equal.jpg")
        new_img = Image.open("/tmp/equal.bmp")
        ref_img = Image.open("{0}/ref.equal.bmp".format(self.ref_dir))
        diff = ImageChops.difference(new_img, ref_img).getbbox()
        self.assertTrue(diff is None)


if __name__ == '__main__':
    nose.runmodule()
