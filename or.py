def tabla_verdad_or():
    print("A | B | A OR B")
    print("----------------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a or b
            print(f"{a} | {b} |   {resultado}")

tabla_verdad_or()