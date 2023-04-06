# criando a string com o alfabeto em letras maiúsculas
alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

# percorrendo e imprimindo a string com enumerate
for i, letter, in enumerate(alfabeto):
    print(i, letter)

# substituindo espaços por traços ("-") e imprimindo para o usuário
alfabeto_dash = alfabeto.replace(" ", "-")
print(alfabeto_dash)
