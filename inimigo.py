import pygame

class Inimigo_corvo:
    def __init__(self):
        self.frame = 0
        self.frame_atual_andando = 0
        self.frame_atual_ataque = 0
        self.frame_atual_morrendo = 0
        self.morte = False
        self.flutuando = 0
        self.flutuando_direcao = True
        self.audio_noloop = True

        spritesheet = pygame.image.load('img/spritesheet_corvo.png').convert_alpha()

        # frames andando
        self.andando_direita = [spritesheet.subsurface(pygame.Rect((0, 0), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*1, 0), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*2, 0), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*3, 0), (116, 80)))]
        self.andando_esquerda = []
        for sprite in self.andando_direita:
            self.andando_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frames ataque
        self.ataque_direita = [spritesheet.subsurface(pygame.Rect((116*4, 0), (116, 80))),
                            spritesheet.subsurface(pygame.Rect((116*5, 0), (116, 80))),
                            spritesheet.subsurface(pygame.Rect((116*6, 0), (116, 80)))]
        self.ataque_esquerda = []
        for sprite in self.ataque_direita:
            self.ataque_esquerda.append(pygame.transform.flip(sprite, True, False))
        
        # frames morrendo
        self.morrendo_direita = [spritesheet.subsurface(pygame.Rect((116*0, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*1, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*2, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*3, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*4, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*5, 80), (116, 80))),
                                spritesheet.subsurface(pygame.Rect((116*6, 80), (116, 80)))]
        self.morrendo_esquerda = []
        for sprite in self.morrendo_direita:
            self.morrendo_esquerda.append(pygame.transform.flip(sprite, True, False))

class Inimigo_lesma:
    def __init__(self):
        self.frame_atual_andando = 0
        self.frame_atual_bola = 0
        self.frame_atual_morrendo = 0
        self.morte = False
        self.frame = 0
        self.frame_bala = 0
        self.limite = 0

        self.bala = []
        self.bala_direcao = True
        self.bala_tempo = 0
        self.tempo_direcao = 0
        self.direcao = True


        spritesheet = pygame.image.load('img/spritesheet_lesma.png').convert_alpha()

        # frames andando
        self.andando_direita = [spritesheet.subsurface(pygame.Rect((102*0, 0), (102, 75))),
                            spritesheet.subsurface(pygame.Rect((102*1, 0), (102, 75))),
                            spritesheet.subsurface(pygame.Rect((102*2, 0), (102, 75)))]
        self.andando_esquerda = []
        for sprite in self.andando_direita:
            self.andando_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frames bola
        self.bola_direita = [spritesheet.subsurface(pygame.Rect((102*3, 0), (102, 75))),
                            spritesheet.subsurface(pygame.Rect((102*4, 0), (102, 75))),
                            spritesheet.subsurface(pygame.Rect((102*5, 0), (102, 75)))]
        self.bola_esquerda = []
        for sprite in self.bola_direita:
            self.bola_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frames morrendo
        self.morrendo_direita = [spritesheet.subsurface(pygame.Rect((102*0, 75), (102, 75))),
                                spritesheet.subsurface(pygame.Rect((102*1, 75), (102, 75))),
                                spritesheet.subsurface(pygame.Rect((102*2, 75), (102, 75))),
                                spritesheet.subsurface(pygame.Rect((102*3, 75), (102, 75))),
                                spritesheet.subsurface(pygame.Rect((102*4, 75), (102, 75))),
                                spritesheet.subsurface(pygame.Rect((102*5, 75), (102, 75)))]
        self.morrendo_esquerda = []
        for sprite in self.morrendo_direita:
            self.morrendo_esquerda.append(pygame.transform.flip(sprite, True, False))

class BOSS:
    def __init__(self):

        spritesheet = pygame.image.load('img/spritesheet_boss.png').convert_alpha()
        self.vida = 3

        coracao_img = pygame.image.load('img/life_boss.png').convert_alpha()
        self.coracao = [coracao_img.subsurface(pygame.Rect((0, 0), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 25), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 50), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 75), (85, 25)))]

        self.flut = 0
        self.flut_direcao = True

        self.rect = 0
        self.direcao = True
        self.flutuando_direcao = True
        self.cansado = False
        self.cansado_tempo = 0
        self.atira = False
        self.atira_quantidade = 0
        self.pedras = [0,0,0]
        self.pedras_quebra = False

        self.dano = False
        self.dano_cooldown = 10

        self.cooldown = 10
        self.atira_tempo = 0

        self.frame_atual_levantando = 0
        self.frame_atual_pousando = 0
        self.frame_atual_cansado = 0
        self.frame_parado = False
        self.pousado = False
        self.levantado = False
        # frame pedra
        self.img_pedra = pygame.image.load('img/pedra.png').convert_alpha()
        # frames levantando
        self.levantando_esquerda = [spritesheet.subsurface(pygame.Rect((137*0, 0), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*1, 0), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*2, 0), (137, 196)))]
        self.levantando_direita = []
        for sprite in self.levantando_esquerda:
            self.levantando_direita.append(pygame.transform.flip(sprite, True, False))
        # frames pousando
        self.pousando_esquerda = [spritesheet.subsurface(pygame.Rect((137*2, 0), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*1, 0), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*0, 0), (137, 196)))]
        self.pousando_direita = []
        for sprite in self.pousando_esquerda:
            self.pousando_direita.append(pygame.transform.flip(sprite, True, False))
        
        # frame frutuando 
        self.flutuando_esquerda = spritesheet.subsurface(pygame.Rect((137*2, 0), (137, 196)))
        self.flutuando_direita = pygame.transform.flip(self.flutuando_esquerda, True, False)
        
        # frames atirando
        self.atirando_esquerda = [spritesheet.subsurface(pygame.Rect((137*0, 196), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*1, 196), (137, 196)))]
        self.atirando_direita = []
        for sprite in self.atirando_esquerda:
            self.atirando_direita.append(pygame.transform.flip(sprite, True, False))

        # frames dano
        self.dano_esquerda = spritesheet.subsurface(pygame.Rect((137*2, 196), (137, 196)))
        self.dano_direita = pygame.transform.flip(self.dano_esquerda, True, False)

        # frames cansado
        self.cansado_esquerda = [spritesheet.subsurface(pygame.Rect((137*0, 2*196), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*1, 2*196), (137, 196))),
                                spritesheet.subsurface(pygame.Rect((137*2, 2*196), (137, 196)))]
        self.cansado_direita = []
        for sprite in self.cansado_esquerda:
            self.cansado_direita.append(pygame.transform.flip(sprite, True, False))
       

        