from clases import *       
 


if __name__ == '__main__':

    dic_pac = {}
    dic_data = {}
    sis = Manejo_data()

    ruta_d = r'C:\Users\alotu\Desktop\Escritorio\udea\programacion\informatica 2\Unidad 3\quiz 3\3_KarenAgudelo_AlejandroLoturco-1\datos\T2'  
    
    pac = Paciente()  
    llave ='holi'
    grados = 90
    sis.cargar_archivos(ruta_d,dic_pac,dic_data,llave,pac)

    rotacion(ruta_d,llave,grados,dic_data)
    

