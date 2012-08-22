import pyglet
key=pyglet.window.key
win = pyglet.window.Window()

class Player():
    def __init__(self, spritesheet):
        sheet = pyglet.image.load(spritesheet)
        sheet._get_gl_format_and_type
        self.images = pyglet.image.ImageGrid(sheet, 3, 7)
        self.animation=[]
        for i in range(3):
            self.animation.append(pyglet.image.Animation.from_image_sequence(self.images[1+7*i:7*i+7], 0.1))
        self.animation.append(self.animation[0].get_transform(flip_x=True))
        self.sprite = pyglet.sprite.Sprite(self.animation[0])
        self.sprite.scale=2
        self.sprite.rotation=0
        self.sprite.y=50

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        if self.key_handler[key.RIGHT]:
            self.sprite.image = self.animation[0]
            self.sprite.x += dt * SPEED
        elif self.key_handler[key.LEFT]:
            self.sprite.image = self.animation[3]
            self.sprite.x -= dt * SPEED
        if self.key_handler[key.UP]:
            self.sprite.image = self.animation[1]
            self.sprite.y += dt * SPEED
        elif self.key_handler[key.DOWN]:
            self.sprite.image = self.animation[2]
            self.sprite.y -= dt * SPEED

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.sprite.image = self.animation[5]
            print("HI")
        





@win.event
def on_draw():
    win.clear()
    randi.sprite.draw()

def update(dt):
    randi.update(dt)


 


if __name__ == "__main__":
    # Start it up!
    SPEED=100
    randi = Player('randimove.png')
    
    #keyboard = key.KeyStateHandler()
    #win.push_handlers(keyboard)
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1/60.0)
    
    # Tell pyglet to do its thing
    pyglet.app.run()

