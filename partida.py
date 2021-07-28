import creatures as cre
from random import randint

class Partida():
    def __init__(self, player, monstros, quantia):
        self.player = player
        self.mobs = monstros
        self.quantia = quantia

    def start_match(self):
        rodada = 0
        print(f'{self.player.get_nome()} encontra um {self.mobs.get_nome()}')
        while rodada == 0:
            #Inicializacao da luta
            print('\n')
            print(f'VIDAS => {self.player.get_nome()}:{self.player.get_vida()} - {self.mobs.get_nome()}:{self.mobs.get_vida()}')

            #Rodada do Player
            extra = 0
            escolha = int(input("Atacar(1), Defender(2), Beber poção(3): "))
            if escolha == 1:
                ataque = randint(0,5) + self.player.get_dano()
                defesa = randint(0,5) + self.mobs.get_defesa()
                print(f'{self.player.get_nome()} deu {ataque} de dano, e {self.mobs.get_nome()} defendeu-se de {defesa} de dano')
                if defesa >= ataque:
                    pass
                else:
                    self.mobs.set_vida(self.mobs.get_vida() - (ataque - defesa))
            if escolha == 2:
                extra = randint(0,5) + self.player.get_defesa()
                print(f'{self.player.get_nome()} tem agora mais {extra} de defesa')
                self.player.set_vida(self.player.get_vida() + 1)
            if (escolha == 3) and (self.player.get_pocoes() > 0):
                if (self.player.get_vida() + 5) > 20:
                    self.player.set_vida(20)
                else:
                    self.player.set_vida(self.player.get_vida() + 5)
                self.player.set_pocoes(self.player.get_pocoes() - 1)
                print(f'{self.player.get_nome()} tem agora {self.player.get_pocoes()} poções')

            #Rodado do monstro
            if self.mobs.get_vida() > 0:
                ataque = randint(0,5) + self.mobs.get_dano()
                defesa = randint(0,5) + self.player.get_defesa() + extra
                print(f'{self.mobs.get_nome()} deu {ataque} de dano, e {self.player.get_nome()} defendeu-se de {defesa} de dano')
                if defesa >= ataque:
                    pass
                else:
                    self.player.set_vida(self.player.get_vida() - (ataque - defesa))

            #Avaliando rodada
            if self.player.get_vida() <= 0:
                print(f'{self.player.get_nome()} foi morto, {self.mobs.get_nome()} venceu')
                rodada = 1
            if self.mobs.get_vida() <= 0:
                print(f'{self.mobs.get_nome()} foi morto, {self.player.get_nome()} venceu')
                rodada = 1

    def uppar(self):
        self.player.set_xp(self.player.get_xp() + self.mobs.get_xp())
        self.player.uppar()