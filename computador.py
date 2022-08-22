# Crie uma classe para armazenar as informações de um computador. O computador deve ter os seguintes atributos:
''' -Modelo
    -Fabricante
    -Processador
    -Memória RAM
    -Tamanho do HD
    -Espaço ocupado do HD
    -Está ligado?'''

#métodos:
#-liga() -> altera o status de "Está ligado" para True
#-desliga() -> altera o status de "Está ligado" para False
#-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
#-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD

class Computador:
    def __init__(self, fabricante, processador, memoriaram, tamanhohd, ocupacaohd, ligado=False):
        self.fabricante = fabricante
        self.processador = processador
        self.ram = memoriaram
        self.hd = tamanhohd
        self.ocupacao = ocupacaohd
        self.estado = ligado

#-liga() -> altera o status de "Está ligado" para True
    def liga(self):
        self.estado = True
        return 'O pc ta ligado'
#-desliga() -> altera o status de "Está ligado" para False
    def desliga(self):
        self.estado = False
        return 'O pc ta desligado'

#-limparHD() -> recebe por parâmetro o tamanho do espaço que deseja liberar do HD
    def limpahd(self, limpar=0):
        self.ocupacao = self.ocupacao - limpar
        if limpar > 256:
            return 'Não é possivel limpar mais que 256'
        elif limpar <= 0:
            return 'Você não esta limpando nada'
        else:
            return limpar

#-ocuparHD() -> recebe por parâmetro o tamanho do espaço que deseja ocupar do HD
    def ocupahd(self, ocupa=0):
        self.ocupacao = ocupa
        if ocupa > 256:
            return 'Não é possivel ocupar mais que 256'
        elif ocupa <= 0:
            return 'Você não esta ocupando nada'
        else: 
            return ocupa




pc = Computador('intel,','i9,','8 GB,','256 GB,',0)
print('-'*30)
print(pc.fabricante,pc.processador,pc.ram,pc.hd,pc.ocupacao,pc.liga())
print(pc.fabricante,pc.processador,pc.ram,pc.hd,pc.ocupacao,pc.desliga())
print('-'*30)
print(pc.fabricante,pc.processador,pc.ram,pc.hd,'Estava ocupando:',pc.ocupahd(64))
print(pc.fabricante,pc.processador,pc.ram,pc.hd,'removeu:',pc.limpahd(48))
print(pc.fabricante,pc.processador,pc.ram,pc.hd,'Agora ocupa:',pc.ocupacao)
print('-'*30)
