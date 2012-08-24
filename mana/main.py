import pyglet
import movement
import landmap

win = pyglet.window.Window()
batch=pyglet.graphics.Batch()

@win.event
def on_draw():
    win.clear()
    batch.draw()

def update(dt):
    randi.update(dt)


 


if __name__ == "__main__":
    SPEED=100
    randi = movement.Player('randimove.png',batch)
    potos = landmap.Map(batch)
    for i in randi.event_handlers:
        win.push_handlers(i)
    
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()
