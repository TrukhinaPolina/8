from PIL import Image, ImageDraw, ImageFont

aaa = Image.open('aaa.jpg')
draw = ImageDraw.Draw(aaa)
font = ImageFont.truetype("ofont.ru_Rubik.ttf", 50)
b = input(" кого хочет поздравить ")
c = b + ' , поздравляю!'

draw.text((50, 790), c, (185, 20, 110), font=font)
# cropped.save('aaa.png')
aaa.show()