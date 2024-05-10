from PIL import Image
a = {'Новый год':'img4.jpg', 'День Победы':'img.jpg1', 'Международный женский день':'img2.jpg','День защитника Отечества':'img3.jpg'}
b = input("введите праздник ")
if b in a:
    c = a[b]
    c = Image.open(c)
print(c.show())