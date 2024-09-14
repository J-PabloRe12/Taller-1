nota1 = float(input("Ingrese la nota del 'Taller 1': "))
nota2 = float(input("Ingrese la nota del 'Taller 2': "))
nota3 = float(input("Ingrese la nota del 'Cuestonario 1': "))
nota4 = float(input("Ingrese la nota del 'Cuestonario 2': "))
nota5 = float(input("Ingrese la nota del 'Proyecto Final': "))
notaFinal = (nota1 * 0.2 + nota2 * 0.15 + nota3 * 0.22 + nota4 * 0.1 + nota5 * 0.33)

if all(0 <= n <= 5 for n in [nota1, nota2, nota3, nota4, nota5]):
    print(f"Tu nota final es: {notaFinal}")

    # Calificar la nota final
    if 4 <= notaFinal <= 5:
        print("Su nota final es excelente")
    elif 3 <= notaFinal < 4:
        print("Su nota final es buena")
    elif 2 <= notaFinal < 3:
        print("Su nota final es regular")
    elif notaFinal < 2:
        print("Su nota es insuficiente")
else:
    print("Ingresaste valores incorrectos, vuelve a intentarlo")