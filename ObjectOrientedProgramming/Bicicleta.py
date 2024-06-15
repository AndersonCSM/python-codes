class Bicicleta:
    def __init__(self, modelo, cor, ano, valor):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biiiiiiiiiiiiiiii")

    def parar(self):
        print("Bicicleta parannnndo")

    def correr(self):
        print("Vrummm")

    def __str__(self):
        # retorna a instância da classe de maneira visualmente agradável
        """
        __dict__ -> retorna o dicionário de dados da classe
        __class__.__name__ -> nome da classe
        """
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Caloy", "azul", "1997", "400")

b1.buzinar()
b1.correr()
b1.parar()
print(b1)
