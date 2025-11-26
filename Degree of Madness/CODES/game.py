import pygame #IMPORTA BIBLIOTECA PYGAME
from pygame.locals import * #IMPORTA TODAS AS FUNÇÕES E VARIÁVEI DA BIBILOTECA
from sys import exit #IMPORTA A FUNÇÃO QUE PERMITE QUE FECHEMOS A JANELA
from random import randint #IMPORTA FUNÇÃO DE ALEATORIEDADE

pygame.init() #INICALIZA TODAS AS FUNÇÕES E VARIÁVEIS DA BIBLIOTECA PYGAME

pygame.mixer.music.set_volume(0.3)
musica_fundo= pygame.mixer.music.load('assets\Legião Instrumental.mp3')
pygame.mixer.music.play(-1)


som_colisao= pygame.mixer.Sound('assets\dano.mp3')
som_colisao.set_volume(0.1)
som_pontos=pygame.mixer.Sound('assets\pontos.mp3')
som_pontos.set_volume(0.1)
som_up_vida=pygame.mixer.Sound('assets\som_up_vida.mp3')
som_up_vida.set_volume(0.1)

largura=1920 #CONSTANTE QUE DETERMINA A LARGURA DA TELA
altura=1080 #CONSTANTE QUE DETERMINA A ALTURA DA TELA

x_vilao1= randint(0,1080)
y_vilao1=0

x_vilao2= randint(0,1080)
y_vilao2=0

x_vilao3= randint(0,1080)
y_vilao3=0

x_vilao4= randint(0,1080)
y_vilao4=0

x_vilao5= randint(0,1080)
y_vilao5=0

x_vilao6= randint(0,1080)
y_vilao6=0

x_personagem=960
y_personagem=540

vida=100

pontos=0
fonte=pygame.font.SysFont('arial',40,True,False)
texto_vida= pygame.font.SysFont('arial',40,True,False)

x_obstaculo = randint(0,1920) #DEFINE OS INSTERVALOS DA ALEATORIEDADE DO EIXO X
y_obstaculo = randint(0,1080) #DEFINE OS INSTERVALOS DA ALEATORIEDADE DO EIXO Y

tela=pygame.display.set_mode((largura,altura)) #FUNÇÃO QUE CRIA A JANELA (NELA CONTÉM AS PROPORÇÕES QUE FORA ESCOLHIDA)
pygame.display.set_caption("Degree of Madness") #DETERMINA O NOME (TÍTULO) DA JANELA


frames=pygame.time.Clock() #VARIÁVE QUE VAI DETERMINAR OS FRAMES DO JOGO

while 1>0: #LOOP PRINCIPAL DO JOGO, POIS O JOGO DEVE TER UM CICLO INFINITO 
    frames.tick(60) #DETERMINA OS FRAMES DO JOGO 
    tela.fill((0,0,0)) #FUNÇÃO QUE FAZ QUE A FORMA SE LOCOMOVA, POIS VAI PREENCHEDO A TELA COM A COR ESCOLHIDA, DANDO A SENSAÇÃO DE CAIR 
    mensagem=f'Pontos:{pontos}'
    mensagem1=f'VIDA:{vida}'

    texto_formatado=fonte.render(mensagem,True,(255,255,255))
    mensagem_vida=texto_vida.render(mensagem1,True,(255,255,255))

    for event in pygame.event.get(): # FUNÇÃO RESPONÁVEL POR CONTER OS EVENTOS (INTERFERÊNCIAS DO CICLO) NO JOGO 
        if event.type == QUIT: #CASO O USUÁRIO QUEIRA SAIR, FECCHA A JANELA
            pygame.quit()
            exit()
        if  event.type==KEYDOWN: #EVENTO PARA MODIFICAR A FORMA, SE APERTAR QUALQUER TECLA
            if event.key==K_a: #DETERMINA O MOVIMENTO QUANDO O USUÁRIO APERTA A TECLA a
                x_personagem=x_personagem-20 #DETERMINA DESLOCAMENTO
            elif event.key==K_d: #DETERMINA O MOVIMENTO QUANDO O USUÁRIO APERTA A TECLA d
                x_personagem=x_personagem+20 #DETERMINA DESLOCAMENTO
            elif event.key==K_s: #DETERMINA O MOVIMENTO QUANDO O USUÁRIO APERTA A TECLA s
                y_personagem=y_personagem+20 #DETERMINA DESLOCAMENTO
            elif event.key==K_w: #DETERMINA O MOVIMENTO QUANDO O USUÁRIO APERTA A TECLA w
                y_personagem=y_personagem-20 #DETERMINA DESLOCAMENTO


# ESSE BLOCO FORA DO LOOP FOR VAI GARANTIR QUE A FORMA SE LOCOMOVA QUANDO A TECLA É PRESSIONADA #
    if pygame.key.get_pressed()[K_a]:
        x_personagem=x_personagem-20
    if pygame.key.get_pressed()[K_d]:
        x_personagem=x_personagem+20
    if pygame.key.get_pressed()[K_s]:
        y_personagem=y_personagem+20
    if pygame.key.get_pressed()[K_w]:
        y_personagem=y_personagem-20

    retangulo_vermelho= pygame.draw.rect(tela,(255,0,0),(x_vilao1,y_vilao1,150,150)) #FUNÇÃO PARA CRIAR UM RETÂNGULO NA JANELA
    if y_vilao1>=altura: #QUANDO A FORMA CHEGA NO FINAL 
        y_vilao1=0  #RETORNA A POSIÇÃO INICIAL
        x_vilao1=randint(0,1980)
    y_vilao1=y_vilao1+5 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)

    retangulo_vermelho2= pygame.draw.rect(tela,(255,0,0),(x_vilao2,y_vilao2,150,150)) #FUNÇÃO PARA CRIAR UM CIRCULO NA JANELA
    if y_vilao2>=altura: #QUANDO A FORMA CHAGA NO FINAL 
        y_vilao2=0  #RETORNA A POSIÇÃO INICIAL
    y_vilao2=y_vilao2+10 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)

    retangulo_vermelho3= pygame.draw.rect(tela,(255,0,0),(x_vilao3,y_vilao3,150,150)) #FUNÇÃO PARA CRIAR UM CIRCULO NA JANELA
    if y_vilao3>=altura: #QUANDO A FORMA CHAGA NO FINAL 
        y_vilao3=0  #RETORNA A POSIÇÃO INICIAL
    y_vilao3=y_vilao3+15 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)

    retangulo_vermelho4= pygame.draw.rect(tela,(255,0,0),(x_vilao4,y_vilao4,150,150)) #FUNÇÃO PARA CRIAR UM RETÂNGULO NA JANELA
    if y_vilao4>=altura: #QUANDO A FORMA CHEGA NO FINAL 
        y_vilao4=0  #RETORNA A POSIÇÃO INICIAL
    y_vilao4=y_vilao4+15 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)
    
    retangulo_vermelho5= pygame.draw.rect(tela,(255,0,0),(x_vilao5,y_vilao5,150,150)) #FUNÇÃO PARA CRIAR UM RETÂNGULO NA JANELA
    if y_vilao5>=altura: #QUANDO A FORMA CHEGA NO FINAL 
        y_vilao5=0  #RETORNA A POSIÇÃO INICIAL
    y_vilao5=y_vilao5+20 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)
    
    retangulo_vermelho6= pygame.draw.rect(tela,(255,0,0),(x_vilao6,y_vilao6,150,150)) #FUNÇÃO PARA CRIAR UM RETÂNGULO NA JANELA
    if y_vilao6>=altura: #QUANDO A FORMA CHEGA NO FINAL 
        y_vilao6=0  #RETORNA A POSIÇÃO INICIAL
    y_vilao6=y_vilao6+25 #ISSO VAI FAZER COM QUE A FORMA SE LOCOMOVA NA JANELA (INICALMENTE ELA SÓ CRECE O TAMANHO NO EIXO ESCOLHIDO)
    
    retangulo_verde_personagem= pygame.draw.rect(tela,(0,255,0),(x_personagem,y_personagem,100,100))
    retangulo_obstaculo=pygame.draw.rect(tela,(255,255,255),(x_obstaculo,y_obstaculo,100,100))

    if retangulo_verde_personagem.colliderect(retangulo_obstaculo): #QUANDO O PERSONAGEM ENCOSTAR NO OBSTACULO 
        x_obstaculo = randint(0,1720) # O OBSTACULO MUDA DE POISÇÃO ALEATORIAMENTE 
        y_obstaculo = randint(0,880)
        pontos=pontos+1
        som_pontos.play()

    tela.blit(texto_formatado,(1500,50))

    if retangulo_verde_personagem.colliderect(retangulo_vermelho): #QUANDO O PERSONAGEM ENCOSTAR NO VILÃO
        vida=vida-1
        som_colisao.play()
    tela.blit(mensagem_vida,(300,50))  

    if retangulo_verde_personagem.colliderect(retangulo_vermelho2): #QUANDO O PERSONAGEM ENCOSTAR NO VILÃO
        vida=vida-1
        som_colisao.play()
    tela.blit(mensagem_vida,(300,50))  

    if retangulo_verde_personagem.colliderect(retangulo_vermelho3): #QUANDO O PERSONAGEM ENCOSTAR NO OBSTACULO 
        vida=vida-1
        som_colisao.play()
    tela.blit(mensagem_vida,(300,50)) 
        

    if retangulo_verde_personagem.colliderect(retangulo_vermelho4): #QUANDO O PERSONAGEM ENCOSTAR NO OBSTACULO 
        vida=vida-1
        som_colisao.play()
    tela.blit(mensagem_vida,(300,50)) 




    pygame.display.update()

