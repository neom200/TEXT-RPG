class Player():
    def __init__(self, nome, arma, armadura, vida=20, nivel=1, xp=0, pocoes=2):
        self.nome = nome
        self.vida = vida
        self.weapon = arma
        self.nivel = nivel
        self.xp = xp
        self.armor = armadura
        self.pocoes = pocoes

    def uppar(self):
        while self.xp > (self.nivel * 5):
            self.nivel += 1
            self.xp -= 1
        while self.vida < 20:
            self.vida += 1
        self.vida += 5 * self.nivel
        
    def get_nome(self):
        return self.nome
    def get_vida(self):
        return self.vida
    def get_weapon(self):
        return self.weapon.nome
    def get_armor(self):
        return self.armor.nome
    def get_dano(self):
        return self.weapon.dano
    def get_defesa(self):
        return self.armor.defesa
    def get_xp(self):
        return self.xp
    def get_pocoes(self):
        return self.pocoes
    def get_nivel(self):
        return self.nivel

    def set_vida(self, quantia):
        self.vida = quantia
    def set_weapon(self, objeto):
        self.weapon = objeto
    def set_armor(self, objeto):
        self.armor = objeto
    def set_xp(self, quantia):
        self.xp = quantia
    def set_pocoes(self, quantia):
        self.pocoes = quantia

    def show_status(self):
        print("Nome: ", self.get_nome(), end=' - ')
        print("Vida: ", self.get_vida())
        print("Arma: ", self.get_weapon(), end=' - ')
        print("Armadura: ", self.get_armor())
        print(f'XP[Nomes]: {self.get_xp()}[{self.get_nivel()}] - ')
        print("Poções: ", self.get_pocoes())


class Monstro():
    def __init__(self, nome, dano, nivel, xp, defesa):
        self.nome = nome
        self.dano = dano + 1
        self.nivel = nivel
        self.vida = (nivel * 10)
        self.xp = xp
        self.defesa = defesa + 1

    def get_nome(self):
        return self.nome
    def get_vida(self):
        return self.vida
    def get_dano(self):
        return self.dano
    def get_defesa(self):
        return self.defesa
    def get_xp(self):
        return self.xp

    def set_vida(self, quantia):
        self.vida = quantia
    def set_dano(self, quantia):
        self.dano = quantia
    def set_defesa(self, quantia):
        self.defesa = quantia