# Aula 5 - Atributos de classe
from POO.pessoa import A

a1 = A()
a2 = A()
a1.vc = 321 # Isso não mexe direto na classe, e sim na instância

A.vc = 'EITA'# Isso mexe, e é o mais recomendavel caso seja necessário

print()

print(a1.vc)
print(a2.vc)
print(A.vc)
