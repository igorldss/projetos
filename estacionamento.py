#Os veículos são cadastrados com tipo do veículo (carro, moto, caminhão, etc.), placa, modelo, data
#e horário de entrada e data e horário de saída, com um valor total a pagar.
#O sistema deve receber como input o valor da hora e só deve atribuir o total a pagar no momento
#que receber a informação do horário de saída, que não é obrigatório inserir na hora do registro do veículo.
#Para isso, deve-se encapsular todos os atributos e ter mapeado a regra que a saída do veículo não poderá 
#ser mais antiga que a entrada dele no estacionamento.


class Estacionamento:
    def __init__(self, veiculo, placa, modelo, data, horarioentrada=0, horariosaida=0):
        self.veiculo = veiculo
        self.placa = placa
        self.modelo = modelo
        self.data = data
        self.horarioentrada = horarioentrada
        self.horariosaida = horariosaida
    
    def getvalorpagar(self):
        return self.horarioentrada
    
    def setvalorpagar(self):
        a = self.horarioentrada
        b = self.horariosaida
        valor_hora = 10
        if a > b:
            return 'A saida não pode ser mais antiga que a entrada'
        else:
            c = b - a
            total = c * valor_hora
        return total

carro1 = Estacionamento('carro',12345,'Monza','19/03/2020')

carro1.horarioentrada = int(input("Digite o horario de entrada: "))
carro1.horariosaida = int(input("Digite o horario de saida: "))


print(
    ' Tipo de veiculo: ',carro1.veiculo,
    '\n','Placa do veiculo: ',carro1.placa,
    '\n','Modelo do veiculo: ',carro1.modelo,
    '\n','Data de uso do estacionamento: ',carro1.data,
    '\n','Valor a pagar: ',carro1.setvalorpagar(),'Reais')