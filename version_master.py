#LIBREIAS UTILIZADAS
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image
import cv2
import numpy as np
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from io import BytesIO
import sys
import time
#import subprocess #Para ejecutar varios procesos al mismo tiempo

# Configurar Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Configurar opciones de Chrome
options = Options()
options.headless = True
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Iniciar un navegador Chrome en modo headless
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()

# Capturar la sección de la página web utilizando Selenium
# Obtener el tamaño de la página web
width = driver.execute_script("return Math.max( document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth );")
height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

# Establecer las dimensiones de la ventana del navegador
driver.set_window_size(width, height)
#Borrar el contenido del archivo output                        
open("output.txt", "w").close()
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'#Ruta donde se encuentre instalado Tesseract
#proc = subprocess.Popen(['python', 'otro_script.py']) #Prefiero abrir y cerrar el txt manualmente, este código permitía ejecutar el otput del txt en otro .py al mismo tiempo

while True:
    try:
        # Capturar screenshot
        screenshot = driver.get_screenshot_as_png()
        with open(r"C:\Ruta\screenshot.png", 'wb') as f: f.write(screenshot)

        # Procesar screenshot
        image = Image.open('screenshot.png').convert('L')
        text = pytesseract.image_to_string(image,lang='spa')

        # Escribir resultado en archivo de texto
        with open("output.txt", 'a') as f:
            f.write(f"{text}\n")
        
        # Esperar 5 segundos antes de capturar otra screenshot
        time.sleep(5)
        open("output.txt", "w").close()
    except KeyboardInterrupt:
        print("Detenido por el usuario")
        break
    #except:
    #    print("Error al procesar la imagen")
    #    break