
nome = input("Digite o nome do agente: ")
nota = float(input("Digite a nota final do agente (0 a 10): "))

if 9.0 <= nota <= 10.0:
    classificacao = "Excelente 😎🏅 "
elif 7.0 <= nota < 9.0:
    classificacao = "Bom 😁👍"
elif 5.0 <= nota < 7.0:
    classificacao = "Regular 😳"
elif 3.0 <= nota < 5.0:
    classificacao = "Ruim 🤦‍♂️🚫"
elif 0.0 <= nota < 3.0:
    classificacao = "Crítico 🫥"
else:
    classificacao = "Nota inválida 😔"

print(f"Agente {nome}, sua classificação é: {classificacao} (nota: {nota})")

