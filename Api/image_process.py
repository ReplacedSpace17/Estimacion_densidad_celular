# Función para procesar la imagen y calcular la densidad celular
import cv2
import numpy as np
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Función para procesar la imagen de la ROI
def procesar_ROI(image):
    # Separar las bandas RGB
    blue_channel, green_channel, red_channel = cv2.split(image)

    # Calcular la banda de intensidad (I)
    intensity_channel = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Calcular los promedios de píxeles por columna de cada banda
    blue_avg_column = np.mean(blue_channel, axis=0)
    green_avg_column = np.mean(green_channel, axis=0)
    red_avg_column = np.mean(red_channel, axis=0)
    intensity_avg_column = np.mean(intensity_channel, axis=0)

    # Calcular el promedio por banda
    blue_avg = np.mean(blue_avg_column)
    green_avg = np.mean(green_avg_column)
    red_avg = np.mean(red_avg_column)
    intensity_avg = np.mean(intensity_avg_column)

    return blue_avg, green_avg, red_avg, intensity_avg

# Función para cargar la imagen con un botón
def cargar_imagen():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    file_path = filedialog.askopenfilename()  # Abrir el cuadro de diálogo para seleccionar archivo
    if file_path:
        # Leer la imagen
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir a formato RGB
        return image
    else:
        return None


def procesar_imagen():
    # Cargar la imagen
    image = cargar_imagen()
    if image is None:
        messagebox.showerror("Error", "No se pudo cargar la imagen.")
        return

    # Definir las coordenadas de la ROI (centrada en la imagen, 250x250 píxeles)
    height, width = image.shape[:2]
    roi_x = int((width - 250) / 2)
    roi_y = int((height - 250) / 2)
    roi_width = 250
    roi_height = 250

    # Extraer la ROI
    roi = image[roi_y:roi_y+roi_height, roi_x:roi_x+roi_width]

    # Procesar la imagen de la ROI
    red_avg, green_avg, blue_avg, intensity_avg = procesar_ROI(roi)

    # Solicitar al usuario el número de células y otros datos
    num_celulas = int(input("Número de células: "))
    volumen_muestra = 0.03333
    temperatura = float(input("Temperatura: "))
    ph = float(input("pH: "))

    # Calcular la densidad celular
    densidad_celular = num_celulas / volumen_muestra

    # Obtener la fecha y hora actual
    fecha_muestreo = datetime.now().strftime("%d/%m/%Y")
    hora_actual = datetime.now()
    hora_muestreo_str = hora_actual.strftime("%H:%M:%S")

    # Crear el diccionario con los datos
    data = {
        "Red_Band": red_avg,
        "Green_Band": green_avg,
        "Blue_Band": blue_avg,
        "Intensity_Band": intensity_avg,
        "Temperatura": temperatura,
        "pH": ph,
        "Muestra(mL)": volumen_muestra,
        "Numero_Celulas": num_celulas,
        "Densidad_Celular": densidad_celular,
        "Fecha_Muestreo": fecha_muestreo,
        "Hora_Muestreo": hora_muestreo_str,
        "Cultivo": "Cultivo 1"
    }

    # Convertir el diccionario a formato JSON
    json_data = json.dumps(data, indent=4)

    # Mostrar el JSON
    print(json_data)

    # Retornar al menú principal
    from app import mostrar_menu
    mostrar_menu()
