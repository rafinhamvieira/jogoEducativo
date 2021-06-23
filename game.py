import pygame
import random
from functionBasic import delay, cleanerScreen

archive = open('archive.txt', 'w')
archive.close()
archive = open('archive.txt', 'a')
cleanerScreen()
nome = input('\n Qual o seu nome? ')
email = input('\n Qual seu email? ')
archive.write(' ' + nome + '\n ' + email)
print('\n Clique na tela quando ela abrir!')
delay()

pygame.init()

loseSound = pygame.mixer.Sound("assets/lose.wav")
waterSound = pygame.mixer.Sound("assets/water.mp3")
largura = 1280
altura = 720
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/parque2.png")
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
    delay()
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
        elif criancaPosicaoX > 1100:
            criancaPosicaoX = 1100
        display.blit(criancaBoneco, (criancaPosicaoX, criancaPosicaoY))  # inserir imagem da tela

        #quando ultrapassa a barreira ele começa em um lugar novo
        display.blit(alcool, (alcoolPosicaoX, alcoolPosicaoY))
        alcoolPosicaoY = alcoolPosicaoY + alcoolVelocidade
        if alcoolPosicaoY > altura :
            pygame.mixer.Sound.play(waterSound)
            alcoolPosicaoY = -220
            alcoolVelocidade += 0.3
            alcoolPosicaoX = random.randrange(0, largura-50)
        #fim da barreira
        # (ini)análise de colisão:
        if criancaPosicaoY < alcoolPosicaoY + alcoolAltura:
            if criancaPosicaoX < alcoolPosicaoX and criancaPosicaoX+criancaLargura > alcoolPosicaoX or alcoolPosicaoX+alcoolLargura > criancaPosicaoX and alcoolPosicaoX+alcoolLargura < criancaPosicaoX+criancaLargura:
                dead()
        # [fim]análise de colisão:
        escrevendoPlacar(desvios)
        fps.tick(60)
        pygame.display.update()
jogo()
print('até mais')