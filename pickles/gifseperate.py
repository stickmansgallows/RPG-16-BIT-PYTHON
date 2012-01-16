def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

from PIL import Image

im = Image.open('Terra.gif')
transparency = im.info['transparency']
im.save('test1.png', transparency=transparency)

im.seek(im.tell()+1)
transparency = im.info['transparency']
im.save('test2.png', transparency=transparency)

for i, frame in enumerate(iter_frames(im)):
    frame.save('text%d.png' % i,**frame.info)