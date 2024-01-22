import pygame, sys  # os pacotes do jogo
from jogador import Jogador  # import da classe Jogador
from fase import Fase  # import das classes das fases
from inimigo import BOSS
from fisica import desenhar  # import da classe Desenhar
from moviepy.editor import *
from moviepy.video.fx.resize import *

pygame.display.set_caption('R;SE')
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
janela = pygame.display.set_mode((1280, 720), 0, 32)
display = pygame.Surface((978, 550))
Voce = Jogador()
Fase_Atual = Fase()
Voce_BOSS = BOSS()

cutscene1 = VideoFileClip('CUTSCENE_1.mp4')

start = False
cutscene = True
cutscene_stage = 0

tempo_cutscene = 0

menu = pygame.Surface((1280, 720))

unknown = pygame.image.load('img/Unknown.png').convert_alpha()
aviso = pygame.image.load('img/aviso.png').convert_alpha()
comandos = pygame.image.load('img/comandos.png').convert_alpha()

logo_rise = pygame.image.load('img/logo.png').convert_alpha()
logo_rise_tiles = [logo_rise.subsurface(pygame.Rect((0, 0), (550, 154))),
                    logo_rise.subsurface(pygame.Rect((550, 0), (550, 154))),
                    logo_rise.subsurface(pygame.Rect((1100, 0), (550, 154)))] 
frame_logo = 0

button_jogar_rect = pygame.Rect(565, 500, 150, 65)
button_jogar = pygame.image.load('img/button_jogar.png').convert_alpha()
button_jogar_tiles = [button_jogar.subsurface(pygame.Rect((0, 0), (150, 65))),
                    button_jogar.subsurface(pygame.Rect((150, 0), (150, 65))),
                    button_jogar.subsurface(pygame.Rect((300, 0), (150, 65)))]
frame_jogar = 0


fade_menu = pygame.Surface((1280, 720))
fade_menu.fill((0,0,0))
alpha_fim = 0
alpha_inicio = 300
comeco = True
fim = False
while True:
    if start == False:
        menu.fill((0,0,0))
        if cutscene == True:
            if cutscene_stage == 0:
                if tempo_cutscene == 0:
                    comeco = True
                if tempo_cutscene < 50:
                    menu.blit(unknown,(440,307))
                    tempo_cutscene += 0.5
                    if tempo_cutscene > 39:
                        fim = True
                else:
                    tempo_cutscene = 0
                    cutscene_stage += 1
            elif cutscene_stage == 1:
                if tempo_cutscene == 0:
                    comeco = True
                if tempo_cutscene < 70:
                    menu.blit(aviso,(0,0))
                    tempo_cutscene += 0.2
                    if tempo_cutscene > 65:
                        fim = True
                else:
                    tempo_cutscene = 0
                    cutscene_stage += 1
            elif cutscene_stage == 2:
                if tempo_cutscene == 0:
                    comeco = True
                if tempo_cutscene < 45:
                    menu.blit(comandos,(0,0))
                    tempo_cutscene += 0.2
                    if tempo_cutscene > 40:
                        fim = True
                else:
                    tempo_cutscene = 0
                    cutscene_stage += 1
            elif cutscene_stage == 3:
                cutscene1.preview()
                cutscene_stage += 1
                cutscene = False


            janela.blit(menu,(0,0))

            if comeco == True:
                if alpha_inicio > 0:
                    alpha_inicio -= 10
                    fade_menu.set_alpha(alpha_inicio)
                    janela.blit(fade_menu,(0,0))
                else:
                    alpha_inicio = 300
                    fade_menu.set_alpha(0)
                    janela.blit(fade_menu,(0,0))
                    comeco = False
            if fim == True:
                if alpha_fim < 300:
                    alpha_fim += 10
                    fade_menu.set_alpha(alpha_fim)
                    janela.blit(fade_menu,(0,0))
                else:
                    alpha_fim = 0
                    fade_menu.set_alpha(0)
                    janela.blit(fade_menu,(0,0))
                    fim = False
        else:
            if frame_logo > 2:
                frame_logo = 0
            else:
                frame_logo += 0.3
            menu.blit(logo_rise_tiles[int(frame_logo)],(365,150))

            if button_jogar_rect.collidepoint(pygame.mouse.get_pos()):
                if frame_jogar > 2:
                    frame_jogar = 0
                else:
                    frame_jogar += 0.3
                menu.blit(button_jogar_tiles[int(frame_jogar)],(565,500))
            else:
                menu.blit(button_jogar_tiles[0],(565,500))
            janela.blit(menu,(0,0))

            if comeco == True:
                if alpha_inicio > 0:
                    alpha_inicio -= 10
                    fade_menu.set_alpha(alpha_inicio)
                    janela.blit(fade_menu,(0,0))
                else:
                    alpha_inicio = 300
                    fade_menu.set_alpha(0)
                    janela.blit(fade_menu,(0,0))
                    comeco = False
        

        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1 and button_jogar_rect.collidepoint(pygame.mouse.get_pos()) and cutscene == False:
                    start = True

  
    elif start == True:

        janela.blit(pygame.transform.scale(desenhar(Fase_Atual, Voce, Voce_BOSS), (1280, 720)), (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.KEYUP:
                Voce.movimentacao(evento.type, evento.key)
    
    # janela.blit(pygame.transform.scale(desenhar(Fase_Atual, Voce, Voce_BOSS), (1280, 720)), (0, 0))

    # for evento in pygame.event.get():
    #     if evento.type == pygame.QUIT:
    #         sys.exit()
    #     if evento.type == pygame.KEYDOWN or evento.type == pygame.KEYUP:
    #         Voce.movimentacao(evento.type, evento.key)

    pygame.display.flip()
    pygame.time.Clock().tick(30)
