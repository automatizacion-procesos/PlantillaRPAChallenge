import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


#----------------------------CONFIGURACIONES----------------------------------#

# Ruta donde se guardan los archivos descargados
RUTA_DESCARGAS = 'D:/Users/felipe.gonzalez/Downloads/challenge.xlsx'

# Xpaths de los campos del formulario que debemos llenar
CAMPOS_TEXTO = (
    '//input[@ng-reflect-name="labelFirstName"]',       # First Name
    '//input[@ng-reflect-name="labelLastName"]',        # Last Name
    '//input[@ng-reflect-name="labelCompanyName"]',     # Company Name
    '//input[@ng-reflect-name="labelRole"]',            # Role in Company
    '//input[@ng-reflect-name="labelAddress"]',         # Addres
    '//input[@ng-reflect-name="labelEmail"]',           # Email
    '//input[@ng-reflect-name="labelPhone"]'            # Phone Number
)

# Xpath botón para continuar con el siguiente formulario
XPATH_BOTON_SUBMIT = '//input[@value="Submit"]'

# Xpath del botón de descarga del archivo
XPATH_BOTON_DESCARGA = '//a[@href="./assets/downloadFiles/challenge.xlsx"]'

# Xpath del botón que inicia el reto
XPATH_BOTON_START = '//button[contains(., Start)]'

# Xpath del mensaje final del reto
XPATH_MENSAJE_RESULTADO = '//div[@class="message2"]'

# Dirección del sitio web del reto
URL_RETO = 'https://rpachallenge.com/'


# Instalamos el navegador de chrome
chromedriver_autoinstaller.install() 

# Definición de objeto que inicia y detiene el ChromeDriver
s = Service()

# # Inicializar las opciones
# opciones_chrome = Options()
# #Para evitar que se genere en consola el error por el bluetooth bloqueado:
# opciones_chrome.add_experimental_option('excludeSwitches', ['enable-logging']) 







#-------------------------------INICIO----------------------------------------#





#-------------------------------PROCESO----------------------------------------#





#---------------------------------FIN-----------------------------------------#


