from PIL import Image, ImageFilter

img = Image.open('./Pokadex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
# filtered_img.show()
crooked = filtered_img.rotate(180)
crooked.save('grey.png', 'png')

resize = filtered_img.resize((300, 300))
resize.save('grey.png', 'png')

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')
