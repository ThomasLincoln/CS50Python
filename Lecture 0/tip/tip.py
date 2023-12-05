pagamento = float(input("How much was the meal? ").replace("$", ""))
porcentagem = float(input("What percentage would you like to tip? ").replace("%", ""))
tip = (pagamento/100) * porcentagem
print(f"Leave ${tip:.2f}")