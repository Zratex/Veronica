from PIL import Image, ImageFont, ImageDraw, ImageEnhance

def drawProgressBar(d,x,y,w,h,progress,bg="gray"):
    #draw background
    d.ellipse((x+w,y,x+h+w,y+h),fill=bg)
    d.ellipse((x, y, x+h, y+h), fill=bg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

    # draw progress bar
    fg=(242,159,11)
    w *= (progress/100)
    d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
    d.ellipse((x, y, x+h, y+h),fill=fg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

    return d

def test(pourcentage:float):
    # create image or load your existing image with out=Image.open(path)
    out = Image.open("Media\LvlBackground.png")
    d = ImageDraw.Draw(out)

    # draw the progress bar to given location, width, progress and color
    d = drawProgressBar(d, 10, 10, 350, 30, pourcentage)
    out.save("output.png")