from PIL import Image, ImageDraw, ImageFont

infile = 'ImagesArchieve/Connections.jpeg'

#TODO: use the image draw routines to modify an image
# with Image.open(infile) as img:
#     draw = ImageDraw.Draw(img)
#     draw.line((0,0) + img.size, width=40, fill=128)
#     draw.line((0, img.size[1], img.size[0], 0), width=40, fill=128)
#     img.show()

# TODO: use the ImageDraw routines to modify an image
with Image.open(infile) as img:
    draw = ImageDraw.Draw(img)
    textStr = "This is random text"
    txtFont = ImageFont.truetype("arial.ttf", 75)
    txtSize = draw.textsize(textStr, font=txtFont)
    location = (20, img.height - txtSize[1])
    draw.text(location, textStr, (255, 255, 255), font= txtFont)
    img.show()