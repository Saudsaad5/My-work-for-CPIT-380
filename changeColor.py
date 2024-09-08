file = "C:\Users\hason\Pictures\Screenshots\IMG_9644.png"
print(file)
pic = makePicture(file)

def changeAnyCol(pic, col):
    if col == "green":
        for pix in getPixels(pic):
            value = getGreen(pix)
            setGreen(pix, value * 0.5)
            
    elif col == "red":
        for pix in getPixels(pic):
            value = getRed(pix)
            setRed(pix, value * 0.5)
            
    elif col == "blue":
        for pix in getPixels(pic):
            value = getBlue(pix)
            setBlue(pix, value * 0.5)


changeAnyCol(pic,"green")
show(pic)
changeAnyCol(pic,"blue")
show(pic)
changeAnyCol(pic,"red")
show(pic)
