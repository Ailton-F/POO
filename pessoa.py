import datetime
from random import randint


# Aula 1 - Criando uma classe
class Pessoa:
    data_atual = datetime.date.today()
    ano_atual = data_atual.year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print('{} não fala comendo!'.format(self.nome))
            return

        if self.falando:
            print('{} Já está falando'.format(self.nome))
            return

        print('{} está falando sobre {}'.format(self.nome, assunto))
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print('{} não está falando'.format(self.nome))
            return

        print('{} parou de falar'.format(self.nome))
        self.falando = False

    def comer(self, alimento):
        if self.falando:
            print('{} Está falando, não pode comer agora!'.format(self.nome))
            return

        if self.comendo:
            print('{} já está comendo!'.format(self.nome))
            return

        print('{} está comendo {}'.format(self.nome, alimento))
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print('{} não está comendo'.format(self.nome))

            return

        print('{} parou de comer'.format(self.nome))
        self.comendo = False

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Aula 2 - Método de classe

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Aula 3 - Método estático

    @staticmethod
    def gera_id():
        id = randint(100000, 999999)
        return print(f'Sua id é {id}')


# Aula 4 - getters e setters
class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


# Aula 5 - Atributos de classe
class A:
    vc = 123  # Variavel de classe

    def __init__(self):  # Variavel de instância
        self.vc = 321


# Aula 6 - Encapsulamento
class BaseDeDados:
    def __init__(self):
        self.__dados = {}  # Um underline significa protegido, dois significa privado
        # para modificar um atributo, fora da classe, com dois underline é preciso se referir a ele como _NOMEDACLASSE__ATRIBUTO
        # Ou criar uma propriedade usando um getter e um setter

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self.__dados:
            self.__dados['Clientes'] = {id: nome}
        else:
            self.__dados['Clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['Clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['Clientes'][id]

#Aula 7 - Relação de associação
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor

    @property
    def nome(self):
        return self.__nome

class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca


    def escrever(self):
        print('Caneta escrevendo')

class MaquinaDeEscrever:
    pass

    def escrever(self):
        print('Máquina escrevendo.......')

#Aula 8 - Agregação
