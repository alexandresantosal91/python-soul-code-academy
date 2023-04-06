from IPython.utils import str

l: str = 'Lista de letras'
data: str = '6/04/2023'

# Tamanho da string

tamanho = len(l)
print(tamanho)

# split da string
lista = l.split(" ")
lista2 = data.split("/")
print(lista)
print(lista2)

# Substituição
print(l.replace(" de ", ""))
