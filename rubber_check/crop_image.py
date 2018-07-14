
####Crop_image
x = 100
y = 100
w = 700
h = 700
####

def image_crop(image):
    crop_image = image[y:y+h, x:x+w]
    return  crop_image
