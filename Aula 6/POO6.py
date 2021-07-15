#Aula 6 - Encapsulamento
from POO.pessoa import BaseDeDados

bd = BaseDeDados()
bd.inserir_cliente(1, 'Ailton')
bd.inserir_cliente(2, 'Alexandre')
bd.inserir_cliente(3, 'Bianca')
bd.apagar_cliente(2)
bd.lista_clientes()
bd.dados = 'Outra coisa'