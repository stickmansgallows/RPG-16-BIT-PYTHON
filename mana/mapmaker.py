import pyglet
import landmap
from pyglet.window import mouse
    
if __name__ == "__main__":
    mainwin = pyglet.window.Window()
    tilewin = pyglet.window.Window()
    mainbatch=pyglet.graphics.Batch()
    sidebatch=pyglet.graphics.Batch()
    test = landmap.Map(mainbatch)
    TILE_SIZE=16
    choice=0
    choosing = []
    for i in range(10):
        for j in range(10):
            choosing.append(pyglet.sprite.Sprite(test.tiles[j*10+i], batch=sidebatch,x=i*16,y=j*16))

    
    @mainwin.event
    def on_draw():
        mainwin.clear()
        mainbatch.draw()
        
    @mainwin.event
    def on_mouse_press(x,y,button,modifiers):
        test.tileWrite(x//16,y//16,choice)

    @mainwin.event
    def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
        if buttons & mouse.LEFT:
            test.tileWrite(x//16,y//16,choice)

    @tilewin.event
    def on_draw():
        tilewin.clear()
        sidebatch.draw()

    @tilewin.event
    def on_mouse_press(x,y,button,modifiers):
        global choice
        choice = (y//16)*10+(x//16)
        print(choice)
    pyglet.app.run()

