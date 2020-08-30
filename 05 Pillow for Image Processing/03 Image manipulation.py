from PIL import Image, ImageFilter, ImageOps

# TODO: use the crop function to crop the image
infile = "ImagesArchieve/Connections.jpeg"
# with Image.open(infile) as img:
#     midx = img.width/2
#     midy = img.height/2
#     croparea = (midy-400, midx-250, midy+400, midx+250)
#     cropimg = img.crop(croparea)
#     cropimg.show()

#TODO: perform a simple resize and rotation
# with Image.open(infile) as img:
#     newimg = img.resize((256,256))
#     newimg = newimg.rotate(45)
#     newimg.show()

# TODO: use the transpose function with a built-in operation
# with Image.open(infile) as img:
#     newimg = img.transpose(Image.FLIP_TOP_BOTTOM)
#     newimg.show()

# TODO: use an image filter operation
# with Image.open(infile) as img:
#      newimg = img.filter(ImageFilter.GaussianBlur(20))
#      newimg.show()

# TODO: use ImageOps for built-in image processing
with Image.open(infile) as img:
    newimg = ImageOps.grayscale(img)
    newimg.show()