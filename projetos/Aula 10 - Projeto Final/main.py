def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def listar():
    vantagens = ['Sintaxe clara e concisa', 'Ampla biblioteca padrão', 'Facilidade de leitura', 'Multiplataforma', 'Grande comunidade de desenvolvedores']
    for v in vantagens:
        print(v)

print("Bem-vindo(a) à Calculadora Python!")
print("Escolha a operação que deseja realizar:")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Dividir")
print("4 - Multiplicar")
print("5 - Listar vantagens do Python")

escolha = input("Digite sua escolha (1/2/3/4/5): ")

if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1, "+", num2, "=", somar(num1, num2))

    elif escolha == '2':
        print(num1, "-", num2, "=", subtrair(num1, num2))

    elif escolha == '3':
        print(num1, "/", num2, "=", dividir(num1, num2))

    elif escolha == '4':
        print(num1, "*", num2, "=", multiplicar(num1, num2))

elif escolha == '5':
    print("As vantagens do Python são:")
    listar()

else:
    print("Opção inválida. Por favor, tente novamente.")