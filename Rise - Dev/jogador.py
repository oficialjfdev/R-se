import pygame

class Jogador:
    def __init__(self):
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        self.audio_pulo = pygame.mixer.Sound('audio/Jogador/Pulando 3.wav')
        self.audio_pulo.set_volume(.3)
        self.audio_pulo2 = pygame.mixer.Sound('audio/Jogador/Pulando 2.wav')
        self.audio_pulo2.set_volume(.3)
        self.audio_dano = pygame.mixer.Sound('audio/Jogador/Perdendo HP 1.wav')
        self.audio_dano2 = pygame.mixer.Sound('audio/Jogador/Perdendo HP 2.wav')
        self.audio_laco = pygame.mixer.Sound('audio/Jogador/Jogando laço 2.wav')
        self.audio_girando = pygame.mixer.Sound('audio/Jogador/Girando 1.wav')

        coracao_img = pygame.image.load('img/life_voce.png').convert_alpha()
        self.coracao = [coracao_img.subsurface(pygame.Rect((0, 0), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 25), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 50), (85, 25))),
                        coracao_img.subsurface(pygame.Rect((0, 75), (85, 25)))]

        self.jogador_estado = 0
        self.direcao = True  # True=direita False=esquerda
        self.frame_atual_andando = 0
        self.frame_atual_agachando = 0
        self.frame_atual_ataqueX = 0
        self.frame_atual_ataqueZ = 0
    
        self.jogador_rect = pygame.Rect(100,100,61,115)
        self.mover = [0,0]
        self.mover_esquerda = False
        self.mover_direita = False
        self.mover_agachar = False
        self.mover_descer = False
        self.mover_ataqueX = False
        self.mover_ataqueZ = False
        self.press_agachar = 0
        self.pause_comandos = False
        self.encosta_chao = False

        self.vida = 3
        self.knockback_damage = False
        self.knockback_tempo = 0
        self.invincible = 0
        self.gravidade = 0
        self.tempo_voo = 0
        self.action_segundo_pulo = False

        self.tempo_ataqueX = 0
        self.tempo_ataqueZ = 0
        self.press_ataqueZ = False
        self.laco_ativado = False
        self.laco_direcao = True
        self.laco = []

        spritesheet = pygame.image.load('img/spritesheet.png').convert_alpha()

        # frame laço
        self.laco_imagem = pygame.image.load('img/laco.png').convert_alpha()

        # frame parado
        self.jogador_parado_direita = spritesheet.subsurface(pygame.Rect((0, 0), (125, 144)))
        self.jogador_parado_esquerda = pygame.transform.flip(self.jogador_parado_direita, True, False)

        # frame pulando
        self.jogador_pulando_direita = spritesheet.subsurface(pygame.Rect((125, 0), (125, 144)))
        self.jogador_pulando_esquerda = pygame.transform.flip(self.jogador_pulando_direita, True, False)

        # frames andando
        self.jogador_andando_direita = [spritesheet.subsurface(pygame.Rect((0, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*1, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*2, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*3, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*4, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*5, 144), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*6, 144), (125, 144)))]
        self.jogador_andando_esquerda = []
        for sprite in self.jogador_andando_direita:
            self.jogador_andando_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frames agachando
        self.jogador_agachando_direita = [spritesheet.subsurface(pygame.Rect((375, 0), (125, 144))),
                                          spritesheet.subsurface(pygame.Rect(((1*125)+375, 0), (125, 144))),
                                          spritesheet.subsurface(pygame.Rect(((2*125)+375, 0), (125, 144)))]
        self.jogador_agachando_esquerda = []
        for sprite in self.jogador_agachando_direita:
            self.jogador_agachando_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frames ataque x
        self.jogador_ataque_x = [spritesheet.subsurface(pygame.Rect((0, 288), (125, 144))),
                                spritesheet.subsurface(pygame.Rect((125*1, 288), (125, 144))),
                                spritesheet.subsurface(pygame.Rect((125*2, 288), (125, 144))),
                                spritesheet.subsurface(pygame.Rect((125*3, 288), (125, 144))),
                                spritesheet.subsurface(pygame.Rect((125*4, 288), (125, 144)))]

        # frames ataque z
        self.jogador_ataque_z_direita = [spritesheet.subsurface(pygame.Rect((0, 432), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*1, 432), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*2, 432), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*3, 432), (125, 144))),
                                        spritesheet.subsurface(pygame.Rect((125*4, 432), (125, 144)))]
        self.jogador_ataque_z_esquerda = []
        for sprite in self.jogador_ataque_z_direita:
            self.jogador_ataque_z_esquerda.append(pygame.transform.flip(sprite, True, False))

        # frame dano
        self.jogador_dano_direita = spritesheet.subsurface(pygame.Rect((250, 0), (125, 144)))
        self.jogador_dano_esquerda = pygame.transform.flip(self.jogador_dano_direita, True, False)

    def movimentacao(self, status, tecla):
        key = pygame.key.get_pressed()
        if status == pygame.KEYDOWN:
            if tecla == pygame.K_LEFT:
                self.mover_direita = True
                self.direcao = False
            elif tecla == pygame.K_RIGHT:
                self.mover_esquerda = True
                self.direcao = True
            elif tecla == pygame.K_DOWN and self.tempo_voo < 2:
                self.mover_agachar = True
                if self.press_agachar == 0 and self.mover_ataqueX == False:
                    self.press_agachar = 1
                    self.jogador_rect.y += 60
            if tecla == pygame.K_UP and self.tempo_voo < 2 and key[pygame.K_DOWN] == 0 and self.knockback_tempo == 0:
                self.audio_pulo.play(loops=0, maxtime=0, fade_ms=0)
                self.gravidade = -30
                self.action_segundo_pulo = True
            elif tecla == pygame.K_UP and self.action_segundo_pulo == True and self.knockback_tempo == 0:
                self.audio_pulo2.play(loops=0, maxtime=0, fade_ms=0)
                self.gravidade = -30
                self.action_segundo_pulo = False
            if key[pygame.K_DOWN] and key[pygame.K_UP]:
                self.mover_descer = True
            if tecla == pygame.K_x and self.mover_ataqueX == False and self.tempo_ataqueX == 0:
                self.audio_girando.play(loops=0, maxtime=0, fade_ms=0)
                self.mover_ataqueX = True
            elif tecla == pygame.K_z and self.mover_ataqueZ == False:
                self.audio_laco.play(loops=0, maxtime=0, fade_ms=0)
                self.mover_ataqueZ = True
                if self.tempo_ataqueZ == 0:
                    self.press_ataqueZ = True
        if status == pygame.KEYUP:
            self.mover_descer = False
            if tecla == pygame.K_RIGHT:
                self.mover_esquerda = False
            if tecla == pygame.K_LEFT:
                self.mover_direita = False
            if tecla == pygame.K_DOWN:
                self.mover_agachar = False
                if self.press_agachar == 1 and self.mover_ataqueX == False:
                    self.press_agachar = 0
                    self.jogador_rect.y -= 60