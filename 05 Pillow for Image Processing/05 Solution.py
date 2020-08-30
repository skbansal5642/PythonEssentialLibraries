from PIL import Image
import glob
import os

# define the size of thumbnail image
thumbsize = (128,128)

images = glob.glob("ImagesArchieve/*.*")
for image in images:
    if image.endswith(".jpeg") or image.endswith(".png") or image.endswith(".gif") or image.endswith(".jpg"):
        fn = os.path.basename(image)
        fileName, ext = os.path.splitext(fn)
        with Image.open(image) as imgfile:
            imgfile.thumbnail(thumbsize)
            imgfile.save("ImagesArchieve/" + fileName + ".thumb" + ext)