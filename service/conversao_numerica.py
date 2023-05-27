# Função que define o menu
def recebendo_num_inteiros():
    numero = int(input('Digite um número: '))
    result = bin(numero)
    print(f'Você digitou o número {numero}.')
    return (f'Em binário o valor é: {result}')
