# image_analysis.py

import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

def cargar_imagen():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter

    file_path = filedialog.askopenfilename()  # Abrir el cuadro de diálogo para seleccionar archivo
    if file_path:
        return cv2.imread(file_path)
    else:
        return None

def analizar_imagenes():
    # Cargar la imagen desde un archivo usando un botón
    img = cargar_imagen()
    if img is None:
        print("No se pudo cargar la imagen.")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar un desenfoque gaussiano para reducir el ruido
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Usar un umbral adaptativo para binarizar la imagen
    adaptive_thresh = cv2.adaptiveThreshold(blurred, 255,
                                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                            cv2.THRESH_BINARY_INV, 11, 2)

    # Encontrar contornos
    contours, _ = cv2.findContours(adaptive_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filtrar contornos por área para eliminar ruido y pequeños artefactos
    min_area = 100
    max_area = 8000
    filtered_contours = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]

    # Dibujar los contornos detectados en la imagen
    img_contours = img.copy()
    cv2.drawContours(img_contours, filtered_contours, -1, (0, 255, 0), 2)

    # Mostrar la imagen con los contornos detectados
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(img_contours, cv2.COLOR_BGR2RGB))
    plt.title(f'Número de células detectadas: {len(filtered_contours)}')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    analizar_imagenes()
