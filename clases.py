import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pydicom
import dicom2nifti
import nilearn
import nilearn.plotting

def nombre_nif(nifti_directory, name_nif):
        cont = 1
        while True:
            nifti_name = f'{name_nif}{cont}'
            nifti_ruta = os.path.join(nifti_directory, nifti_name)
            if not os.path.exists(nifti_ruta):
                return nifti_name
            cont += 1

def ingre_imag(dicc,ruta,llave):
    imagen = cv2.imread(ruta)
    dicc[llave]=imagen

def nombre_imgr(carpeta = os.getcwd()):
    carpeta_nombre = 'img_r'
    carpeta = os.path.join(carpeta,carpeta_nombre)
    cont = 0
    for filename in os.listdir(carpeta):
        if filename.endswith('.JPG'):
            subcont = int(filename.split(".")[0].split("_")[-1])
            cont = max(cont, subcont)
    
    nuevo_cont = cont + 1
    nombre_archivo = f'Rotacion_{nuevo_cont}.JPG'
    return nombre_archivo


def rotacion(llave,grados,dic_data):
    if llave in dic_data:
        dicoms = dic_data[llave]
        print(f"Hay {len(dicoms)} imagenes relacionadas a la llave ingresada")
        selec = int(input("Ingrese el numero de la imagen que desea rotar: "))-1
        ds = dicoms[selec] 
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

        
        nombre_archivo = nombre_imgr()        
        ruta_guardado = os.path.join(os.getcwd(), f'img_r\{nombre_archivo}')
        cv2.imwrite(ruta_guardado, imagen_rotada)
        
        print(f'Imagen rotada guardada como: {nombre_archivo}')
    else:
        print(f'Error: No se encontro informacion para la llave {llave} en dic_data.')
        
class Paciente():
    def __init__(self,nombre='',edad='No aplica',identificacion = '',img=''):
        self._nombre = nombre
        self._edad = edad
        self._id = identificacion
        self._img = img
        self._data = []

    def getNombre(self):
        return self._nombre 
    def getId(self):
        return self._id
    def getEdad(self):
        return self._edad
    def getImg(self):
        return self._img
    def getData(self):
        return self._data

     
    def setNombre(self,n):
        self._nombre = n 
    def setId(self,i):
        self._id = i
    def setAge(self,e):
        self._edad = e
    def setImg(self,img):
        self._img = img
    def setData(self,info):
        self._data.append(info)        




class Manejo_data(Paciente):
    def __init__(self):
        super().__init__()  

    def cargar(self,ruta_pac,dic1,dic2,llave,paciente):        
        carpeta = os.listdir(ruta_pac)
        for ruta_dicom in carpeta:
            if ruta_dicom.endswith('.dcm'): 
                ruta_dicom = os.path.join(ruta_pac, ruta_dicom)
                dicom = pydicom.dcmread(ruta_dicom) 
                paciente.setData(dicom)
        data=paciente.getData()
        nombre = data[0].PatientName
        ID = data[0].PatientID    
        try:
            edad = data[0][ 0x0010 , 0x1010 ].value
        except:
            edad = 'No disponible' 
        paciente.setNombre(nombre)
        paciente.setId(ID)        
        paciente.setAge(edad)          
        nifti_directory = os.path.join(os.getcwd(),'nifti')
        os.makedirs(nifti_directory, exist_ok=True) 
        nifti_name = nombre_nif(nifti_directory, 'nifti')
        output_nifti_file = os.path.join(nifti_directory, nifti_name) 
        os.makedirs(output_nifti_file, exist_ok=True) 
        dicom2nifti.convert_directory(ruta_pac, output_nifti_file)
        archivos_nifti = os.listdir(output_nifti_file)
        ruta_imagen = os.path.join(output_nifti_file,archivos_nifti[0])
        imagen = nilearn.image.load_img(ruta_imagen)    
        paciente.setImg(imagen)                
        dic1[llave] = paciente
        dic2[llave] = data  

    def transformar_im(self,llave,tam_kernel, dic_data):             
        if llave in dic_data:
            imagen = dic_data[llave]            
            imagen1 = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            umbral=np.mean(imagen1)
            _, binarizada = cv2.threshold(imagen1, umbral, 255, cv2.THRESH_BINARY)
            #fijamos kernel cuadrado de 1
            kernel = np.ones((tam_kernel, tam_kernel), np.uint8)
            #Usamos MORPH_CLOSE para primero dilatacion y luego erosion
            morfologia = cv2.morphologyEx(binarizada, cv2.MORPH_CLOSE, kernel , iterations=1)
            texto = f'Imagen binarizada'
            morfologia = cv2.putText(morfologia, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (220, 0, 0), 2)
            #imagen original
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.imshow(imagen1, cmap='gray')
            plt.title("Imagen original")
            plt.axis('off')
            #imagen binarizada
            plt.subplot(1, 2, 2)
            plt.imshow(morfologia, cmap='gray')
            plt.title(f"Imagen binarizada Umbral: {umbral}, Tamaño Kernel: {tam_kernel}")
            plt.axis('off')
            plt.show()  
            llave2 = input("Ingrese la nueva llave con la que guardara la imagen modificada: ")          
            dic_data[llave2] = morfologia
            print("Imagen guardad satisfactoriamente")

        else:
            print(f'Error: No se encuentra informacion para la llave {llave} en dic_data.')


            

