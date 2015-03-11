from bunch import Bunch
import config

width = config.width
height = config.height

# The first number scales the photo. The second shifts x, third shifts y.
photo_type = Bunch()
photo_type.equation = (0.8, 0.1, 0)
photo_type.operator = (0.145, 0.2, 0.49)
photo_type.equal = (0.145, 0.2, 0.77)

def thumb_info(im_size, rescale):
    """Calculate the size for a thumb_name."""

    new_width = int(rescale * width)
    new_height = int(new_width * im_size[1] / im_size[0])
    return (new_width, new_height)


def box_info(im_size, thumb_size, x_scale, y_scale):
    """Calculate the box based on image, thumb_size, and shifts."""

    x_shift = int(x_scale * width)
    y_shift = int(y_scale * height)
    return (x_shift, y_shift, x_shift + thumb_size[0], y_shift + thumb_size[1])


def thumb_box_info(type, im_size):
    """Numbers needed to rescale and place a photo."""

    thumb = thumb_info(im_size, photo_type[type][0])
    box = box_info(im_size, thumb, photo_type[type][1], photo_type[type][2])
    return {"thumb":thumb, "box":box}


def number_info(im_size, i):
    """Calculate the thumbnail dimensions and box location."""

    y_scale = (0.16666, 0.44166, 0.71666)
    thumb = thumb_info(im_size, 0.25)
    box = box_info(im_size, thumb, 0.375, y_scale[i])
    return {"thumb":thumb, "box":box}



#eq_width = int(8 * width / 10)
#eq_height = int(3 * height / 10)
#eq_box = (0, 0, eq_width, eq_height)

plane = Bunch()
plane.line = Bunch()
plane.line.pos = (int(width / 3), int(height * .703), \
        int(width * 2 / 3), int(height * .703 ))
plane.line.color = "#000000"
plane.line.width = 4
