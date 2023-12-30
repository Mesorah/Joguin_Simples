#Jogo simples com apenas um bixo, o jogo n tem história, e sendo um jogo de turnos
#chance de se esquivar automatico
from random import randint
def main():
    print('\033[1;33mLuta 1x1 contra The Mega of The Blaster of The World')
    print('Você tem 10 de vida e causa 3 de dano contra ele com 25 de vida e causa 4 de dano')
    print('Você tem 3 poções de cura que curam 4 pontos de vida')
    print('Você e o boss têm 10% de chance de dar e receber críticos, causando o dobro de dano')
    print('Você tem 75% de chance de se esquivar, mas você da 2 de dano e se você não se esquivar você toma 3 de dano')
    print('Se você conseguir 2 ataque seguidos você usa o super causando 5 de dano')
    print('Tem 10% de chance de você ou o monstro se esquivar automáticamente\033[m')
def vida():
    vida_jogador = 10
    vida_mostro = 25
    começa = randint(1,2)
    cura = 3
    tot = 0
    super = []

    if começa == 1 or começa == 2:
        print('Você começa')
        ataque = 'a'

        while ataque != 'p':
            while vida_mostro != 0:
                ataque = str(input('Aperte p para atacar ou e para esquivar: ')).lower()
                if ataque == 'e':
                    chance_esquiva = randint(1, 3)
                    lado = 'a'
                    while lado != 'esquerda' or lado != 'direita':
                        lado = str(input('direita ou esquerda: ')).lower()
                        if lado == 'direita':
                            if chance_esquiva == 1 or chance_esquiva == 2:
                                vida_mostro -= 2
                                print(f'\033[1;34mVocê se esquivou para a direita e deu 2 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            break
                        elif lado == 'esquerda':
                            if chance_esquiva == 1 or chance_esquiva == 2:
                                vida_mostro -= 2
                                print(f'\033[1;34mVocê se esquivou para a esquerda e deu 2 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m')
                            break
                        else:
                            print('erro')
                tot += 1
                if tot > 1 and vida_jogador < 10:
                    if cura > 0 and vida_jogador <= 6:
                        while True:
                            poçao = str(input(f'\033[1;32mVocê tem {cura} poções de cura. Precione 1 para tomar uma poção de cura e 2 para não tomar:\033[m '))
                            if poçao == '1':
                                cura -= 1
                                vida_jogador += 4
                                print(f'Você usou uma poção de cura. Poções restantes: {cura}')
                                print(f'\033[1;36mVocê recuperou 4 pontos de vida\033[m')
                                break
                            elif poçao == '2':
                                break
                            else:
                                print('Erro: digite "1" para tomar poção ou "2" para não tomar.')
                if ataque not in 'p':
                    print()
                else:   
                    #usar aqui
                    chance_desvio_automatico = randint(1, 2)
                    chance_acerto_monstro = randint(0,1)
                    chance_acerto_jogador = randint(0,1)
                    critico_pessoa = randint(1, 10)
                    #desvio automatico
                    if chance_desvio_automatico == 1:
                        c = vida_jogador
                        print(f'você se desviou Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                    elif chance_desvio_automatico == 2:
                        d = vida_mostro
                        print(f'o monstro se desviou Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                    if critico_pessoa == 1 and chance_desvio_automatico != 2:
                        vida_mostro -= 6    
                        print(f'\033[1;35mVocê deu um CRÍTICO de 6 de dano\033[m.')
                        print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}') 
                    else:
                        if chance_acerto_monstro == 0 and chance_desvio_automatico != 2:  
                            if super.count(1) < 2:  
                                vida_mostro -= 3
                                print(f'\033[1;32mO monstro tomou 3 de dano\033[m')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')   
                            #ataque normal pessoa 
                            carregado = 2
                            super.append(1)
                            if super.count(1) == 2:
                                vida_mostro -= 5
                                print(f'voce usou o super Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                                while carregado != 0:
                                    super.remove(1)
                                    carregado -= 1                       
                        if vida_mostro <= 0:
                            print(f'\033[1;34mVocê venceu meu parabéns 🥳😎\033[m')
                            break
                        else:
                            critico_boss = randint(1,10)
                            if critico_boss == 1 and chance_desvio_automatico != 1:
                                #ataque crítico
                                vida_jogador -= 8
                                print(f'\033[1;31mVocê tomou um CRÍTICO de 8 de dano\033[m.')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                            elif chance_acerto_monstro == 1 and chance_desvio_automatico != 1:
                                #ataque normal boss
                                super.append(0) 
                                if 1 in super:
                                    super.pop(0)
                                vida_jogador = vida_jogador - 4
                                print(f'\033[1;31mVocê tomou 4 de dano\033[m.')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                    if vida_jogador <= 0:
                        print('Você perdeu que pena... 😢🙁')
                        break

main()
vida()