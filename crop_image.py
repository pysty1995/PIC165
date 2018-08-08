
####Crop_image, default is 800x600
start_col = 100
start_row = 100
end_col = 800
end_row = 800
####

def image_crop(image):
    crop_image = image[start_row:end_row, start_col:end_col]
    return  crop_image
