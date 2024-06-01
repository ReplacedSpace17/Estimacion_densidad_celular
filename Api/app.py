# menu.py

def mostrar_menu():
    print("Menú Principal")
    print("1. Técnica de conteo celular")
    print("2. Procesamiento de Imágenes")
    print("3. Modelo de Regresion Lineal")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Por favor, ingrese una opción (0-3): "))
            if opcion == 0:
                print("Saliendo del programa...")
                break
            elif opcion == 1:
                from image_analysis import analizar_imagenes
                analizar_imagenes()
                
                # Aquí puedes agregar el código para la Opción 1
            elif opcion == 2:
                from image_process import procesar_imagen
                procesar_imagen()
                # Aquí puedes agregar el código para la Opción 2
            elif opcion == 3:
                from model_regresion_lineal import procesar_imagen
                procesar_imagen()
            else:
                print("Opción no válida, por favor intente nuevamente.")
        except ValueError:
            print("Entrada no válida, por favor ingrese un número del 0 al 3.")

if __name__ == "__main__":
    main()
