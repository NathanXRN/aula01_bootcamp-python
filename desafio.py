CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome    = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário 
# Converte a entrada para um número de ponto flutuante 
salario = float(input("Digite o valor do salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido 
# Converte a entrada para um número de ponto flutuante
bonus   = float(input("Digite a porcentagem bônus recebido: "))

# 4) Calcule o valor do bônus final 
valor_do_bonus = round((CONSTANTE_BONUS + salario * bonus),2)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus 
print(f"O usuário {nome} possui um bônus de R${valor_do_bonus} reais.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?









