import pyglet
import pickle
import gzip
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(2)

class Map():
    def __init__(self, batch=None, name="NULL"):
        bkgnd = pyglet.image.load('background.png')
        self.tiles = pyglet.image.ImageGrid(bkgnd, 10,10)
        if name == "NULL":
            self.x=20
            self.y=20
            self.tileval=[]
            self.block=[]
            self.batch=batch
            #self.objects=[]
            self.sprite=[]
            for i in range(self.x): #Default to grass
                self.tileval.append([])
                self.block.append([])
                for j in range(self.y):
                    self.tileval[i].append(84)
                    self.block[i].append(False)
            self.updateSprite()
        else:
            self.load(name)

    def save(self, name):
        #file = gzip.GzipFile(name, 'wb')
        #file.write(self.x)
        #file.write(self.y)
        #file.write(pickle.dumps(self.tileval, 0))
        #file.close()
        #end(base64.encodestring(open(enemies['name'][x]+'.gif','rb').read()))
        pickle.dump(self.tileval, gzip.open(name+".map", "wb"))

    def load(self, name):
        """
        file = gzip.GzipFile(name, 'rb')
        buffer = ""
        self.x = file.readline()
        self.y = file.readline()
        while True:
            data = file.read()
            if data == "":
                break
            buffer += data
        self.tileval = buffer
        file.close()
        """
        self.tileval = pickle.load(gzip.open(name+".map", "rb"))
        self.x = len(self.tileval)
        if self.x > 0:
            self.y = len(self.tileval[0])

    def updateSprite(self):
        self.sprite=[]
        for i in range(self.x):
            self.sprite.append([])
            for j in range(self.y):
                self.sprite[i].append(pyglet.sprite.Sprite(self.tiles[self.tileval[i][j]], batch=self.batch, group=background,x=i*16,y=j*16))

    def tileWrite(self, x,y,num):
        self.tileval[x][y] = num
        self.sprite[x][y].image = self.tiles[num]

if __name__ == "__main__":
    win = pyglet.window.Window()
    batch=pyglet.graphics.Batch()
    test = Map()
    @win.event
    def on_draw():
        win.clear()
        batch.draw()
    pyglet.app.run()
