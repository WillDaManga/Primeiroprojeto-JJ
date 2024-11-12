# Função para exibir a tabuada de um número
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Solicita ao usuário o número para o qual deseja ver a tabuada
numero = int(input("Digite o número para ver sua tabuada: "))

# Chama a função e exibe a tabuada
tabuada(8)