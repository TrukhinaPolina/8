from PIL import Image
image = Image.open('img2.jpg')
cropped = image.crop((0, 0, 853, 900))
cropped.save('aaa.jpg')