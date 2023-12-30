#Jogo simples com apenas um bixo, o jogo n tem história, e sendo um jogo de turnos
#super
#esquivou azul
#nao se esquivou vermelho
from random import randint
def main():
    print('\033[1;33mLuta 1x1 contra The Mega of The Blaster of The World')
    print('Você tem 10 de vida e causa 3 de dano contra ele com 25 de vida e causa 4 de dano')
    print('Você tem 3 poções de cura que curam 4 pontos de vida')
    print('Você e o boss têm 10% de chance de dar e receber críticos, causando o dobro de dano')
    print('Você tem 75% de chance de se esquivar, mas você da 3 de dano e se você não se esquivar você toma 3 de dano\033[m]')
def vida():
    vida_jogador = 10
    vida_mostro = 25
    começa = randint(1,2)
    cura = 3
    tot = 0

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
                                vida_mostro -= 3
                                print(f'\033[1;34mVocê se esquivou para a direita e deu 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m]')
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m]')
                            break
                        elif lado == 'esquerda':
                            if chance_esquiva == 1 or chance_esquiva == 2:
                                vida_mostro -= 3
                                print(f'\033[1;34mVocê se esquivou para a esquerda e deu 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m]')
                            
                            else:
                                vida_jogador -= 3
                                print(f'\033[1;31mvocê não conseguiu se esquivar e tomou 3 de dano Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}\033[m]')
                            break
                        else:
                            print('erro')
                tot += 1
                if tot > 1 and vida_jogador < 10:
                    if cura > 0:
                        poçao = int(input(f'Você tem {cura} poções de cura. Precione 1 para tomar uma poção de cura: '))
                        if poçao == 1:
                            cura -= 1
                            vida_jogador += 4
                            print(f'Você usou uma poção de cura. Poções restantes: {cura}')
                            print(f'\033[1;33mVocê recuperou 4 pontos de vida\033[m')
                if ataque not in 'p':
                    print()
                else:   
                    chance_acerto = randint(0,1)
                    critico_pessoa = randint(1, 10)
                    if critico_pessoa == 1:
                        vida_mostro -= 6    
                        print(f'\033[1;35mVocê deu um CRÍTICO de 6 de dano\033[m.')
                        print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}') 
                    else:
                        if chance_acerto == 0:                 
                            vida_mostro -= 3
                            print(f'\033[1;32mO monstro tomou 3 de dano\033[m')
                            print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                        
                            if vida_mostro <= 0:
                                print('Você venceu')
                                break
                        else:
                            critico_boss = randint(1,10)
                            if critico_boss == 1:
                                vida_jogador -= 8
                                print(f'\033[1;31mVocê tomou um CRÍTICO de 8 de dano\033[m.')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                            else:
                                vida_jogador = vida_jogador - 4
                                print(f'\033[1;31mVocê tomou 4 de dano\033[m.')
                                print(f'Sua vida {vida_jogador} \ Vida do monstro: {vida_mostro}')
                    if vida_jogador <= 0:
                        print('Você perdeu')
                        break

main()
vida()