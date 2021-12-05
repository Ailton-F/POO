#Aula 7 - Associação
from pessoa import Escritor
from pessoa import Caneta
from pessoa import MaquinaDeEscrever

escritor = Escritor('Ailton')
caneta = Caneta('bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina

escritor.ferramenta.escrever()


