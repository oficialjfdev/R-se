import pygame
from moviepy.editor import *
from moviepy.video.fx.resize import *

class Fase:
    def __init__(self):
        self.audio_espinho = pygame.mixer.Sound('audio/Efeito/FLORESTA/ESPINHO.wav')
        self.audio_piso_pulo = pygame.mixer.Sound('audio/Efeito/FLORESTA/PISANDO_PULO_FLORESTA.wav')
        self.audio_tiro_lesma = pygame.mixer.Sound('audio/Efeito/LESMA/LESMA_ATAQUE.wav')
        self.audio_morte_lesma = pygame.mixer.Sound('audio/Efeito/LESMA/LESMA_MORRE.wav')
        self.audio_pisado_lesma = pygame.mixer.Sound('audio/Efeito/LESMA/LESMA_SENDO_PISADA.wav')
        self.audio_morte_corvo = pygame.mixer.Sound('audio/Efeito/CORVOS/CORVO_MORRE.wav')
        self.audio_ataque_corvo = pygame.mixer.Sound('audio/Efeito/CORVOS/CORVO_ATAQUE_1.wav')

        self.audio_ataque_BOSS = pygame.mixer.Sound('audio/Efeito/BOSS/BOSS_ATAQUE.wav')
        self.audio_dano_BOSS = pygame.mixer.Sound('audio/Efeito/BOSS/BOSS_ATINGIDO.wav')

        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, 'img')
        self.level = 1

        self.fade = pygame.Surface((978,550))
        self.fade.fill((0,0,0))
        self.fade.set_alpha(0)
        self.alpha = 0
        self.alpha_inicio = 300
        self.tremendo = [0,0]

        self.sombra = pygame.image.load('img/sombra.png').convert_alpha()
        self.sombra_rect = 0

        self.gameover = True
        self.status_gameover = 1
        self.fim = []
        self.cutscene_fase_3 = 0
        self.plataforma = []
        self.plataforma_flutuante = []
        self.plataforma_espinho = []
        self.limite_lesmaE = []
        self.limite_lesmaD = []
        self.camera = [0,0]
        self.chao1 = pygame.image.load('img/chao1.png').convert_alpha()
        self.chao2 = pygame.image.load('img/chao2.png').convert_alpha()
        self.chao3 = pygame.image.load('img/chao3.png').convert_alpha()
        self.chao_caverna = pygame.image.load('img/chao_caverna.png').convert_alpha()
        self.frente_caverna = pygame.image.load('img/frente_caverna.png').convert_alpha()
        self.poco = pygame.image.load('img/poco.png').convert_alpha()
        self.espinho = pygame.image.load('img/espinho.png').convert_alpha()
        self.fundo1 = pygame.image.load('img/fundo1_arvores.png').convert_alpha()
        self.fundo2 = pygame.image.load('img/fundo2_montanha.png').convert_alpha()
        self.tiles_fase1 = [['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '0', '0', '2', '2', '0', '0', '0', '5e', '0', '0', '0', '0', '9', '0', '0', '0', '5d', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '8', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '3', '0', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'FIM', '11', '4'],
                           ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
        self.tiles_fase2 = [['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5e', '0', '0', '9', '0', '0', '5d', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '10', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '2', '0', '5e', '0', '0', '9', '0', '5d', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '8', '0', '0', '0', '0', '0', '2', '2', '2', '0', '2', '2', '2', '0', '0', '2', '2', '2', '0', '0', '2', '2', '2', '2', '0', '0', '0', '0', '2', '2', '2', '2', '0', '0', '2', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '2', '2', '2', '2', '0', '0', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '0', '3', '3', '0', '0', '3', '3', '0', '0', '0', '0', '0', '0', '0', '0', 'FIM', '12', '4'],
                           ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
        self.tiles_fase3 = [['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '0', '0', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '2', '2', '2', '2', '0', '0', '2', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', 'c', '13', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0', '3', '3', '3', '3', '3', '3', '3', '3', '3', '3', '0', '0', '0', '3', '3', '3', '0', '0', '0', '0', '0', '0', '0', '1p', 'p', '1p', '4'],
                           ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'FIM', '1', '1'],
                           ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
        self.tiles_fase4 = [['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0','4'],
                           ['4', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4'],
                           ['4', '0', '0', '0', '0', 'BOSS', '0', '0', '0', '0', '0', '0', '4'],
                           ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]        
        self.ib = pygame.image.load('img/ib.png').convert_alpha()
        self.shoiti = pygame.image.load('img/shoiti.png').convert_alpha()
        self.jhow = pygame.image.load('img/jhow.png').convert_alpha()
        plataforma1 = pygame.image.load('img/plataforma1.png').convert_alpha()
        self.plataforma1_tiles = [plataforma1.subsurface(pygame.Rect((0, 0), (100, 100))),
                                plataforma1.subsurface(pygame.Rect((100, 0), (100, 100))),
                                plataforma1.subsurface(pygame.Rect((200, 0), (100, 100)))] 
        plataforma2 = pygame.image.load('img/plataforma2.png').convert_alpha()
        self.plataforma2_tiles = [plataforma2.subsurface(pygame.Rect((0, 0), (100, 200))),
                                plataforma2.subsurface(pygame.Rect((100, 0), (100, 200))),
                                plataforma2.subsurface(pygame.Rect((200, 0), (100, 200)))] 
        plataforma3 = pygame.image.load('img/plataforma3.png').convert_alpha()
        self.plataforma3_tiles = [plataforma3.subsurface(pygame.Rect((0, 0), (100, 300))),
                                plataforma3.subsurface(pygame.Rect((100, 0), (100, 300))),
                                plataforma3.subsurface(pygame.Rect((200, 0), (100, 300)))] 
        self.amarelado = pygame.image.load('img/amarelado.png').convert_alpha()
        # 1 = chão
        # 2 = plataforma
        # 3 = espinho
        # 4 = limite da tela
        # 5e = limite para inimigos esquerda
        # 5d = limite para inimigos direita
        # 6 = plataforma canto esquerdo
        # 7 = plataforma canto direito
        # 8 = spawn jogador
        # 9 = spawn lesma 
        # 10 = spawn corvo
        # 11 = npc ib
        # 12 = npc sh
        # 13 = npc jh
        # c = cena fase 3
        # p = poço

        self.cutscene2 = VideoFileClip('CUTSCENE_2.mp4')
        self.cutscene3 = VideoFileClip('CUTSCENE_3.mp4')
        self.cutscene4 = VideoFileClip('CUTSCENE_4.mp4')
        self.cutscene5 = VideoFileClip('CUTSCENE_5.mp4')
        self.cutscene6 = VideoFileClip('CUTSCENE_6.mp4')
        self.cutscene4_titulo = VideoFileClip('CAPITULO_4_TITULO.mp4')
        self.cutscene_tran = VideoFileClip('CUTSCENE_TRAN.mp4')
class Fase2:
    def __init__(self):
        self.mapa = 0
class Fase3:
    def __init__(self):
        self.mapa = 0
class Fase4:
    def __init__(self):
        self.mapa = 0
