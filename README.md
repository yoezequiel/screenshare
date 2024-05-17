# ScreenShare

ScreenShare es una aplicación web desarrollada en Python utilizando el framework Flask y OpenCV para permitir la transmisión en tiempo real de la cámara y pantalla de manera Offline.

## Funcionalidades

-   **Transmisión de la cámara**: La aplicación captura el video en tiempo real de la cámara conectada al dispositivo y lo transmite a través de una página web.
-   **Captura de pantalla**: Además de la transmisión de la cámara, la aplicación permite capturar la pantalla del dispositivo y mostrarla en la misma página web.
-   **Botón de pantalla completa**: Los usuarios pueden activar el modo de pantalla completa para la visualización de la captura de pantalla.

## Requisitos

-   Python 3.x
-   Flask
-   OpenCV
-   Pillow
-   Flask-SocketIO

## Instalación

1. Clona o descarga este repositorio en tu máquina local.

    ```bash
    git clone https://github.com/yoezequiel/screenshare.git
    ```

2. Instala las dependencias utilizando el siguiente comando:

    ```
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación Python utilizando el siguiente comando:

    ```
    python app.py
    ```

2. Abre tu navegador web y accede a la dirección `http://localhost:5000`.

## Comandos Adicionales

-   Para desactivar la transmisión de la cámara, puedes ejecutar la aplicación con el siguiente argumento:

    ```
    python app.py --camera off
    ```

-   Para cambiar el puerto, puede ejecutar la aplicacion con el siguiente argumento
    ```
    python app.py --port 8080
    ```

## Contribución

Las contribuciones son bienvenidas. Si encuentras un error o deseas mejorar la funcionalidad, no dudes en abrir un issue o enviar un pull request.
