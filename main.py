from clases import *

def main():
    dic_pac = {}
    dic_data = {}    
    sis = Manejo_data()    
    while True:
        print("""Sistema hospitalario, escojala opcion deseada
                        \r1.Ingresar paciente
                        \r2.Ingresar imagen JPG o PNG
                        \r3.Transformacion de imagen DICOM
                        \r4.Manipulacion de imagen JPG o PNG
                        \r5.Salir""")
        opcion = int(input("Ingrese la opcion deseada"))
        if opcion == 1:
            pac = Paciente()
            llave = input("Ingrese la llave con la que desea almacenar al paciente")
            ruta = input(r"Ingrese la ruta de la carpeta con los dicoms del paciente: ")
            sis.cargar_archivos(ruta,dic_pac,dic_data,llave,pac)
            print("Paciente ingresado correctamente")
            continue
        elif opcion == 2:
            llave = input("Ingrese la llave con la que desea almacenar la imagen")
            ruta = input(r"Ingrese la ruta de la imagen que desea guardar: ")            
            ingre_imag(dic_data,ruta,llave)
            print("Imagen guardada")
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
