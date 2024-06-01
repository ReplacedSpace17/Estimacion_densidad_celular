import cv2
import numpy as np
import json
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from sklearn.linear_model import LinearRegression

BandRed_prediccion = 0.0
BandGreen_prediccion = 0.0
BandBlue_prediccion = 0.0
BandIntensity_prediccion = 0.0
Temperature_prediccion = 0.0
pH_prediccion = 0.0

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
    file_path = filedialog.askopenfilename()  # Abrir el cuadro de diálogo para seleccionar archivo
    if file_path:
        # Leer la imagen
        image = cv2.imread(file_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convertir a formato RGB
        return image
    else:
        return None

# Función para procesar la imagen y calcular la densidad celular
def procesar_imagen():
    global BandRed_prediccion, BandGreen_prediccion, BandBlue_prediccion, BandIntensity_prediccion, Temperature_prediccion, pH_prediccion

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

    # Pedir al usuario los valores de temperatura y pH
    temperatura = float(input("Temperatura: "))
    ph = float(input("pH: "))

    # Actualizar las variables globales
    BandRed_prediccion = red_avg
    BandGreen_prediccion = green_avg
    BandBlue_prediccion = blue_avg
    BandIntensity_prediccion = intensity_avg
    Temperature_prediccion = temperatura
    pH_prediccion = ph

    # Entrenar el modelo y realizar la predicción
    entrenar_y_predecir()



# Función para entrenar el modelo y realizar la predicción
def entrenar_y_predecir():
    global BandRed_prediccion, BandGreen_prediccion, BandBlue_prediccion, BandIntensity_prediccion, Temperature_prediccion, pH_prediccion

    # Leer los datos del archivo JSON
    with open('datos.json') as f:
        datos = json.load(f)

    # Inicializar listas para almacenar los valores de cada banda y densidad celular
    red_band_values = []
    green_band_values = []
    blue_band_values = []
    intensity_values = []
    temperature_values = []
    ph_values = []
    density_values = []

    # Iterar sobre los datos y extraer los valores de cada banda y densidad celular
    for dato in datos:
        red_band_values.append(dato["Red_Band"])
        green_band_values.append(dato["Green_Band"])
        blue_band_values.append(dato["Blue_Band"])
        intensity_values.append(dato["Intensity_Band"])
        temperature_values.append(dato["Temperatura"])
        ph_values.append(dato["pH"])
        density_values.append(dato["Densidad_Celular"])

    # Convertir listas a arrays numpy
    red_band_array = np.array(red_band_values)
    green_band_array = np.array(green_band_values)
    blue_band_array = np.array(blue_band_values)
    intensity_array = np.array(intensity_values)
    temperature_array = np.array(temperature_values)
    ph_array = np.array(ph_values)
    density_array = np.array(density_values)

    # Transponer los arrays de valores de las bandas RGBI, temperatura y pH
    X = np.array([red_band_array, green_band_array, blue_band_array, intensity_array, temperature_array, ph_array]).T

    # Valor de la densidad celular
    y = density_array

    # Inicializar y ajustar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X, y)

    # Coeficientes de regresión (pendientes)
    coeficientes = model.coef_

    # Intercepción
    intercepcion = model.intercept_

    # Calcular el coeficiente de determinación (R^2)
    r_cuadrado = model.score(X, y)

    # Mostrar resultados del modelo entrenado
    print("Coeficientes de regresión (pendientes):", coeficientes)
    print("Intercepción:", intercepcion)
    print("Coeficiente de determinación (R^2):", r_cuadrado)

    # Realizar la predicción utilizando el modelo entrenado
    X_new = np.array([[BandRed_prediccion, BandGreen_prediccion, BandBlue_prediccion, BandIntensity_prediccion, Temperature_prediccion, pH_prediccion]])
    predicted_density = model.predict(X_new)
    print("Densidad celular predicha:", predicted_density[0])


# Ejecutar el bucle de la interfaz gráfica

