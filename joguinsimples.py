#Jogo simples com apenas um bixo, o jogo n tem história, e sendo um jogo de turnos
from random import randint
def main():
    print('Luta 1x1 contra The mega of The Blaster of The World')
    print('Você com 10 de vida de 3 de dano contra ele com 25 de vida e 4 de dano')
    print('você tem 3 pots de cura que curam 4 de vida')
def vida():
    vida_jogador = 10
    vida_mostro = 25
    começa = randint(1,2)
    cura = 3
    tot = 0

    if começa == 1 or começa == 2:
        print('voce começa')
        ataque = 'a'

        while ataque != 'p':
            while vida_mostro != 0:
                ataque = str(input('aperte p para atacar: ')).lower()
                tot += 1
                if tot > 1:
                    if cura > 0:
                        poçao = int(input(f'você tem {cura} poções de cura precione 1 para tomar uma poção de cura: '))
                        if poçao == 1:
                            cura -= 1
                            vida_jogador += 4
                            print(f'Você usou uma poção de cura. Poções restantes: {cura}')
                            print(f'voce recuperou 4 pontos de vida')
                if ataque not in 'p':
                    print('erro')
                else:   
                    chance_acerto = randint(0,1)
                    if chance_acerto == 0:
                        vida_mostro = vida_mostro - 3
                        print('o monstro tomou 3 de dano')
                        print(f'sua vida {vida_jogador}  \ vida do monstro: {vida_mostro}')
                        if vida_mostro <= 0:
                            print('voce venceu')
                            break
                    else:
                        vida_jogador = vida_jogador - 4
                        print('você tomou 4 de dano')
                        print(f'sua vida {vida_jogador}  \ vida do monstro: {vida_mostro}')
                    if vida_jogador <= 0:
                        print('voce perdeu')
                        break


main()
vida()
