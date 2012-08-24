import pyglet
from pyglet.window import key

SPEED=100
midground = pyglet.graphics.OrderedGroup(1)

class Player():
    def __init__(self, spritesheet, batch=None):
        sheet = pyglet.image.load(spritesheet)
        sheet._get_gl_format_and_type
        self.images = pyglet.image.ImageGrid(sheet, 4, 7)
        self.animation=[]
        self.batch=batch
        for i in range(4):
            self.animation.append(pyglet.image.Animation.from_image_sequence(self.images[1+7*i:7*i+7], 0.1))
        self.sprite = pyglet.sprite.Sprite(self.animation[0], batch=self.batch, group=midground)
        self.sprite.scale=1
        self.sprite.rotation=0
        self.sprite.y=50
        

        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        if self.key_handler[key.RIGHT]:
            self.sprite.x += dt * SPEED
            if not self.vert(dt):
                self.setOnce(1)
        elif self.key_handler[key.LEFT]:
            self.sprite.x -= dt * SPEED
            if not self.vert(dt):
                self.setOnce(0)
        else:
            self.vert(dt)
            
        if (not self.key_handler[key.RIGHT] and not self.key_handler[key.LEFT] and not self.key_handler[key.UP] and not self.key_handler[key.DOWN]):
            for i in range(4):
                if self.sprite.image == self.animation[i]:
                    self.sprite.image = self.images[i*7]
                    break


    def on_key_press(self, symbol, modifiers):
        pass
        
    def on_key_release(self, symbol, modifiers):
        pass

    def setOnce(self, a):
        if self.sprite.image != self.animation[a]:
            self.sprite.image = self.animation[a]

    def vert(self, dt):
        if self.key_handler[key.UP]:
            self.sprite.y += dt * SPEED
            self.setOnce(2)
        elif self.key_handler[key.DOWN]:
            self.sprite.y -= dt * SPEED
            self.setOnce(3)
        else:
            return False
        return True

if __name__ == "__main__":
    win = pyglet.window.Window()
    batch=pyglet.graphics.Batch()
