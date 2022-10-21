from lib2to3.pgen2 import driver
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #Se activa la opción para poder ingresar información en un inputbox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import re
import numpy as np
import pandas as pd
from datetime import datetime

class Vaquita():
    def __init__(self, tipo):
        self.tipo = tipo
    
    def fetchinfo_vaquita(self):
#############################################################################################################        
        if self.tipo == "vegetales" or self.tipo == "all":
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            browser.get('https://lavaquita.co/')

            #Abrimos la seccion de vegetales.
            browser.maximize_window()
            seleccionarVegetales = browser.find_element(By.XPATH,"//*[@id='site-header-nav']/nav/ul[1]/li[2]/a").click()
            seleccionarVegetales = browser.find_element(By.XPATH,"//*[@id='site-header-nav']/nav/ul[1]/li[2]/a").click()


            browser.implicitly_wait(15)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")
            siguientePagina= browser.find_element(By.XPATH,"/html/body/main/div[1]/div[1]/div[3]/nav[2]/ul/li[1]")

            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])


            #Loop para iterar sobre los productos.
            while (siguientePagina!=None):  
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"productitem--image-link"))):
                    if i > len(productos)-1:
                        siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                        siguientePagina.click()
                        try:
                            borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                        except Exception as E:
                            print(E)
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")

                    #Se da click a cada uno de los productos
                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos, debe ser el ultimo span debido a que algunos productos pueden tener precio en promocio y sin promocion, el ultimo siempre es el actual.
                    price = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-product']/section/article/div[2]/div[1]/div[2]/div/div[2]/span[last()]")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.CLASS_NAME,'product-title')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    """ sku = browser.find_element(By.XPATH,"/html/body/main/div[1]/section/article/div[2]/div[1]/div[3]/span")
                    skut = sku.text
                    print("SKU: " + sku.text) """

                    imagen = browser.find_element(By.XPATH,"//img[@class='product-gallery--loaded-image']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"La vaquita","Vegetales y frutas",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                print("QUE PUTAS ESTA PASANDO")
                try:
                    siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                    siguientePagina.click()
                except NoSuchElementException:
                    print("Not exists")
                    siguientePagina = None
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)
            
            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_Lavaquita_vegetales.csv', index = False)
            browser.close()

###########################################################################################################        
        if self.tipo == "carnes" or self.tipo == "all":
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            browser.get('https://lavaquita.co/')

            #Abrimos la seccion de carnes.
            browser.maximize_window()
            seleccionarCarne = browser.find_element(By.XPATH,"/html/body/header/div/div[2]/nav/ul[1]/li[1]/a").click()
            seleccionarCarne = browser.find_element(By.XPATH,"/html/body/header/div/div[2]/nav/ul[1]/li[1]/a").click()


            browser.implicitly_wait(15)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")
            siguientePagina= browser.find_element(By.XPATH,"/html/body/main/div[1]/div[1]/div[3]/nav[2]/ul/li[1]")

            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])


            #Loop para iterar sobre los productos carnicos.
            while (siguientePagina!=None):
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)  
                for i in range(len(browser.find_elements(By.CLASS_NAME,"productitem--image-link"))):
                    if i > len(productos)-1:
                        siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                        siguientePagina.click()
                        try:
                            borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                        except Exception as E:
                            print(E)
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")

                    #Se da click a cada uno de los productos
                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos, debe ser el ultimo span debido a que algunos productos pueden tener precio en promocio y sin promocion, el ultimo siempre es el actual.
                    price = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-product']/section/article/div[2]/div[1]/div[2]/div/div[2]/span[last()]")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.CLASS_NAME,'product-title')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    """ sku = browser.find_element(By.XPATH,"/html/body/main/div[1]/section/article/div[2]/div[1]/div[3]/span")
                    skut = sku.text
                    print("SKU: " + sku.text) """

                    
                    imagen = browser.find_element(By.XPATH,"//img[@class='product-gallery--loaded-image']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"La vaquita","Carnes",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                
                try:
                    siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                    siguientePagina.click()
                except NoSuchElementException:
                    print("Not exists")
                    siguientePagina = None
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)  
            
            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_Lavaquita_carnes.csv', index = False)
            browser.close()
#############################################################################################################
        if self.tipo == "despensa" or self.tipo == "all":

            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            browser.get('https://lavaquita.co/')

            #Abrimos la seccion de despensa.
            browser.maximize_window()
            seleccionarSnack = browser.find_element(By.XPATH,"//*[@id='site-header-nav']/nav/ul[1]/li[4]/a").click()
            seleccionarSnack = browser.find_element(By.XPATH,"//*[@id='site-header-nav']/nav/ul[1]/li[4]/a").click()


            browser.implicitly_wait(15)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")
            siguientePagina= browser.find_element(By.XPATH,"/html/body/main/div[1]/div[1]/div[3]/nav[2]/ul/li[1]")

            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            #Loop para iterar sobre los productos.
            while (siguientePagina!=None):  
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"productitem--image-link"))):
                    if i > len(productos)-1:
                        siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                        siguientePagina.click()
                        try:
                            borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                        except Exception as E:
                            print(E)
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"productitem--image-link")

                    #Se da click a cada uno de los productos
                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos, debe ser el ultimo span debido a que algunos productos pueden tener precio en promocio y sin promocion, el ultimo siempre es el actual.
                    price = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-product']/section/article/div[2]/div[1]/div[2]/div/div[2]/span[last()]")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.CLASS_NAME,'product-title')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    """ sku = browser.find_element(By.XPATH,"/html/body/main/div[1]/section/article/div[2]/div[1]/div[3]/span")
                    skut = sku.text
                    print("SKU: " + sku.text) """

                    imagen = browser.find_element(By.XPATH,"//img[@class='product-gallery--loaded-image']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"La vaquita","Despensa",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se encuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                try:
                    siguientePagina = browser.find_element(By.XPATH,"//*[@id='shopify-section-static-collection']/div[1]/div[3]/nav[2]/ul/li[last()]/a")
                    siguientePagina.click()
                except NoSuchElementException:
                    print("Not exists")
                    siguientePagina = None
                try:
                    borrar = browser.find_element(By.CLASS_NAME,"product-recently-viewed-clear").click()
                except Exception as E:
                    print(E)


            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_Lavaquita_snacks.csv', index = False)
            browser.close()
