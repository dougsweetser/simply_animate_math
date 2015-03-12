from bunch import Bunch
import config

width = config.width
height = config.height

# The first number scales the photo. The second shifts x, third shifts y.
photo_type = Bunch()
photo_type.equation = (0.175, 0.1, 0)
photo_type.operator = (0.145, 0.15, 0.49)
photo_type.equal = (0.145, 0.15, 0.77)

def thumb_info(im_size, rescale):
    """Calculate the size for a thumb_name, rescaling by height"""

    new_height = int(rescale * height)
    new_width = int(new_height * im_size[0] / im_size[1])
    return (new_width, new_height)


def box_info(im_size, thumb_size, x_scale, y_scale):
    """Calculate the box based on image, thumb_size, and shifts."""

    x_shift = int(x_scale * width)
    y_shift = int(y_scale * height)
    return [x_shift, y_shift, x_shift + thumb_size[0], y_shift + thumb_size[1]]


def thumb_box_info(type, im_size):
    """Numbers needed to rescale and place a photo."""

    thumb = thumb_info(im_size, photo_type[type][0])
    box = box_info(im_size, thumb, photo_type[type][1], photo_type[type][2])
    return {"thumb":thumb, "box":box}


def number_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    y_scale = (0.16666, 0.44166, 0.71666)
    thumb = thumb_info(im_size, 0.25)
    box = box_info(im_size, thumb, 0.333, y_scale[i])
    return {"thumb":thumb, "box":box}

def number_2d_1_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    y_scale = (0.16666, 0.44166, 0.71666)
    thumb = thumb_info(im_size, 0.25)
    box = box_info(im_size, thumb, 0.33, y_scale[i])
    return {"thumb":thumb, "box":box}

def number_2d_2_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    new_i = i % 3
    y_scale = (0.16666, 0.44166, 0.71666)
    thumb = thumb_info(im_size, 0.25)
    box = box_info(im_size, thumb, 0.6, y_scale[new_i])
    return {"thumb":thumb, "box":box}


def number_2d_3_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    new_i = i % 3
    y_scale = (0.16666, 0.44166, 0.71666)
    thumb = thumb_info(im_size, 0.25)
    box = box_info(im_size, thumb, 0.70, y_scale[new_i])
    return {"thumb":thumb, "box":box}



plane = Bunch()
plane.line = Bunch()
plane.line.pos = (int(width * 0.331), int(height * .703), \
       int(width * 0.58), int(height * .703 ))
plane.line.color = "#000000"
plane.line.width = 4
plane.line.values = (plane.line.pos, plane.line.color, plane.line.width)

dynamic_1d = Bunch()
dynamic_1d.line = Bunch()
dynamic_1d.line.pos = (int(width * 0.331), int(height * 0.703), \
        int(width * 0.694), int(height * .703 ))
dynamic_1d.line.color = "#000000"
dynamic_1d.line.width = 4
dynamic_1d.line.values = (dynamic_1d.line.pos, dynamic_1d.line.color, dynamic_1d.line.width)

dynamic_3d = Bunch()
dynamic_3d.line = Bunch()
dynamic_3d.line.pos = (int(width * 0.331), int(height * .703), \
        int(width * 0.96), int(height * .703 ))
dynamic_3d.line.color = "#000000"
dynamic_3d.line.width = 4
dynamic_3d.line.values = (dynamic_3d.line.pos, dynamic_3d.line.color, dynamic_3d.line.width)
