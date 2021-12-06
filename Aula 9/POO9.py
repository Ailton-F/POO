from pessoa import Cliente
from pessoa import Endereco

c1 = Cliente('Ailton', 17)
c1.insere_enreco('Natal', 'RN')
print(c1.nome)
c1.lista_endereco()
print()

c2 = Cliente('Bianca', 16)
c2.insere_enreco('Natal', 'RN')
c2.insere_enreco('Rio de Janeiro', 'RJ')
print(c2.nome)
c2.lista_endereco()
print()

c3 = Cliente('João', 30)
c3.insere_enreco('São Paulo', 'SP')
print(c3.nome)
c3.lista_endereco()