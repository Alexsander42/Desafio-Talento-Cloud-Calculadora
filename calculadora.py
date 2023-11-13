
def calculadora(num1, num2, operacao):
    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero"
    else:
        resultado = "Operação inválida"
    
    return resultado

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao_desejada = input("Digite a operação desejada (soma, subtracao, multiplicacao, divisao): ")

resultado_final = calculadora(numero1, numero2, operacao_desejada)
print(f"O resultado da operação é: {resultado_final}")
