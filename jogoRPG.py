import creatures as cre
from partida import Partida
import tools
from random import randint

""" LOJA """
w_names = ['Adaga', 'Machado', 'Espada', 'Foice', 'Duas Lâminas', 'Martelo', 'Sabre de Luz']
a_names = ['Roupa de Couro', 'Roupa de Malha', 'Armadura de Bronze', 'Armadura de Ferro', 'Armadura de Obsidian', 'Armadura de Escamas de Dragão']
wps = []
t = 0
for elem in w_names:
    wps.append(tools.Weapon(elem, t+3, t+5))
    t += 3
ams = []
t = 1
for elem in a_names:
    ams.append(tools.Armor(elem, t+3, t+5))
    t += 3
shop = tools.Loja(10, wps, ams)

""" MONSTROS """
nomes = ['Goblin', 'Troll', 'Fantasma', 'Vampiro', 'Demonio']
monsters = []
nms = 1
for q in range(10):
    monsters.append(cre.Monstro(nomes[q%5], nms+1, nms, nms+3, nms))
    nms += 1


""" JOGADOR """
n = input("Digite seu nome: ")
jogador = cre.Player(n, wps[0], ams[0])


""" JOGO """
jgs = 0
while jgs < len(monsters):
    print("--------------------\n")
    print(f'Status de {jogador.get_nome()}: {jogador.get_weapon()}, {jogador.get_armor()}, {jogador.get_pocoes()} poções')

    camin = input("Deseja ir a Loja primeiro? (S/N):")
    if camin == 'S' or camin == 's':
        print()
        shop.comprar(jogador)
        print()

    print("--------SEESÂO DE BATALHA-------")
    p = Partida(jogador, monsters[jgs], 1)
    print(f'[{jogador.get_nome()}]: {jogador.get_xp()} XP - Lv.{jogador.get_nivel()}')
    p.start_match()
    if jogador.get_vida() > 0:
        p.uppar()
        print(f'{jogador.get_nome()} tem agora {jogador.get_xp()} de XP e está no nível {jogador.get_nivel()}')
        if jogador.get_pocoes() == 0:
            jogador.set_pocoes(2)
        jgs += 1
    else:
        print(f'{jogador.get_nome()} foi derrotado')
        jgs = 1000
