from bunch import Bunch
import config

width = config.width
height = config.height

def equation_info(im_size):
    """Calculate the thumbnail dimensions and box location."""

    rescale = 0.8
    new_width = int(rescale * width)
    new_height = int(new_width * im_size[1] / im_size[0])
    x_shift = int(0.1 * width)
    info = {}
    info["thumb"] = (new_width, new_height)
    info["box"] = (x_shift, 0, x_shift + new_width, new_height)
    return info

def number_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    rescale = 0.25
    new_width = int(rescale * width)
    new_height = int(new_width * im_size[1] / im_size[0])
    x_shift = int(0.5 * width - new_width / 2)
    info = {}
    info["thumb"] = (new_width, new_height)
    info["box"] = (x_shift, int(new_height / 1.5 + i * new_height * 1.1), x_shift + new_width, int(new_height + new_height / 1.5 + i * new_height * 1.1))
    return info

def operator_info(im_size):
    """Calculate the thumbnail dimensions and box location."""

    rescale = 0.145
    new_width = int(rescale * width)
    new_height = int(new_width * im_size[1] / im_size[0])
    x_shift = int(0.2 * width)
    info = {}
    info["thumb"] = (new_width, new_height)
    y_shift = width * 0.49
    info["box"] = (x_shift, int(y_shift), x_shift + new_width, int(new_height + y_shift))
    return info

def equal_info(im_size):
    """Calculate the thumbnail dimensions and box location."""

    rescale = 0.145
    new_width = int(rescale * width)
    new_height = int(new_width * im_size[1] / im_size[0])
    x_shift = int(0.2 * width)
    info = {}
    info["thumb"] = (new_width, new_height)
    y_shift = height * 0.77
    info["box"] = (x_shift, int(y_shift), x_shift + new_width, int(new_height + y_shift))
    return info

eq_width = int(8 * width / 10)
eq_height = int(3 * height / 10)
eq_box = (0, 0, eq_width, eq_height)

plane = Bunch()
plane.line = Bunch()
plane.line.pos = (int(width / 3), int(height * .703), \
        int(width * 2 / 3), int(height * .703 ))
plane.line.color = "#000000"
plane.line.width = 4
