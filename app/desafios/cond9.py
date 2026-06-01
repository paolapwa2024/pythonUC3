# === VERIFICADOR DE DIA DA SEMANA ===

dia = input("Digite o dia da semana: ").strip().lower()

match dia:
    case "segunda":
        print("Dia útil — começo de semana!")
    case "terca":
        print("Dia útil.")
    case "quarta":
        print("Dia útil — metade da semana!")
    case "quinta":
        print("Dia útil.")
    case "sexta":
        print("Dia útil — quase fim de semana!")
    case "sabado" | "domingo":
        print("Final de semana!")
    case _:
        print("Dia inválido. Digite ex: segunda, terca, sexta, sabado...")