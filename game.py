import pygame
import random
import time


pygame.init()

loseSound = pygame.mixer.Sound("assets/lose.wav")
waterSound = pygame.mixer.Sound("assets/water.mp3")
largura = 800
altura = 600
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/sky.png")
display = pygame.display.set_mode((largura, altura))
icone = pygame.image.load("assets/icone.jpg")
pygame.display.set_icon(icone)
pygame.display.set_caption("Não deixe a criança ser influenciada! ")
criancaBoneco = pygame.image.load("assets/crianca.png")
criancaPosicaoX = largura * 0.42
criancaPosicaoY = altura * 0.7
movimentoX = 0
alcool = pygame.image.load("assets/alcool.png")
drogas = pygame.image.load("assets/drogas.png")



#inicio cores https://www.rapidtables.com/web/color/RGB_Color.html
branco = (255,255,255)
preto = (0,0,0)
# cores fim

def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()

def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf", 40)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()

def dead():
    message_display("A criança foi influenciada e está mal! ")
    
def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Desvios:"+str(desvios), True, branco)
    display.blit(texto, (0, 0))

def jogo():
    pygame.mixer.music.load('assets/musicashark.mp3')
    pygame.mixer.music.play(-1) # -1 é loopig infinito
    criancaPosicaoX = largura * 0.45
    criancaPosicaoY = altura * 0.68
    criancaLargura = 120
    movimentoX = 0
    alcoolPosicaoX = largura * 0.45
    alcoolPosicaoY = -220
    alcoolLargura = 45
    alcoolAltura = 98
    alcoolVelocidade = 5

    drogasPosicaoX = largura * 0.45
    drogasPosicaoY = -220
    drogasLargura = 45
    drogasAltura = 101
    drogasVelocidade = 5
    desvios = 0

    while True:
        #verificar interação do usuario
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0
        #fim verificar interação do usuario
        #fundo
        display.fill(branco)
        display.blit(fundo, (0,0))
        #fundo fim
        criancaPosicaoX = criancaPosicaoX + movimentoX
        display.blit(criancaBoneco, (criancaPosicaoX, criancaPosicaoY))
        if criancaPosicaoX < 0:
            criancaPosicaoX = 0
        elif criancaPosicaoX > 680:
            criancaPosicaoX = 680
        display.blit(criancaBoneco, (criancaPosicaoX, criancaPosicaoY))  # inserir imagem da tela

        #quando ultrapassa a barreira ele começa em um lugar novo
        display.blit(alcool, (alcoolPosicaoX, alcoolPosicaoY))
        #display.blit(drogas, (drogasPosicaoX, drogasPosicaoY))
        alcoolPosicaoY = alcoolPosicaoY + alcoolVelocidade
        drogasPosicaoY = drogasPosicaoY + drogasVelocidade
        if alcoolPosicaoY > altura :
            pygame.mixer.Sound.play(waterSound)
            alcoolPosicaoY = -220
            alcoolVelocidade += 0.3
            alcoolPosicaoX = random.randrange(0, largura-50)
            desvios += 1
        """if drogasPosicaoY > altura :
            pygame.mixer.Sound.play(waterSound)
            alcoolPosicaoY = -220
            alcoolVelocidade += 0.3
            alcoolPosicaoX = random.randrange(0, largura-50)
            desvios += 1
            """
        #fim da barreira
        # (ini)análise de colisão:
        if criancaPosicaoY < alcoolPosicaoY + alcoolAltura:
            if criancaPosicaoX < alcoolPosicaoX and criancaPosicaoX+criancaLargura > alcoolPosicaoX or alcoolPosicaoX+alcoolLargura > criancaPosicaoX and alcoolPosicaoX+alcoolLargura < criancaPosicaoX+criancaLargura:
                dead()
        #if criancaPosicaoY < drogasPosicaoY + drogasAltura:
            #if criancaPosicaoX < drogasPosicaoX and criancaPosicaoX+criancaLargura > drogasPosicaoX or drogasPosicaoX+drogasLargura > criancaPosicaoX and drogasPosicaoX+drogasLargura < criancaPosicaoX+criancaLargura:
                #dead()

        # [fim]análise de colisão:
        escrevendoPlacar(desvios)
        
        fps.tick(60)
        pygame.display.update()
jogo()
print('até mais')