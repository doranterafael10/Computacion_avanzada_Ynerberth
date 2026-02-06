def mostrar_menu() -> None:
    print("\n___ Menú de Postres ___")
    print("1. Crear Menú de postres.txt")
    print("2. Agregar postre al Menú")
    print("3. Leer Menú de postres")
    
    print("0. Salir")

def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            with open("postres.txt", "w") as archivo:
                archivo.write("Menú de postres \n")
                print("Menú de postres.txt creado")
        elif opcion == "2":
            with open("postres.txt", "a") as archivo:
                postre = input("Ingrese el nombre del postre: ")
                archivo.write(postre + '\n')
                print("Postre agregado al Menú")
        elif opcion == "3":
            with open("postres.txt", "r") as archivo:
                contenido = archivo.read()
                print("Lista de postres:\n" + contenido)
        elif opcion == "0":
            print("Saliendo del programa... ")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()