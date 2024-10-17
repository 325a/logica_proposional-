def tabla_verdad_and():
    print("A | B | A AND B")
    print("----------------")
    for a in [0, 1]:
        for b in [0, 1]:
            resultado = a and b
            print(f"{a} | {b} |   {resultado}")

tabla_verdad_and()




