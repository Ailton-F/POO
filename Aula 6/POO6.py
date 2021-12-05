# Aula 6 - Encapsulamento
from pessoa import BaseDeDados

bd = BaseDeDados()
bd.inserir_cliente(1, 'Ailton')
bd.inserir_cliente(2, 'Alexandre')
bd.inserir_cliente(3, 'Bianca')
bd.apagar_cliente(2)
bd.dados = 'Outra coisa' #Assim não consigo alterar
#bd._BaseDeDados__dados = 'outra coisa' #Só consigo acessar uma variavel restrita dessa maneira
bd.lista_clientes()

