from obj import Obj, Player, Texto
import random

class Game:

    def __init__(self):
        
        self.bg = Obj("assets/background.jpg", 0, 0)
        self.bg2 = Obj("assets/background.jpg", 0, -640)

        self.ekans = Obj("assets/ekans1.png", random.randrange(150, 330), -50)
        self.code = Obj("assets/profa_silvana.jpg", random.randrange(0, 330), -50)
        self.pdf = Obj("assets/professor_lidiano.jpg", random.randrange(0, 330), -50)
        self.carro = Obj("assets/professor_cleyton.png", random.randrange(0, 130), -50)
        self.player = Player("assets/boneco1.png", 150, 570)

        self.change_scene = False
        self.scene_type = None

        self.score = Texto(120, "0")
        self.vidas = Texto(60, "4")

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)
        self.ekans.drawing(window)
        self.code.drawing(window)
        self.pdf.drawing(window)
        self.carro.drawing(window)
        self.player.drawing(window)
        self.score.draw(window, 150, 50)
        self.vidas.draw(window, 50, 50)

    def update(self):
        self.ekans.anima("ekans", 8, 4)
        self.player.anima("boneco", 8, 4)
        self.move_bg()
        self.move_ekans()
        self.move_code()
        self.move_pdf()
        self.move_carro()
        self.player.colisao(self.ekans.group, "Ekans")
        self.player.colisao(self.carro.group, "Carro")
        self.player.colisao(self.pdf.group, "Pdf")
        self.player.colisao(self.code.group, "Code")
        self.game_over()
        self.winner()
        self.score.update_texto(str(self.player.pts))
        self.vidas.update_texto(str(self.player.vida))

    def move_bg(self):
        self.bg.sprite.rect[1] += 2
        self.bg2.sprite.rect[1] += 2

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_ekans(self):
        self.ekans.sprite.rect[1] += 10

        if self.ekans.sprite.rect[1] >= 700:
            self.ekans.sprite.kill()
            self.ekans = Obj("assets/ekans1.png", random.randrange(150, 330), -50)

    def move_code(self):
        self.code.sprite.rect[1] += 8

        if self.code.sprite.rect[1] >= 700:
            self.code.sprite.kill()
            self.code = Obj("assets/profa_silvana.jpg", random.randrange(0, 330), -50)

    def move_pdf(self):
        self.pdf.sprite.rect[1] += 8

        if self.pdf.sprite.rect[1] >= 700:
            self.pdf.sprite.kill()
            self.pdf = Obj("assets/professor_lidiano.jpg", random.randrange(0, 330), -50)

    def move_carro(self):
        self.carro.sprite.rect[1] += 13

        if self.carro.sprite.rect[1] >= 700:
            self.carro.sprite.kill()
            self.carro = Obj("assets/professor_cleyton.png", random.randrange(0, 130), -50)

    def game_over(self):
        if self.player.vida <= 0:
            self.change_scene = True
            self.scene_type = "gameover"

    def winner(self):
        if self.player.pts >= 10:
            self.change_scene = True
            self.scene_type = "win"