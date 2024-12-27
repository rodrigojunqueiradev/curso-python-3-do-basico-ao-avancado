primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite um valor: ")

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior")
elif primeiro_valor == segundo_valor:
    print(f"Os valores são iguais")
else:
    print(f"{segundo_valor} é maior")
