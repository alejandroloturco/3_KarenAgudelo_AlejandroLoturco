from clases import *
dic_data = {}
dic_pac = {}

def main():    
    while True:
        print("""Sistema hospitalario, escojala opcion deseada
                        \r1.Ingresar paciente
                        \r2.Ingresar imagen JPG o PNG
                        \r3.Transformacion de imagen DICOM
                        \r4.Manipulacion de imagen JPG o PNG
                        \r5.Salir""")
        opcion = int(input("Ingrese la opcion deseada"))
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    main()