import abc


class Produtos:
    def __init__(self, nome, preco_unit, unidade_medida, qtd_estocada):
        self.nome = nome
        self._preco = preco_unit
        self.unidade = unidade_medida
        self.estoque = qtd_estocada

    @abc.abstractmethod
    def acresenta10(self):
        pass

    @abc.abstractmethod
    def desconta20(self):
        pass

    @abc.abstractmethod
    def acrecimo15(self):
        pass

class Alimento(Produtos):
    def __init__(self,nome, preco_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preco_unit, unidade_medida, qtd_estocada)

    @property
    def acresenta10(self):
        return self._preco

    @acresenta10.setter
    def acresenta10(self):
        a  = (self.estoque * self._preco) * 0.1
        return a

class Higiene(Produtos):
    def __init__(self,nome, preco_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preco_unit, unidade_medida, qtd_estocada)

    @property
    def desconta20(self):
        return self._preco

    @desconta20.setter
    def desconta20(self):
        a  = (self.estoque * self._preco) - (self._preco * 0.2)
        return a

class Eletronicos(Produtos):
    def __init__(self,nome, preco_unit, unidade_medida, qtd_estocada):
        super().__init__(nome, preco_unit, unidade_medida, qtd_estocada)

    @property
    def acrecimo15(self):
        return self._preco
    
    @acrecimo15.setter
    def acrecimo15(self):
        a  = (self.estoque * self._preco) * 0.15
        return a



alimento1 = Alimento('Leite',5.00,'Litro',150)
higiene1 = Higiene('Papel Higienico',12.00,'kilo',2500)
eletronico1 = Eletronicos('Celular',1000.00,'gramas',123)

print(' Alimeto:',alimento1.nome,'\n','Valor do Produto:',alimento1._preco,'\n','Unidade de medida:',alimento1.unidade,'\n','Estoque:',alimento1.estoque)
print('-'*30)
print(' Limpeza:',higiene1.nome,'\n','Valor do Produto:',higiene1._preco,'\n','Unidade de medida:',higiene1.unidade,'\n','Estoque:',higiene1.estoque)
print('-'*30)
print(' Eletronicos:',eletronico1.nome,'\n','Valor do Produto:',eletronico1._preco,'\n','Unidade de medida:',eletronico1.unidade,'\n','Estoque:',eletronico1.estoque)
print('-'*30)