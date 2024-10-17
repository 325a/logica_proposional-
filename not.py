def tabla_verdad_not():
    print("A | NOT A")
    print("---------")
    for a in [0, 1]:
        resultado = not a
        print(f"{a} |  {int(resultado)}")

tabla_verdad_not()