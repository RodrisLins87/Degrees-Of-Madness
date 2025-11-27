import pygame
from pygame.locals import *
from random import randint
from sys import exit

# =============================
# CLASSE BASE DE TODAS ENTIDADES
# =============================
class Entidade:
    def __init__(self, imagem, x=None, y=None, vel=0):
        self.image = pygame.image.load(imagem)
        self.rect = self.image.get_rect()

        self.rect.x = x if x is not None else randint(0, 900)
        self.rect.y = y if y is not None else 0

        self.vel = vel

    def update(self):
        self.rect.y += self.vel

    def draw(self, tela):
        tela.blit(self.image, (self.rect.x, self.rect.y))

    def reset_if_needed(self, altura, largura):
        if self.rect.y >= altura:
            self.rect.y = 0
            self.rect.x = randint(0, largura)


# =============================
# CLASSE PLAYER
# =============================
class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets_imagem/personagem_v.png")
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel = 10
        self.vida = 100

    def mover(self):
        keys = pygame.key.get_pressed()

        if keys[K_a]:
            self.rect.x -= self.vel
        if keys[K_d]:
            self.rect.x += self.vel
        if keys[K_w]:
            self.rect.y -= self.vel
        if keys[K_s]:
            self.rect.y += self.vel

    def draw(self, tela):
        tela.blit(self.image, (self.rect.x, self.rect.y))


# =============================
# CLASSES ESPECIALIZADAS
# =============================
class Enemy(Entidade):
    pass


class Item(Entidade):
    pass


# =============================
# CLASSE PRINCIPAL DO JOGO
# =============================
class Game:
    def __init__(self):
        pygame.init()

        # Música
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.load('assets/Legião Instrumental.mp3')
        pygame.mixer.music.play(-1)

        self.som_dano = pygame.mixer.Sound('assets/dano.mp3')
        self.som_dano.set_volume(0.1)

        self.som_pontos = pygame.mixer.Sound('assets/pontos.mp3')
        self.som_pontos.set_volume(0.1)

        self.som_vida = pygame.mixer.Sound('assets/som_up_vida.mp3')
        self.som_vida.set_volume(0.1)

        # Tela
        self.largura = 960
        self.altura = 800
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Degree of Madness")

        # Fundo
        self.fundo = pygame.image.load("assets_imagem/background.jpg").convert()

        # Clock
        self.clock = pygame.time.Clock()

        # Player
        self.player = Player(400, 500)

        # Pontos
        self.pontos = 0
        self.font = pygame.font.SysFont('arial', 40, True, False)

        # Obstáculo
        self.obstaculo = Entidade("assets_imagem/diploma.png",
                                  randint(0, 900), randint(0, 700), 0)

        # Inimigos
        self.inimigos = [
            Enemy("assets_imagem/lidiano_v.png", vel=5),
            Enemy("assets_imagem/silvana_V.png", vel=8),
            Enemy("assets_imagem/cleyton_v.png", vel=10)
        ]

        # Item de vida
        self.ficha = Item("assets_imagem/ficha_V.png", vel=8)

    # ---------------------------------------
    # VERIFICAR TODAS AS COLISÕES DO JOGO
    # ---------------------------------------
    def verificar_colisoes(self):
        # Obstáculo da pontuação
        if self.player.rect.colliderect(self.obstaculo.rect):
            self.obstaculo.rect.x = randint(0, 900)
            self.obstaculo.rect.y = randint(0, 700)
            self.pontos += 1
            self.som_pontos.play()

        # Inimigos (tiram vida)
        for inimigo in self.inimigos:
            if self.player.rect.colliderect(inimigo.rect):
                self.player.vida -= 1
                self.som_dano.play()

        # Ficha (aumenta vida)
        if self.player.rect.colliderect(self.ficha.rect):
            if self.player.vida < 100:
                self.player.vida += 10
            self.ficha.rect.y = 0
            self.ficha.rect.x = randint(0, 900)
            self.som_vida.play()

    # ---------------------------------------
    # LOOP PRINCIPAL
    # ---------------------------------------
    def run(self):
        rodando = True

        while rodando:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    rodando = False

            # Movimento do player
            self.player.mover()

            # Atualizar inimigos
            for inimigo in self.inimigos:
                inimigo.update()
                inimigo.reset_if_needed(self.altura, self.largura)

            # Atualizar item de vida
            self.ficha.update()
            self.ficha.reset_if_needed(self.altura, self.largura)

            # Verificar colisões
            self.verificar_colisoes()

            # Desenhar
            self.tela.blit(self.fundo, (0, 0))

            self.player.draw(self.tela)
            self.obstaculo.draw(self.tela)

            for inimigo in self.inimigos:
                inimigo.draw(self.tela)

            self.ficha.draw(self.tela)

            # Texto
            txt = self.font.render(f"Pontos: {self.pontos}", True, (255,255,255))
            vida_txt = self.font.render(f"Vida: {self.player.vida}", True, (255,255,255))

            self.tela.blit(txt, (650, 30))
            self.tela.blit(vida_txt, (150, 30))

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    Game().run()
