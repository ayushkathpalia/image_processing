from PIL import Image, ImageFilter


def image_filters():
    img = Image.open('./assets/scenery2.jpg')
    img2 = Image.open('./assets/scenery1.jpeg')
    img3 = Image.open('./assets/man.jpg')

    filtered_img_blur = img.filter(ImageFilter.BLUR)
    filtered_img_blur.save("scenery2_blur.png", 'png')

    filtered_img_smooth = img.filter(ImageFilter.SMOOTH)
    filtered_img_smooth.save("scenery2_smooth.png", 'png')

    filtered_img_greyscale = img2.convert('L')
    filtered_img_greyscale.save("scenery1_greyscale.png", 'png')

    resize_img2 = img2.resize((300, 300))
    resize_img2.save("resize_img2.png", 'png')

    crop_img = img.crop((1, 2, 300, 300))
    crop_img.save("crop_img.png", 'png')

    img3.thumbnail((200,200))
    img3.save('thumbnail_man.jpg')


image_filters()
