class Medico:
    def __init__(self, crm, nome, idade, salario):
        self.crm = crm
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def calculaaposentadoria(self):
        idademedico = self.idade
        if idademedico < 55:
            return 'não pode aposentar!'
        elif idademedico >= 55:
            valoraposentadoria = self.salario * 0.80
            return valoraposentadoria

class Auxiliar(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)
        self.salario = salario
        self.nome = nome
        self.idade = idade

    def calculaaposentadoria(self):
        idadeauxiliar = self.idade
        if idadeauxiliar < 60:
            return 'não pode aposentar!'
        elif idadeauxiliar >= 60:
            valoraposentadoria = self.salario * 0.80
            return valoraposentadoria

class Cirurgiao(Medico):
    def __init__(self, crm, nome, idade, salario):
        super().__init__(crm, nome, idade, salario)

    def calculaaposentadoria(self):
        idadecirurgiao = 0
        if idadecirurgiao < 50:
            return 'não pode aposentar!'
        elif idadecirurgiao >= 50:
            valoraposentadoria = (self.salario * 0.80) + 2000                                                  
            return valoraposentadoria

