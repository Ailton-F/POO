#Aula 2 - Método de classe
from POO.pessoa import Pessoa

p1 = Pessoa.por_ano_nascimento('Ailton', 2004)
print(p1.idade)
p1.get_ano_nascimento()
