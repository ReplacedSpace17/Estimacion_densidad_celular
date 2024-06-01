# Estimación de Densidad Celular

Este proyecto tiene como objetivo estimar la densidad celular a partir de imágenes utilizando un modelo de regresión lineal. El programa permite al usuario cargar una imagen, seleccionar una región de interés (ROI) y calcular la densidad celular basada en las características de la imagen y valores adicionales de temperatura y pH.

## Requisitos

Asegúrate de tener instalado Python 3.7 o superior. Las siguientes bibliotecas de Python son necesarias para ejecutar el proyecto:

- opencv-python
- numpy
- scikit-learn
- tkinter

## Instalación

1. Clona el repositorio en tu máquina local:

    ```sh
    git clone https://github.com/ReplacedSpace17/Estimacion_densidad_celular
    cd Estimacion_densidad_celular/Api
    ```

2. Activa el entorno virtual:

    ```sh
    source venv/bin/activate
    ```

3. Instala las dependencias necesarias:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```sh
    python app.py
    ```

2. Carga una imagen utilizando el botón "Cargar Imagen".

3. Se te pedirá ingresar la temperatura y el pH. Proporciona estos valores cuando se te solicite.

4. La aplicación procesará la imagen y calculará los valores medios de las bandas de color (RGB) y la intensidad de la imagen en la región de interés (ROI).

5. El modelo de regresión lineal utilizará estos valores, junto con la temperatura y el pH proporcionados, para predecir la densidad celular.

6. La densidad celular predicha se mostrará en la consola.

## Estructura del Proyecto

