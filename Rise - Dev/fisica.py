import pygame, random
from inimigo import Inimigo_corvo, Inimigo_lesma, BOSS
from moviepy.editor import *

tela = pygame.Surface((978,550)) 

lesmas_rect = []
lesmas_object = []
lesma_limite = []
corvos_rect = []
corvos_object = []
level_mapa = []
y = 0
def desenhar(fase, jogador, BOSS_obj):
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
    # SPAWN INIMIGOS/JOGADOR
    if fase.level == 1:
        level_mapa = fase.tiles_fase1
    elif fase.level == 2:
        level_mapa = fase.tiles_fase2
    elif fase.level == 3:
        level_mapa = fase.tiles_fase3
    elif fase.level == 4:
        level_mapa = fase.tiles_fase4
    if fase.gameover == True:
        if fase.status_gameover == 1:
            if fase.level == 4:
                pygame.mixer.music.load('audio/Efeito/CAVERNA/AMBIENTE_CAVERNA_BOSS.mp3')
            else:
                pygame.mixer.music.load('audio/Efeito/FLORESTA/AMBIENTE_FLORESTA.wav')
            pygame.mixer.music.play(-1)
            lesmas_rect.clear()
            lesmas_object.clear()
            lesma_limite.clear()
            corvos_rect.clear()
            corvos_object.clear()
            jogador.mover[0] = 0
            jogador.mover_esquerda = False
            jogador.mover_direita = False
            jogador.mover_agachar = False
            jogador.mover_descer = False
            jogador.mover_ataqueX = False
            jogador.mover_ataqueZ = False
            y = 0
            for layer in level_mapa:
                x = 0
                for tile in layer:
                    if tile == '5':
                        lesma_limite.append(pygame.Rect(x*100, y*100, 100, 100))
                    if tile == '8':
                        jogador.jogador_rect.x = x*100
                        jogador.jogador_rect.y = y*100
                    if tile == '9':
                        lesmas_rect.append(pygame.Rect(x*100, y*100, 102, 75))
                        lesmas_object.append(Inimigo_lesma())
                    if tile == '10':
                        corvos_rect.append(pygame.Rect(x*100, y*100, 116, 80))
                        corvos_object.append(Inimigo_corvo())
                    if tile == 'c':
                        fase.cutscene_fase_3 = pygame.Rect(x*100, 0, 100, 700)
                    if tile == 'BOSS':
                        BOSS_obj.rect = pygame.Rect(x*100, (y-1)*100+3, 137, 196)
                    x += 1
                y += 1
        elif fase.status_gameover == 2:
            pygame.mixer.music.load('audio/Músicas Originais/03 - Alone in the room.wav')
            pygame.mixer.music.play(-1)
            lesmas_rect.clear()
            lesmas_object.clear()
            lesma_limite.clear()
            corvos_rect.clear()
            corvos_object.clear()
            jogador.mover[0] = 0
            jogador.mover_esquerda = False
            jogador.mover_direita = False
            jogador.mover_agachar = False
            jogador.mover_descer = False
            jogador.mover_ataqueX = False
            jogador.mover_ataqueZ = False
            y = 0
            for layer in level_mapa:
                x = 0
                for tile in layer:
                    if tile == '8':
                        jogador.jogador_rect.x = x*400
                        jogador.jogador_rect.y = y*100
                    x += 1
                y += 1
            
    
    # Conf. Camera
    if jogador.jogador_rect.x < 489.0:
        x = 0.0
        fase.camera[0] = 0.0
    elif jogador.jogador_rect.x > (len(level_mapa[0])*100)-489.0:
        x = 0.0
        fase.camera[0] = (len(level_mapa[0])*100)-978.0
    else:
        x = (jogador.jogador_rect.x-fase.camera[0]-489)/4

    if jogador.jogador_rect.y > 450.0:
        y = 0.0
    else:
        y = (jogador.jogador_rect.y-fase.camera[1]-275)/4

    fase.camera[0] += x
    fase.camera[1] += y
    fase.plataforma = []
    fase.plataforma_flutuante = []
    fase.plataforma_espinho = []

    for construcao in range(0, 4):  # 0=fundo2 1=fundo1 2=plataforma e personagem
        if construcao == 0 and fase.level != 4:
            tela.blit(fase.fundo2, (0, 0))
        elif construcao == 1 and fase.level != 4:
            tela.blit(fase.fundo1, (0-fase.camera[0]/5, -130-fase.camera[1]/3))
            tela.blit(fase.amarelado, (0, 0))
        elif construcao == 2:
            if fase.level == 1:
                tela.blit(fase.chao1, (0-fase.camera[0], 0-135-fase.camera[1]))
            elif fase.level == 2:
                tela.blit(fase.chao2, (0-fase.camera[0], 0-135-fase.camera[1]))
            elif fase.level == 3:
                tela.blit(fase.chao3, (0-fase.camera[0], 0-135-fase.camera[1]))
            elif fase.level == 4:
                tela.blit(fase.chao_caverna, (0-fase.camera[0], 0-200-fase.camera[1]))
            y = 0
            for layer in level_mapa:
                x = 0
                for tile in layer:
                    if tile == '5d':
                        fase.limite_lesmaD.append(pygame.Rect(x*100, y*100, 100, 100))
                    if tile == '5e':
                        fase.limite_lesmaE.append(pygame.Rect(x*100, y*100, 100, 100))
                    if tile == '2':
                        fase.plataforma_flutuante.append(pygame.Rect(x*100, y*100, 100, 10))
                    if tile == '3':
                        fase.plataforma_espinho.append(pygame.Rect(x*100, (y*100)+50, 100, 50))
                    if tile == '1' or tile == '4':
                        fase.plataforma.append(pygame.Rect(x*100, y*100, 100, 100))
                    if tile == '1p':
                        if layer[x-1] == '0' or layer[x-1] == '4':
                            fase.plataforma.append(pygame.Rect((x*100)+90, y*100, 10, 100))
                        if layer[x+1] == '0' or layer[x+1] == '4':
                            fase.plataforma.append(pygame.Rect(x*100, y*100, 10, 100))
                    if tile == 'FIM' and fase.level != 3:
                        fase.fim = pygame.Rect(x*100, 0, 100, 700)
                    if tile == 'FIM' and fase.level == 3:
                        fase.fim = pygame.Rect(x*100, y*100, 100, 50)
                    x += 1
                y += 1
        elif construcao == 3:
            y = 0
            for layer in level_mapa:
                x = 0
                for tile in layer:
                    if tile == '2':
                        if y == 3:
                            if layer[x-1] == '0' or layer[x-1] == '4':
                                tela.blit(fase.plataforma3_tiles[0], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            elif layer[x+1] == '0':
                                tela.blit(fase.plataforma3_tiles[2], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            else:
                                tela.blit(fase.plataforma3_tiles[1], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                        if y == 4:
                            if layer[x-1] == '0' or layer[x-1] == '4':
                                tela.blit(fase.plataforma2_tiles[0], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            elif layer[x+1] == '0' or layer[x+1] == '4':
                                tela.blit(fase.plataforma2_tiles[2], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            else:
                                tela.blit(fase.plataforma2_tiles[1], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                        if y == 5:
                            if layer[x-1] == '0' or layer[x-1] == '4':
                                tela.blit(fase.plataforma1_tiles[0], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            elif layer[x+1] == '0' or layer[x+1] == '4':
                                tela.blit(fase.plataforma1_tiles[2], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                            else:
                                tela.blit(fase.plataforma1_tiles[1], ((x*100)-fase.camera[0], (y*100)-15-fase.camera[1]))
                    if tile == '3':
                        tela.blit(fase.espinho, ((x*100)-fase.camera[0], (y*100)-fase.camera[1]))
                    if tile == '11':
                        tela.blit(fase.ib, ((x*100)-fase.camera[0], (y*100)-166-fase.camera[1]))
                    if tile == '12':
                        tela.blit(fase.shoiti, ((x*100)-fase.camera[0], (y*100)-62-fase.camera[1]))
                    if tile == '13' and fase.status_gameover == 1:
                        tela.blit(fase.jhow, ((x*100)-fase.camera[0], (y*100)-209-fase.camera[1]))
                    x += 1
                y += 1

    # FUNC./INT. DO INIMIGO
    for corvo_rect, corvo_object in zip(corvos_rect, corvos_object):
        if corvo_rect.colliderect(jogador.jogador_rect):
            corvo_object.morte = True
        else:
            for tile in fase.plataforma_flutuante+fase.plataforma:
                if corvo_rect.colliderect(tile):
                    corvo_object.morte = True
        if corvo_rect.x-jogador.jogador_rect.x < 400 and corvo_object.morte == False:
            corvo_object.flutuando = 0
            if corvo_object.audio_noloop == True:
                fase.audio_ataque_corvo.play(loops=0, maxtime=0, fade_ms=0)
                corvo_object.audio_noloop = False
            if corvo_object.frame_atual_ataque > len(corvo_object.ataque_direita):
                corvo_object.frame_atual_ataque = 0
            corvo_object.frame = animacao_loop(corvo_object.frame_atual_ataque, len(corvo_object.ataque_direita)-1, corvo_object.ataque_direita)
            corvo_object.frame_atual_ataque += 0.30
            corvo_rect.x -= 25
            corvo_rect.y += 25
        elif corvo_object.morte == True:
            corvo_object.flutuando = 0
            if corvo_object.frame_atual_morrendo > len(corvo_object.ataque_direita):
                corvos_object.remove(corvo_object)
                corvos_rect.remove(corvo_rect)
            corvo_object.frame = animacao_loop(corvo_object.frame_atual_morrendo, len(corvo_object.morrendo_direita)-1, corvo_object.morrendo_direita)
            corvo_object.frame_atual_morrendo += 0.30
        else:
            if corvo_object.frame_atual_andando > len(corvo_object.andando_direita):
                corvo_object.frame_atual_andando = 0
            corvo_object.frame = animacao_loop(corvo_object.frame_atual_andando, len(corvo_object.andando_direita)-1, corvo_object.andando_direita)
            corvo_object.frame_atual_andando += 0.50
            if corvo_object.flutuando_direcao == True:
                corvo_object.flutuando += 1
            elif corvo_object.flutuando_direcao == False:
                corvo_object.flutuando -= 1
            if corvo_object.flutuando > 10 or corvo_object.flutuando < -10:
                corvo_object.flutuando_direcao = not corvo_object.flutuando_direcao
        tela.blit(corvo_object.frame, (corvo_rect.x-fase.camera[0], corvo_object.flutuando+corvo_rect.y-fase.camera[1]))



    for inimigo_rect, inimigo_object in zip(lesmas_rect, lesmas_object):
        if inimigo_object.morte == True:
            fase.audio_morte_lesma.play(loops=0, maxtime=0, fade_ms=0)
            if inimigo_object.frame_atual_morrendo > len(inimigo_object.morrendo_esquerda)-1:
                lesmas_rect.remove(inimigo_rect)
                lesmas_object.remove(inimigo_object)
            else:
                if inimigo_object.direcao == True:
                    inimigo_object.frame = animacao_loop(inimigo_object.frame_atual_morrendo, len(inimigo_object.morrendo_esquerda)-1, inimigo_object.morrendo_esquerda)
                else:
                    inimigo_object.frame = animacao_loop(inimigo_object.frame_atual_morrendo, len(inimigo_object.morrendo_direita)-1, inimigo_object.morrendo_direita)
                inimigo_object.frame_atual_morrendo += 0.20
        else:
            inimigo_rect.y += 10
            if inimigo_object.direcao == True and inimigo_rect.x-jogador.jogador_rect.x > -375 and inimigo_rect.x-jogador.jogador_rect.x < 0 and inimigo_rect.y-jogador.jogador_rect.y < 144 and inimigo_rect.y-jogador.jogador_rect.y < 75:
                inimigo_object.frame_atual_andando = 0
                inimigo_object.frame = inimigo_object.andando_esquerda[0]
                if inimigo_object.bala == []:
                    fase.audio_tiro_lesma.play(loops=0, maxtime=0, fade_ms=0)
                    inimigo_object.bala_direcao = True
                    inimigo_object.bala.append(pygame.Rect(inimigo_rect.x+107, inimigo_rect.y+35, 25, 25))
            elif inimigo_object.direcao == False and inimigo_rect.x-jogador.jogador_rect.x < 300 and inimigo_rect.x-jogador.jogador_rect.x > 0 and inimigo_rect.y-jogador.jogador_rect.y < 144 and jogador.jogador_rect.y-inimigo_rect.y < 75:
                inimigo_object.frame_atual_andando = 0
                inimigo_object.frame = inimigo_object.andando_direita[0]
                if inimigo_object.bala == []:
                    fase.audio_tiro_lesma.play(loops=0, maxtime=0, fade_ms=0)
                    inimigo_object.bala_direcao = False
                    inimigo_object.bala.append(pygame.Rect(inimigo_rect.x-5, inimigo_rect.y+35, 25, 25))
            else:
                for direita, esquerda in zip(fase.limite_lesmaD, fase.limite_lesmaE):
                    if inimigo_rect.colliderect(direita) == 1:
                        inimigo_object.direcao = False
                        inimigo_object.limite = 1
                    elif inimigo_rect.colliderect(esquerda) == 1:
                        inimigo_object.direcao = True
                        inimigo_object.limite = 1
                    else:
                        inimigo_object.limite = 0
                if inimigo_object.tempo_direcao < random.randint(8,20) or inimigo_object.limite == 1:
                    if inimigo_object.frame_atual_andando > len(inimigo_object.andando_direita):
                        inimigo_object.frame_atual_andando = 0
                    if inimigo_object.direcao == True:
                        inimigo_rect.x += 2
                        inimigo_object.frame = animacao_loop(inimigo_object.frame_atual_andando, len(inimigo_object.andando_esquerda)-1, inimigo_object.andando_esquerda)
                    else:
                        inimigo_rect.x -= 2
                        inimigo_object.frame = animacao_loop(inimigo_object.frame_atual_andando, len(inimigo_object.andando_direita)-1, inimigo_object.andando_direita)
                    inimigo_object.frame_atual_andando += 0.20
                    inimigo_object.tempo_direcao += 0.1
                else:
                    inimigo_object.direcao = not inimigo_object.direcao
                    inimigo_object.tempo_direcao = 0
                    inimigo_object.frame_atual_andando = 0
        inimigo_rect = move_inimigo(inimigo_rect, inimigo_object, fase.plataforma_flutuante+fase.plataforma, lesma_limite)
        tela.blit(inimigo_object.frame, (inimigo_rect.x-fase.camera[0], inimigo_rect.y-fase.camera[1]))
        if inimigo_object.bala != []:
            if inimigo_object.frame_atual_bola> len(inimigo_object.bola_direita):
                inimigo_object.frame_atual_bola = 0
            if inimigo_object.bala_direcao == True:
                inimigo_object.bala[0].x += 8
                inimigo_object.frame_bola = animacao_loop(inimigo_object.frame_atual_bola, len(inimigo_object.bola_direita)-1, inimigo_object.bola_direita)
            else:
                inimigo_object.bala[0].x -= 8
                inimigo_object.frame_bola = animacao_loop(inimigo_object.frame_atual_bola, len(inimigo_object.bola_esquerda)-1, inimigo_object.bola_esquerda)
            tela.blit(inimigo_object.frame_bola, (inimigo_object.bala[0].x-fase.camera[0]-38, inimigo_object.bala[0].y-fase.camera[1]-30))
            inimigo_object.bala_tempo += 1
            inimigo_object.frame_atual_bola += 0.20
            damage_bala(jogador, inimigo_object.bala)
        if inimigo_object.bala_tempo > 60:
            inimigo_object.bala_tempo = 0
            inimigo_object.bala = []
    print(BOSS_obj.vida)
    # BOSS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if fase.level == 4:
        if BOSS_obj.cansado == True:
            BOSS_obj.frame_atual_levantando = 0
            BOSS_obj.pedras = [0,0,0]
            BOSS_obj.rect.y += 5
            if BOSS_obj.pousado == False:
                if BOSS_obj.flutuando_direcao == True:
                    tela.blit(BOSS_obj.flutuando_esquerda, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                else:
                    tela.blit(BOSS_obj.flutuando_direita, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
            for tile in fase.plataforma:
                if BOSS_obj.rect.colliderect(tile) == 1:
                    BOSS_obj.pousado = True
                    if BOSS_obj.frame_parado == False:
                        if int(BOSS_obj.frame_atual_pousando) >= 3:
                            BOSS_obj.frame_atual_pousando = 2
                            BOSS_obj.frame_parado = True
                        if BOSS_obj.flutuando_direcao == True:
                            tela.blit(BOSS_obj.pousando_esquerda[int(BOSS_obj.frame_atual_pousando)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                        else:
                            tela.blit(BOSS_obj.pousando_direita[int(BOSS_obj.frame_atual_pousando)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                        BOSS_obj.frame_atual_pousando += 0.5
                    else:
                        BOSS_obj.frame_atual_pousando = 0
                        if int(BOSS_obj.frame_atual_cansado) >= 3:
                            BOSS_obj.frame_atual_cansado = 0
                        if BOSS_obj.dano_cooldown < 10:
                            if BOSS_obj.flutuando_direcao == True:
                                tela.blit(BOSS_obj.dano_esquerda, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                            else:
                                tela.blit(BOSS_obj.dano_direita, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                        else:
                            if BOSS_obj.flutuando_direcao == True:
                                tela.blit(BOSS_obj.cansado_esquerda[int(BOSS_obj.frame_atual_cansado)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                            else:
                                tela.blit(BOSS_obj.cansado_direita[int(BOSS_obj.frame_atual_cansado)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                        BOSS_obj.frame_atual_cansado += 0.1
                    BOSS_obj.rect.bottom = tile.top
                    if BOSS_obj.cansado_tempo == 0:
                        BOSS_obj.dano = True
                    BOSS_obj.cansado_tempo += 0.1
                    if BOSS_obj.cansado_tempo > 20:
                        BOSS_obj.frame_parado = False
                        BOSS_obj.cansado = False
                        BOSS_obj.pousado = False
                        BOSS_obj.levantado = False
                        BOSS_obj.cansado_tempo = 0
                        BOSS_obj.atira_quantidade = 0
        elif BOSS_obj.cansado == False:
            if BOSS_obj.levantado == False:
                if int(BOSS_obj.frame_atual_levantando) >= 3:
                    BOSS_obj.frame_atual_levantando = 2
                    BOSS_obj.levantado = True
                if BOSS_obj.flutuando_direcao == True:
                    tela.blit(BOSS_obj.levantando_esquerda[int(BOSS_obj.frame_atual_levantando)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                else:
                    tela.blit(BOSS_obj.levantando_direita[int(BOSS_obj.frame_atual_levantando)], (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]))
                BOSS_obj.frame_atual_levantando += 0.5
            else:
                if BOSS_obj.flut_direcao == True:
                    BOSS_obj.flut += 1
                elif BOSS_obj.flut_direcao == False:
                    BOSS_obj.flut -= 1
                if BOSS_obj.flut > 10 or BOSS_obj.flut < -10:
                    BOSS_obj.flut_direcao = not BOSS_obj.flut_direcao
                    
                if BOSS_obj.flutuando_direcao == True:
                    tela.blit(BOSS_obj.flutuando_esquerda, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]+BOSS_obj.flut))
                else:
                    tela.blit(BOSS_obj.flutuando_direita, (BOSS_obj.rect.x-fase.camera[0], BOSS_obj.rect.y-fase.camera[1]+BOSS_obj.flut))

            if BOSS_obj.rect.y > 130:
                BOSS_obj.rect.y -= 10
            else:
                if BOSS_obj.pedras[0] == 0 and BOSS_obj.pedras[1] == 0 and BOSS_obj.pedras[2] == 0:
                    BOSS_obj.pedras = [pygame.Rect(BOSS_obj.rect.x-100, BOSS_obj.rect.y, 50, 50),
                                        pygame.Rect(BOSS_obj.rect.x+182, BOSS_obj.rect.y, 50, 50),
                                        pygame.Rect(BOSS_obj.rect.x, BOSS_obj.rect.y-70, 50, 50)]
                if BOSS_obj.atira_quantidade == 3:
                    BOSS_obj.cansado = True

                if BOSS_obj.cooldown < 20:
                    BOSS_obj.cooldown += 0.2

                if BOSS_obj.atira == False:
                    if BOSS_obj.flutuando_direcao == True:
                        BOSS_obj.rect.x -= 10
                        for pedra in BOSS_obj.pedras:
                            if pedra != 0:
                                pedra.x -= 10
                    elif BOSS_obj.flutuando_direcao == False:
                        BOSS_obj.rect.x += 10
                        for pedra in BOSS_obj.pedras:
                            if pedra != 0:
                                pedra.x += 10
                    if BOSS_obj.cooldown >= 20:
                        if BOSS_obj.rect.x-jogador.jogador_rect.x < 400 and BOSS_obj.rect.x-jogador.jogador_rect.x > 300:
                            BOSS_obj.atira = True
                            BOSS_obj.flutuando_direcao = True
                            fase.audio_ataque_BOSS.play(loops=0, maxtime=0, fade_ms=0)
                        elif jogador.jogador_rect.x-BOSS_obj.rect.x < 400 and jogador.jogador_rect.x-BOSS_obj.rect.x > 300:
                            BOSS_obj.atira = True
                            BOSS_obj.flutuando_direcao = False
                            fase.audio_ataque_BOSS.play(loops=0, maxtime=0, fade_ms=0)
                elif BOSS_obj.atira == True:
                    BOSS_obj.pedras_quebra = True
                    BOSS_obj.atira_tempo += 0.15
                    if BOSS_obj.flutuando_direcao == True:
                        BOSS_obj.pedras[BOSS_obj.atira_quantidade].x -= 5
                        BOSS_obj.pedras[BOSS_obj.atira_quantidade].y += 5
                    elif BOSS_obj.flutuando_direcao == False:
                        BOSS_obj.pedras[BOSS_obj.atira_quantidade].x += 5
                        BOSS_obj.pedras[BOSS_obj.atira_quantidade].y += 5
                    if BOSS_obj.atira_tempo > 10:
                        BOSS_obj.pedras[BOSS_obj.atira_quantidade] = 0
                        BOSS_obj.atira_tempo = 0
                        BOSS_obj.atira_quantidade += 1
                        BOSS_obj.atira = False
                        BOSS_obj.cooldown = 0
                        BOSS_obj.pedras_quebra = False

                for tile in fase.plataforma:
                    if BOSS_obj.rect.colliderect(tile):
                        if BOSS_obj.flutuando_direcao == True:
                            BOSS_obj.rect.left = tile.right
                            BOSS_obj.flutuando_direcao = False
                        else:
                            BOSS_obj.rect.right = tile.left
                            BOSS_obj.flutuando_direcao = True
        damage_boss(jogador, BOSS_obj, fase)


        
        #sprite
        if BOSS_obj.pedras != []:
            for pedra in BOSS_obj.pedras:
                if pedra != 0:
                    tela.blit(BOSS_obj.img_pedra, (pedra.x-25-fase.camera[0], pedra.y-25-fase.camera[1]))
                
                
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # desenho sprites jogador
    if jogador.knockback_damage == True:
        if jogador.direcao == True:
            jogador.jogador_estado = jogador.jogador_dano_direita
        else:
            jogador.jogador_estado = jogador.jogador_dano_esquerda
    elif jogador.knockback_damage == False and jogador.mover_ataqueX == True:
        if jogador.frame_atual_ataqueX > len(jogador.jogador_ataque_x):
            jogador.frame_atual_ataqueX = 0
        jogador.jogador_estado = animacao(jogador.frame_atual_ataqueX, jogador.jogador_ataque_x)
        jogador.frame_atual_ataqueX += 0.8
    elif jogador.knockback_damage == False and jogador.mover_ataqueZ == True and jogador.press_ataqueZ == True:
        if jogador.frame_atual_ataqueZ > len(jogador.jogador_ataque_z_direita):
            jogador.frame_atual_ataqueZ = 0
            jogador.press_ataqueZ = False
        if jogador.direcao == True:
            jogador.jogador_estado = animacao(jogador.frame_atual_ataqueZ, jogador.jogador_ataque_z_direita)
        else:
            jogador.jogador_estado = animacao(jogador.frame_atual_ataqueZ, jogador.jogador_ataque_z_esquerda)
        jogador.frame_atual_ataqueZ += 0.9
    elif jogador.pause_comandos == False:
        if jogador.mover_agachar == True and jogador.tempo_voo < 0.6 and jogador.mover_ataqueX == False:
            if jogador.frame_atual_agachando > 2:
                jogador.frame_atual_agachando = 2
            else:
                jogador.frame_atual_agachando += 0.6
            if jogador.direcao == True:
                jogador.jogador_estado = animacao(jogador.frame_atual_agachando, jogador.jogador_agachando_direita)
            else:
                jogador.jogador_estado = animacao(jogador.frame_atual_agachando, jogador.jogador_agachando_esquerda)
        elif (jogador.mover_esquerda == True or jogador.mover_direita == True) and jogador.tempo_voo < 0.6:
            if jogador.mover_esquerda == True and jogador.mover_direita == True:
                jogador.frame_atual_andando = 0
                if jogador.direcao == True:
                    jogador.jogador_estado = jogador.jogador_parado_direita
                else:
                    jogador.jogador_estado = jogador.jogador_parado_esquerda
            else:
                if jogador.frame_atual_andando > 6:
                    jogador.frame_atual_andando = 0
                    jogador.frame_atual_andando += 0.35
                else:
                    jogador.frame_atual_andando += 0.35
                if jogador.direcao == True:
                    jogador.jogador_estado = animacao_loop(jogador.frame_atual_andando, 6, jogador.jogador_andando_direita)
                else:
                    jogador.jogador_estado = animacao_loop(jogador.frame_atual_andando, 6, jogador.jogador_andando_esquerda)
        elif jogador.tempo_voo > 0.6:
            jogador.frame_atual_agachando = 0
            jogador.frame_atual_andando = 0
            if jogador.direcao == True:
                jogador.jogador_estado = jogador.jogador_pulando_direita
            else:
                jogador.jogador_estado = jogador.jogador_pulando_esquerda
        else:
            jogador.frame_atual_agachando = 0
            jogador.frame_atual_andando = 0
            if jogador.direcao == True:
                jogador.jogador_estado = jogador.jogador_parado_direita
            else:
                jogador.jogador_estado = jogador.jogador_parado_esquerda
        if jogador.mover_agachar == False:
            jogador.frame_atual_agachando = 0
    else:
        if jogador.direcao == True:
            jogador.jogador_estado = jogador.jogador_parado_direita
        else:
            jogador.jogador_estado = jogador.jogador_parado_esquerda
    if jogador.laco != []:
        tela.blit(jogador.laco_imagem, (jogador.laco[0].x-fase.camera[0], jogador.laco[0].y-fase.camera[1]))

    #Física
    if jogador.mover_ataqueX == True and jogador.tempo_ataqueX <= 6:
        jogador.tempo_ataqueX += 0.5
    if jogador.mover_ataqueX == True and jogador.tempo_ataqueX > 6:
        jogador.mover_ataqueX = False
    if jogador.tempo_ataqueX > 6:
        if jogador.tempo_ataqueX >= 10:
            jogador.tempo_ataqueX = 0
        else:
            jogador.tempo_ataqueX += 0.5

    if jogador.mover_ataqueZ == True and jogador.tempo_ataqueZ <= 4:
        if jogador.laco == []:
            if jogador.direcao == True:
                jogador.laco.append(pygame.Rect(jogador.jogador_rect.x+125, jogador.jogador_rect.y+57, 30, 30))
                jogador.laco_direcao = True
            else:
                jogador.laco.append(pygame.Rect(jogador.jogador_rect.x-30, jogador.jogador_rect.y+57, 30, 30))
                jogador.laco_direcao = False
        jogador.tempo_ataqueZ += 0.2
    if jogador.mover_ataqueZ == True and jogador.tempo_ataqueZ > 4:
        jogador.mover_ataqueZ = False
    if jogador.tempo_ataqueZ > 4:
        if jogador.tempo_ataqueZ >= 8:
            jogador.tempo_ataqueZ = 0
            jogador.laco.clear()
        else:
            jogador.tempo_ataqueZ += 0.2

    if jogador.laco != []:
        for laco in jogador.laco:
            if jogador.laco_direcao == True:
                laco.x += 15
            else:
                laco.x -= 15

    if jogador.pause_comandos == False and jogador.knockback_damage == False:
        jogador.knockback_tempo = 0
        jogador.mover = [0, 0]
        if jogador.mover_esquerda == True and jogador.mover_agachar == False and jogador.mover_direita == False:
            jogador.direcao = True
            if jogador.mover_ataqueX == True:
                jogador.mover[0] += 5
            else:
                jogador.mover[0] += 10
            jogador.jogador_rect.height = 115
        elif jogador.mover_direita == True and jogador.mover_agachar == False and jogador.mover_esquerda == False:
            jogador.direcao = False
            if jogador.mover_ataqueX == True:
                jogador.mover[0] -= 5
            else:
                jogador.mover[0] -= 10
            jogador.jogador_rect.height = 115
        elif jogador.mover_agachar == True and jogador.mover_ataqueX == False:
            jogador.jogador_rect.height = 55
        else:
            jogador.jogador_rect.height = 115
    elif jogador.pause_comandos == True:
        jogador.knockback_tempo = 0
        jogador.mover = [0, 0]

    jogador.mover[1] += jogador.gravidade
    jogador.gravidade += 3.5
    if jogador.gravidade > 20:
        jogador.gravidade = 20    

    jogador.jogador_rect, colisão_plataforma, colisão_dano = move(jogador, fase.plataforma, fase.plataforma_flutuante, fase)

    #dano
    if fase.plataforma_espinho != []:
        damage_tela(jogador, fase.plataforma_espinho, fase)
    if lesmas_rect != []:
        damage_lesma(jogador, lesmas_rect, lesmas_object, fase)
    if jogador.laco != []:
        damage_laco(jogador, lesmas_rect, lesmas_object)
    if corvos_rect != []:
        damage_corvo(jogador, corvos_rect, corvos_object, fase)

    # condições e blit
    if jogador.mover_agachar == True and jogador.mover_ataqueX == False:
        tela.blit(jogador.jogador_estado, (jogador.jogador_rect.x - fase.camera[0]-32, jogador.jogador_rect.y - fase.camera[1]-84))
    else:
        tela.blit(jogador.jogador_estado, (jogador.jogador_rect.x - fase.camera[0]-32, jogador.jogador_rect.y - fase.camera[1]-29))

    if jogador.tempo_voo > 0.5:
        jogador.encosta_chao = True
    if colisão_plataforma['bottom'] == True:
        jogador.action_segundo_pulo = False
        jogador.tempo_voo = 0
        jogador.gravidade = 0
        if jogador.encosta_chao == True:
            fase.audio_piso_pulo.play(loops=0, maxtime=0, fade_ms=0)
        jogador.encosta_chao = False
    elif jogador.tempo_voo < 5:
        jogador.tempo_voo += 0.5

    #poco
    y = 0
    for layer in level_mapa:
        x = 0
        for tile in layer:
            if tile == 'p':
                tela.blit(fase.poco, ((x*100)-fase.camera[0]-10, (y*100)-fase.camera[1]))
            x += 1
        y += 1

    # sombra
    if fase.level == 3 and fase.status_gameover == 2:
        if fase.sombra_rect == 0:
            fase.sombra_rect = pygame.Rect(-1200, -600, 870, 1000)
        fase.camera[0] += random.randint(-5, 5)
        fase.camera[1] += random.randint(-5, 5)
        tela.blit(fase.sombra, (fase.sombra_rect.x-fase.camera[0], fase.sombra_rect.y-fase.camera[1]))
        if jogador.jogador_rect.colliderect(fase.fim) != 1:
            fase.sombra_rect.x += 9
            if jogador.jogador_rect.colliderect(fase.sombra_rect) == 1:
                jogador.audio_dano.play(loops=0, maxtime=0, fade_ms=0)
                jogador.vida -= 1

    # cutscene 3
    if fase.cutscene_fase_3 != 0:
        if jogador.jogador_rect.colliderect(fase.cutscene_fase_3) == 1:
            jogador.mover[0] = 0
            jogador.mover_esquerda = False
            jogador.mover_direita = False
            jogador.mover_agachar = False
            jogador.mover_descer = False
            jogador.mover_ataqueX = False
            jogador.mover_ataqueZ = False
            jogador.pause_comandos = True
            fase.fade.set_alpha(fase.alpha)
            if fase.alpha <= 300:
                fase.alpha += 10
            else:
                fase.cutscene4.preview()
                fase.alpha = 0
                fase.status_gameover = 2
                fase.cutscene_fase_3 = 0
            tela.blit(fase.fade, (0,0))
    # tela cena fase boss
    if fase.level == 4:
        tela.blit(fase.frente_caverna, (0-fase.camera[0], 0-200-fase.camera[1]))
        if BOSS_obj.vida == 3:
            tela.blit(BOSS_obj.coracao[0], (868, 500)) #(25, 953) (978,550)
        elif BOSS_obj.vida == 2:
            tela.blit(BOSS_obj.coracao[1], (868, 500))
        elif BOSS_obj.vida == 1:
            tela.blit(BOSS_obj.coracao[2], (868, 500))
    
    if jogador.vida == 3:
        tela.blit(jogador.coracao[0], (25, 500)) #(25, 953)
    elif jogador.vida == 2:
        tela.blit(jogador.coracao[1], (25, 500))
    elif jogador.vida == 1:
        tela.blit(jogador.coracao[2], (25, 500))

    # fim
    if fase.fim != []:
        if jogador.jogador_rect.colliderect(fase.fim) == 1:
            jogador.mover[0] = 0
            jogador.mover_esquerda = False
            jogador.mover_direita = False
            jogador.mover_agachar = False
            jogador.mover_descer = False
            jogador.mover_ataqueX = False
            jogador.mover_ataqueZ = False
            jogador.pause_comandos = True
            if fase.level == 3:
                fase.fade.fill((255,255,255))
            fase.fade.set_alpha(fase.alpha)
            if fase.alpha <= 300:
                fase.alpha += 10
            else:
                if fase.level == 1:
                    fase.cutscene2.preview()
                    fase.gameover = True
                    fase.level = 2
                elif fase.level == 2:
                    fase.cutscene3.preview()
                    fase.gameover = True
                    fase.level = 3
                elif fase.level == 3:
                    fase.cutscene_tran.preview()
                    fase.cutscene4_titulo.preview()
                    fase.gameover = True
                    fase.status_gameover = 1
                    fase.level = 4
                fase.alpha = 0
            tela.blit(fase.fade, (0,0))
        else:
            jogador.pause_comandos = False

    # fade inicio
    if fase.gameover == True:
        fase.fade.fill((0,0,0))
        fase.fade.set_alpha(fase.alpha_inicio)
        jogador.pause_comandos = True
        if fase.alpha_inicio >= 0:
            fase.alpha_inicio -= 30
        else:
            fase.gameover = False
            jogador.pause_comandos = False
            fase.alpha_inicio = 300
        tela.blit(fase.fade, (0,0))

    # GAME-OVER
    if jogador.vida <= 0:
        if fase.level == 4:
            fase.cutscene5.preview()
            fase.level = 5
        else:
            jogador.vida = 3
            fase.gameover = True
            if fase.level == 3 and fase.status_gameover == 2:
                fase.sombra_rect = 0
    if BOSS_obj.vida == 0:
        fase.cutscene6.preview()
        fase.level = 5


    return tela

def colisao_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def encontrar_object(rect, tiles, obj):
    obj_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            obj_list.append(obj[tiles.index(tile)])
    return obj_list

def move_inimigo(rect, obj, tiles, tiles2):
    hit_list_plataforma = colisao_test(rect, tiles)
    hit_list_limite = colisao_test(rect, tiles2)
    for tile in hit_list_plataforma:
        rect.bottom = tile.top
    for tile in hit_list_limite:
        obj.direcao = not obj.direcao
        obj.tempo_direcao = 0
    return rect

def move(jogador, tiles, tiles2, fase):
    colisao_lados = {'top': False, 'bottom': False, 'right': False, 'left': False}
    colisao_dano = {'top': False, 'bottom': False, 'right': False, 'left': False}
    jogador.jogador_rect.x += jogador.mover[0]
    hit_list_plataforma = colisao_test(jogador.jogador_rect, tiles)
    hit_list_plataforma_2 = colisao_test(jogador.jogador_rect, tiles2)
    for tile in hit_list_plataforma:
        if jogador.mover[0] > 0:
            jogador.jogador_rect.right = tile.left
            colisao_lados['right'] = True
        elif jogador.mover[0] < 0:
            jogador.jogador_rect.left = tile.right
            colisao_lados['left'] = True

    jogador.jogador_rect.y += jogador.mover[1]
    hit_list_plataforma = colisao_test(jogador.jogador_rect, tiles)
    hit_list_plataforma_2 = colisao_test(jogador.jogador_rect, tiles2)
    for tile in hit_list_plataforma:
        if jogador.mover[1] > 0:
            jogador.jogador_rect.bottom = tile.top
            colisao_lados['bottom'] = True
        elif jogador.mover[1] < 0:
            jogador.jogador_rect.top = tile.bottom
            colisao_lados['top'] = True
    for tile in hit_list_plataforma_2:
        if jogador.mover[1] > 0 and jogador.jogador_rect.bottom <= tile.top + 30 and jogador.mover_descer == False:
            jogador.jogador_rect.bottom = tile.top
            colisao_lados['bottom'] = True
    
    return jogador.jogador_rect, colisao_lados, colisao_dano

def animacao(frame, sprite):
    return sprite[int(frame)]


def animacao_loop(frame, frame_final, sprite):
    if frame > frame_final:
        return sprite[0]
    else:
        return sprite[int(frame)]

def damage_tela(jogador, tiles_inimigo, fase):
    colisao_dano = {'top': False, 'bottom': False, 'right': False, 'left': False}
    hit_list_espinho = colisao_test(jogador.jogador_rect, tiles_inimigo)
    for tile in hit_list_espinho:
        if jogador.invincible >= 40:
            fase.audio_espinho.play(loops=0, maxtime=0, fade_ms=0)
            jogador.audio_dano.play(loops=0, maxtime=0, fade_ms=0)
            jogador.invincible = 0
            jogador.vida -= 1
            jogador.knockback_damage = True
            if jogador.mover[0] > 0:
                colisao_dano['right'] = True
            elif jogador.mover[0] < 0:
                colisao_dano['left'] = True
            else: 
                colisao_dano['top'] = True
    if jogador.invincible < 40:
        jogador.invincible += 1
    if colisao_dano['left'] == True:
        jogador.mover[0] = 25
        jogador.mover[1] = -5
    elif colisao_dano['right'] == True:
        jogador.mover[0] = -25
        jogador.mover[1] = -5
    elif colisao_dano['top'] == True:
        if jogador.direcao == True:
            jogador.mover[0] = -25
            jogador.mover[1] = -5
        else:
            jogador.mover[0] = 25
            jogador.mover[1] = -5            
    if jogador.knockback_damage == True:
        if jogador.knockback_tempo > 3:
            jogador.knockback_damage = False
        jogador.knockback_tempo += 1

def damage_lesma(jogador, tiles_inimigo, tiles_object, fase):
    colisao_dano = {'right': False, 'left': False}
    hit_list = colisao_test(jogador.jogador_rect, tiles_inimigo)
    obj_list = encontrar_object(jogador.jogador_rect, tiles_inimigo, tiles_object)
    for tile,obj in zip(hit_list,obj_list):
        if obj.morte == False:
            if jogador.invincible >= 40:
                if jogador.mover[1] > 3.5:
                    fase.audio_pisado_lesma.play(loops=0, maxtime=0, fade_ms=0)
                    jogador.jogador_rect.bottom = tile.top
                    jogador.jogador_rect.y -= 20
                    obj.morte = True
                elif jogador.mover_ataqueX == True:
                    obj.morte = True
                else:
                    jogador.audio_dano2.play(loops=0, maxtime=0, fade_ms=0)
                    jogador.invincible = 0
                    jogador.vida -= 1 
                    jogador.knockback_damage = True
                    if jogador.mover[0] > 0:
                        colisao_dano['right'] = True
                    elif jogador.mover[0] < 0:
                        colisao_dano['left'] = True
    if jogador.invincible < 40:
        jogador.invincible += 1
    if colisao_dano['left'] == True:
        jogador.mover[0] = 25
        jogador.mover[1] = -5
    elif colisao_dano['right'] == True:
        jogador.mover[0] = -25
        jogador.mover[1] = -5
    if jogador.knockback_damage == True:
        if jogador.knockback_tempo > 3:
            jogador.knockback_damage = False
        jogador.knockback_tempo += 1

def damage_corvo(jogador, tiles_inimigo, tiles_object, fase):
    colisao_dano = {'right': False, 'left': False}
    hit_list = colisao_test(jogador.jogador_rect, tiles_inimigo)
    obj_list = encontrar_object(jogador.jogador_rect, tiles_inimigo, tiles_object)
    for tile,obj in zip(hit_list,obj_list):
        if obj.morte == False:
            fase.audio_morte_corvo.play(loops=0, maxtime=0, fade_ms=0)
            if jogador.invincible >= 40:
                if jogador.mover_ataqueX == True:
                    obj.morte = True
                else:
                    jogador.audio_dano2.play(loops=0, maxtime=0, fade_ms=0)
                    jogador.invincible = 0
                    jogador.vida -= 1 
                    jogador.knockback_damage = True
                    if jogador.mover[0] > 0:
                        colisao_dano['right'] = True
                    elif jogador.mover[0] < 0:
                        colisao_dano['left'] = True
    if jogador.invincible < 40:
        jogador.invincible += 1
    if colisao_dano['left'] == True:
        jogador.mover[0] = 25
        jogador.mover[1] = -5
    elif colisao_dano['right'] == True:
        jogador.mover[0] = -25
        jogador.mover[1] = -5
    if jogador.knockback_damage == True:
        if jogador.knockback_tempo > 3:
            jogador.knockback_damage = False
        jogador.knockback_tempo += 1

def damage_laco(jogador, tiles_inimigo, tiles_object):
    colisao_dano = {'right': False, 'left': False}
    hit_list = colisao_test(jogador.laco[0], tiles_inimigo)
    obj_list = encontrar_object(jogador.laco[0], tiles_inimigo, tiles_object)
    for tile,obj in zip(hit_list,obj_list):
        obj.morte = True
        jogador.tempo_ataqueZ = 5
        jogador.laco.clear()

def damage_bala(jogador, tiles_inimigo):
    colisao_dano = {'top': False, 'bottom': False, 'right': False, 'left': False}
    hit_list = colisao_test(jogador.jogador_rect, tiles_inimigo)
    for tile in hit_list:
        if jogador.invincible >= 40:
            jogador.audio_dano2.play(loops=0, maxtime=0, fade_ms=0)
            jogador.invincible = 0
            jogador.vida -= 1
            jogador.knockback_damage = True
            if jogador.mover[0] > 0:
                colisao_dano['right'] = True
            elif jogador.mover[0] < 0:
                colisao_dano['left'] = True
            else: 
                colisao_dano['top'] = True
            tiles_inimigo.clear()
    if jogador.invincible < 40:
        jogador.invincible += 1
    if colisao_dano['left'] == True:
        jogador.mover[0] = 25
        jogador.mover[1] = -5
    elif colisao_dano['right'] == True:
        jogador.mover[0] = -25
        jogador.mover[1] = -5
    elif colisao_dano['top'] == True:
        if jogador.direcao == True:
            jogador.mover[0] = -25
            jogador.mover[1] = -5
        else:
            jogador.mover[0] = 25
            jogador.mover[1] = -5            
    if jogador.knockback_damage == True:
        if jogador.knockback_tempo > 3:
            jogador.knockback_damage = False
        jogador.knockback_tempo += 1

def damage_boss(jogador, inimigo, fase):
    colisao_dano = {'right': False, 'left': False}
    hit_list = colisao_pedra(jogador.jogador_rect, inimigo.pedras)
    if inimigo.rect.colliderect(jogador.jogador_rect):
        if inimigo.vida != 0:
            if jogador.invincible >= 40 and inimigo.dano == False:
                    jogador.audio_dano2.play(loops=0, maxtime=0, fade_ms=0)
                    jogador.invincible = 0
                    jogador.vida -= 1 
                    jogador.knockback_damage = True
                    if jogador.mover[0] > 0:
                        colisao_dano['right'] = True
                    elif jogador.mover[0] < 0:
                        colisao_dano['left'] = True
            elif inimigo.dano == True:
                if jogador.mover_ataqueX == True:
                    inimigo.vida -= 1
                    inimigo.dano = False
                    inimigo.dano_cooldown = 0
                    fase.audio_dano_BOSS.play(loops=0, maxtime=0, fade_ms=0)
    if jogador.laco != []:
        if inimigo.rect.colliderect(jogador.laco[0]):
            jogador.tempo_ataqueZ = 5
            jogador.laco.clear()
            if inimigo.dano == True:
                inimigo.vida -= 1
                inimigo.dano = False
                inimigo.dano_cooldown = 0
                fase.audio_dano_BOSS.play(loops=0, maxtime=0, fade_ms=0)
    if inimigo.pedras != []:
        for pedra in hit_list:
            if pedra.colliderect(jogador.jogador_rect):
                if jogador.invincible >= 40:
                    jogador.audio_dano2.play(loops=0, maxtime=0, fade_ms=0)
                    jogador.invincible = 0
                    jogador.vida -= 1 
                    jogador.knockback_damage = True
                    pedra = 0
    if inimigo.dano_cooldown < 10:
        inimigo.dano_cooldown += 1
    if jogador.invincible < 40:
        jogador.invincible += 1
    if colisao_dano['left'] == True:
        jogador.mover[0] = 25
        jogador.mover[1] = -5
    elif colisao_dano['right'] == True:
        jogador.mover[0] = -25
        jogador.mover[1] = -5
    if jogador.knockback_damage == True:
        if jogador.knockback_tempo > 3:
            jogador.knockback_damage = False
        jogador.knockback_tempo += 1
def colisao_pedra(rect, tiles):
    hit_list = []
    for tile in tiles:
        if tile != 0:
            if rect.colliderect(tile):
                hit_list.append(tile)
    return hit_list
