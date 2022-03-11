# Pyxelで四角を移動するものを作った
# https://www.lisz-works.com/entry/pyxel-move-rect

import pyxel

class Position:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
    def moveUp(self, amount):
        self.y -= amount
    def moveDown(self, amount):
        self.y += amount
    def moveRight(self, amount):
        self.x += amount
    def moveLeft(self, amount):
        self.x -= amount

class App:
    def __init__(self):
        pyxel.init(160, 120)

        x = pyxel.width / 2
        y = pyxel.height / 2
        self.position = Position(x, y, 5, 5)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_A, 1, 1):
            self.position.moveLeft(1)
        elif pyxel.btnp(pyxel.KEY_D, 1, 1):
            self.position.moveRight(1)
        elif pyxel.btnp(pyxel.KEY_W, 1, 1):
            self.position.moveUp(1)
        elif pyxel.btnp(pyxel.KEY_S, 1, 1):
            self.position.moveDown(1)
        elif pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.position.x, self.position.y, 5, 5, 11)

App()