class Armor:
    def __init__(self, nome, defesa, preco):
        self.nome = nome
        self.defesa = defesa
        self.preco = preco

class Weapon:
    def __init__(self, nome, dano, preco):
        self.nome = nome
        self.dano = dano
        self.preco = preco

class Loja:
    def __init__(self, pocoes=10, weapons=[], armors=[]):
        self.pocoes = pocoes
        self.weapons = weapons
        self.armors = armors
    
    def comprar(self, jogador):
        print("---BEM VINDO A LOJA---")
        escolha = -1
        while escolha != 0:
            escolha = int(input("\nDo que precisa? Armas(1), Armaduras(2), Poções(3), Sair(0): "))
            if escolha == 3:
                pots = int(input(f'Temos atualmente {self.pocoes} poções, cada 1 custa 3xp\nQuantos você quer?: '))
                custo = jogador.get_xp() - (pots * 3)
                if custo < 0:
                    print("Opa, não tens dinheiro para tudo isso, venderei-te somente uma")
                    jogador.set_pocoes(jogador.get_xp() + 1)
                else:
                    print("Aqui está, meu consagrado!")
                    jogador.set_pocoes(pots)

                print("Vorte sempre, meu fiote de canguru ;)")
            
            if escolha == 2:
                print("Catálogo de Armaduras:")
                for e in range(len(self.armors)):
                    print(f'[{e}]{self.armors[e].nome}: {self.armors[e].defesa} dano, {self.armors[e].preco} de XP')
                print()
                escol = int(input("Quais vais querer? (escolha por indice): "))
                custo = jogador.get_xp() - self.armors[escol].preco
                if custo < 0:
                    print("Opa, não tens dinheiro para tudo isso, não venderei-te!")
                else:
                    print("Aqui está, meu compadre!")
                    jogador.set_armor(self.armors[escol])

                print("Vorte sempre, meu fiote de canguru ;)")

            if escolha == 1:
                print("Catálogo de Armas:")
                for e in range(len(self.weapons)):
                    print(f'[{e}]{self.weapons[e].nome}: {self.weapons[e].dano} dano, {self.weapons[e].preco} de XP')
                print()
                escol = int(input("Quais vais querer? (escolha por indice): "))
                custo = jogador.get_xp() - self.weapons[escol].preco
                if custo < 0:
                    print("Opa, não tens dinheiro para tudo isso, não venderei-te!")
                else:
                    print("Aqui está, meu bom cliente!")
                    jogador.set_weapon(self.weapons[escol])

        print("Vorte sempre, meu fiote de canguru ;)")
