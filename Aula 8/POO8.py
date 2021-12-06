#Aula 8 - Agregação
from pessoa import CarrinhoDeCompras
from pessoa import Produtos

carrinho = CarrinhoDeCompras()
produto1 = Produtos('camisa', 40)
produto2 = Produtos('iphone', 100000)
produto3 = Produtos('panela', 15)

carrinho.inserirProduto(produto1)
carrinho.inserirProduto(produto2)
carrinho.inserirProduto(produto3)
carrinho.listaProdutos()
print(carrinho.tsum())

