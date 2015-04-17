"""Test photos module."""

import io
import nose
import re
import sys
import unittest

sys.path.insert(0, '..')
import photos

class PhotosTests(unittest.TestCase):
    """Test harness."""

    def setUp(self):
        """Grab print statements."""

        self.output = io.StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        """Reset output."""

        sys.stdout = self.saved_stdout

    def test_get_photos(self):
        """Look at dictionary found."""

        ph_dict = photos.get_photos()
        self.assertTrue("plus.jpg" in ph_dict)

    def test_print_ls(self):
        """Look at dictionary found."""

        photos.print_ls()
        ls_string = self.output.getvalue()
        self.assertTrue(re.search("plus.jpg", ls_string))


if __name__ == '__main__':
    nose.runmodule()
