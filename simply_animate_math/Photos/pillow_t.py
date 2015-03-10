from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('/Users/doug/Sam/photos/ball_8_10.png').convert('RGBA')

base.show()

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('/Users/doug/Library/Application Support/OpenOffice.org 2.1/user/fonts/TimesNewRoman.ttf', 40)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
# draw text, full opacity
d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

dir(Image)

out = Image.alpha_composite(base, txt)

out.show()
