# ------------------------------------
# Este arquivo contém todas as classes
# referentes a campeonatos de surf
# ------------------------------------
# -------------------------------
# Classe Patrocinador
# -------------------------------
class Patrocinador:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

# -------------------------------
# Classe Atleta
# -------------------------------
class Atleta:
    def __init__(self, nome, idade, pontuacao, categoria):
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao
        self.categoria = categoria

# -------------------------------
# Classe Campeonato
# -------------------------------
class Campeonato:
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        self.categoria = categoria
        self.nome = nome
        self.local = local
        self.premiacao = premiacao
        self.patrocinadores = patrocinadores
        self.atletas = []
        self.vencedor = ''
    
    def incliurAtletas(self,atletas):
        self.atletas = atletas

    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome

# -------------------------------
# Classe CampeonatoLenda
# -------------------------------
class CampeonatoLenda(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        for a in atletas:
            if (a.categoria == 'lenda'):
                self.atletas.append(a)

    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 100

# -------------------------------
# Classe CampeonatoProfissional
# -------------------------------
class CampeonatoProfisional(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        for a in atletas:
            if (a.categoria == 'lenda') | (a.categoria == 'profissional'):
                self.atletas.append(a)

    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 50

# -------------------------------
# Classe CampeonatoAmador
# -------------------------------
class CampeonatoAmador(Campeonato):
    def __init__(self, categoria, nome, local, premiacao,patrocinadores):
        super().__init__(categoria, nome, local, premiacao,patrocinadores)

    def incliurAtletas(self,atletas):
        for a in atletas:
            if (a.categoria == 'amador'):
                self.atletas.append(a)
            
    def vencidoPor(self,atleta):
        self.vencedor = atleta.nome
        atleta.pontuacao += 10
