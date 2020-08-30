from PIL import Image

# TODO: read an image an examine some basic attributes using the Image class
image = Image.open("ImagesArchieve/Data.png")
# print(image.filename)
# print(image.format)
# print(image.size)
# print(image.height)
# print(image.width)
# print(image.mode)
# for k, v in image.info.items():
#     print(f"key: {k}, value: {v}")

# TODO: use the save function to convert an image to a new type
# outfile = "ImagesArchieve/Data.png"
# image.save(outfile, "JPEG")
# with Image.open(outfile) as im:
#     print(f"\nImage Format: {im.format}")

# TODO: show the image using platform viewer app
image.show()