from clases import *

def main():
    dic_pac = {}
    dic_data = {}    
    sis = Manejo_data()    
    while True:
        print("""Sistema hospitalario, escojala opcion deseada
                        \r1.Ingresar paciente
                        \r2.Ingresar imagen JPG o PNG
                        \r3.Rotacion de imagen DICOM
                        \r4.Manipulacion de imagen JPG o PNG
                        \r5.Salir""")
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            pac = Paciente()
            llave = input("Ingrese la llave con la que desea almacenar al paciente: ")
            ruta = input(r"Ingrese la ruta de la carpeta con los dicoms del paciente: ")
            sis.cargar_archivos(ruta,dic_pac,dic_data,llave,pac)
            print("Paciente ingresado correctamente")
            continue
        elif opcion == 2:
            llave = input("Ingrese la llave con la que desea almacenar la imagen: ")
            ruta = input(r"Ingrese la ruta de la imagen que desea guardar: ")            
            ingre_imag(dic_data,ruta,llave)
            print("Imagen guardada")
            continue
        elif opcion == 3:
            llave = input("Ingrese la llave con la que desea almacenar la imagen")
            ruta = input(r"Ingrese la ruta de la imagen que desea guardar: ") 
            grados = int(input("""Seleccione los grados que desea rotar la imagen
                               \r1-90°
                               \r2-180°
                               \r3-270°""")) 
            if grados == 1:
                grados = 90
            elif grados == 2:
                grados = 180
            elif grados == 3:
                grados = 270
            rotacion(ruta,llave,grados,dic_data)
            
            continue

        elif opcion == 4:
            llave = int(input("Ingrese la llave de la imagen JPG o PNG: "))
            kernel = int(input("Ingrese el tamaño del kernel"))
            umbral = input("Ingrese el umbral")
            sis.trasformar_im(llave, umbral, kernel, dic_data)
            continue

        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()
