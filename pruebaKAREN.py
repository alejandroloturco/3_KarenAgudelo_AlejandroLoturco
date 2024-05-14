from clases import *       

def nombre_imgr(carpeta):    
    for filename in os.listdir(carpeta):
        if filename.endswith('.JPG'):
            subcont = int(filename.split(".")[0].split("_")[-1])
            cont = max(cont, subcont)
        nuevo_cont = cont + 1
        nombre_archivo = f'Rotacion_{nuevo_cont}.JPG'
        return nombre_archivo

def rotacion(ID,grados,dic_data):
    if ID in dic_data:
        dicom = dic_data[ID]
        ds = pydicom.dcmread(dicom[0])
        img = ds.pixel_array

        if grados not in [90,180,270]:
            print("Los grados de rotacion deben ser 90,180 o 270")
            return False 
        img_rgb = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2RGB)
        row, col, _ = img_rgb.shape
        MR = cv2.getRotationMatrix2D((col/2, row/2), grados, 1) 
        imagen_rotada = cv2.warpAffine(img_rgb, MR, (col, row))
        original_title = f'Imagen DICOM Original ({llave})'
        rotada_title = f'Imagen Rotada ({grados} grados)'
        plt.subplot(1, 2, 1)
        plt.imshow(img_rgb, cmap='gray')
        plt.title(original_title)
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(imagen_rotada)
        plt.title(rotada_title)
        plt.axis('off')
        plt.show()

        carpeta = r'C:\Users\Karen\Desktop\QUIZ3\3_KarenAgudelo_AlejandroLoturco\img_r'
        nombre_archivo = nombre_imgr(carpeta)
        ruta_guardado = os.path.join(carpeta, nombre_archivo)
        cv2.imwrite(ruta_guardado, imagen_rotada)
        
        print(f'Imagen rotada guardada como: {nombre_archivo}')
    else:
        print(f'Error: No se encontró información para el ID {ID} en dic_data.')
  
            
if __name__ == '__main__':

    dic_pac = {}
    dic_data = {}
    sis = Manejo_data()

    ruta_d = r'C:\Users\Karen\Desktop\QUIZ3\datos\T2'  
    
    pac = Paciente()  
    llave ='holi'
    grados = 90
    sis.cargar_archivos(ruta_d,dic_pac,dic_data,llave,pac)

    rotacion(llave,grados,dic_data)
    

