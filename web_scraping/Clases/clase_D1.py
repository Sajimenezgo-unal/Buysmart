from lib2to3.pgen2 import driver
from tabnanny import check
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
from selenium.webdriver import ActionChains
from datetime import datetime

class D1():
    def __init__(self, tipo):
        self.tipo = tipo

    def fetchinfo_D1(self):

        if self.tipo == "vegetales" or self.tipo == "all":
#############################################################################################################
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            action = ActionChains(browser)


            browser.get('https://domicilios.tiendasd1.com/')

            #Abrimos la seccion.
            browser.maximize_window()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.CLASS_NAME,"generalHeader__mainMenuBtn").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[1]").click()

            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[1]").click()
            time.sleep(5)

            seleccionarCarne = browser.find_element(By.XPATH,"//div[@class='ant-carousel']//descendant::div[@class='slick-slide slick-active slick-current']//h4[1]").click()

            htmlelement= browser.find_element(By.TAG_NAME,'html')

            time.sleep(3)
            htmlelement.send_keys(Keys.END)
            time.sleep(2)
            htmlelement.send_keys(Keys.END)
            time.sleep(3)
            htmlelement.send_keys(Keys.HOME)
            time.sleep(2)
            htmlelement.send_keys(Keys.HOME)
            time.sleep(3)

            seleccionarCarne = browser.find_element(By.XPATH,"//*[@id='app']/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[2]/div/ul/li[20]").click()
            time.sleep(5)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
            print("Que putas esta ocurriendo_0")
            try:
                siguientePagina= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[2]/a")
            except Exception as E:
                siguientePagina = 0
            print(siguientePagina)

            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            htmlelement= browser.find_element(By.TAG_NAME,'html')

            #Loop para iterar sobre los productos.
            while (siguientePagina!=None):
                time.sleep(5)
                htmlelement.send_keys(Keys.END)
                time.sleep(2)
                htmlelement.send_keys(Keys.END)
                time.sleep(5)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(2)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(5)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"prod__image__img "))):
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                    browser.implicitly_wait(20)

                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos.

                    price = browser.find_element(By.XPATH,"//div/div[2]/div/div[2]/div/div/div/div/div[1]/p")  
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.XPATH,'//div/div[2]/div/div[2]/div/div/div/div/p[1]')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    #PRUEBA PARA EXTRAER IMMAGENES, REVISAR.
                    imagen = browser.find_element(By.XPATH,"//img[@class='sc-jKJlTe hLtlKH carousel__img ']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    #PRUEBA PARA EXTRAER links, REVISAR.
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"D1","Vegetales y frutas",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se encuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                    browser.execute_script("window.scrollBy(0,50)") 
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
            #TENGO PROBLEMA PARA RESOLVER AQUI, LA PAGINA LLEGA A LA ULTIMA PAGINA DE LA SECCION Y ENCUENTRA EL BOTON Y LO UNDE, SOLO QUE EL BOTON NO HACE NADA, REVISAR.
            #Solucion: que si siguiente pagina es igual, si no ha cambiado, que no unda el boton sino que sea None  para que acabe el  loop
                print("Que putas esta ocurriendo")
                try:
                    siguientePagina = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[last()]/button").click()
                except Exception as E:
                    print("not exist")
                    siguientePagina = None

            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_D1_vegetalesverduras.csv', index = False)
            browser.close()

#############################################################################################################
        if self.tipo == "carnes" or self.tipo == "all":

            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            action = ActionChains(browser)


            browser.get('https://domicilios.tiendasd1.com/')

            #Abrimos la seccion de carnes.
            browser.maximize_window()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.CLASS_NAME,"generalHeader__mainMenuBtn").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()

            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()
            time.sleep(5)

            seleccionarCarne = browser.find_element(By.XPATH,"//div[@class='ant-carousel']//descendant::div[@class='slick-slide slick-active slick-current']//h4[1]").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']/descendant::li[@class='categories-menu__item'][5]").click()

            time.sleep(5)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
            try:
                siguientePagina= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[2]/a")
            except Exception as E:
                siguientePagina = 0
            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            htmlelement= browser.find_element(By.TAG_NAME,'html')
            #Loop para iterar sobre los productos carnicos.
            while (siguientePagina!=None):
                time.sleep(5)
                htmlelement.send_keys(Keys.END)
                time.sleep(5)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(5)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"prod__image__img "))):
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                    browser.implicitly_wait(20)

                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos.
                    price = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[1]/p")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/p[1]')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    #PRUEBA PARA EXTRAER IMMAGENES, REVISAR.
                    imagen = browser.find_element(By.XPATH,"//img[@class='sc-jKJlTe hLtlKH carousel__img ']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    #PRUEBA PARA EXTRAER links, REVISAR.
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"D1","Carnes",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                    browser.execute_script("window.scrollBy(0,50)") 
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                try:
                    siguientePagina = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[last()]/button").click()
                except Exception as E:
                    print("not exist")
                    siguientePagina = None
            
            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_D1_pescadomarisco.csv', index = False)
            browser.close()

        ###########Seccion carnes pollo#############

            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            browser.get('https://domicilios.tiendasd1.com/')

            #Abrimos la seccion de carnes.
            browser.maximize_window()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.CLASS_NAME,"generalHeader__mainMenuBtn").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()

            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()
            time.sleep(5)

            seleccionarCarne = browser.find_element(By.XPATH,"//div[@class='ant-carousel']//descendant::div[@class='slick-slide slick-active slick-current']//h4[1]").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']/descendant::li[@class='categories-menu__item'][6]").click()

            time.sleep(5)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
            try:
                siguientePagina= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[2]/a")
            except Exception as E:
                siguientePagina = 0
            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            htmlelement= browser.find_element(By.TAG_NAME,'html')
            #Loop para iterar sobre los productos carnicos.
            while (siguientePagina!=None):
                time.sleep(5)
                htmlelement.send_keys(Keys.END)
                time.sleep(5)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(5)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"prod__image__img "))):
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                    browser.implicitly_wait(20)

                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos.
                    price = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[1]/p")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/p[1]')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    #PRUEBA PARA EXTRAER IMMAGENES, REVISAR.
                    imagen = browser.find_element(By.XPATH,"//img[@class='sc-jKJlTe hLtlKH carousel__img ']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    #PRUEBA PARA EXTRAER links, REVISAR.
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"D1","Carnes",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                    browser.execute_script("window.scrollBy(0,50)") 
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                try:
                    siguientePagina = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[last()]/button").click()
                except Exception as E:
                    print("not exist")
                    siguientePagina = None
            
            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_D1_pollo.csv', index = False)
            browser.close()

        ###########Seccion carnes res cerdo#############

            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            browser.get('https://domicilios.tiendasd1.com/')

            #Abrimos la seccion de carnes.
            browser.maximize_window()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.CLASS_NAME,"generalHeader__mainMenuBtn").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()

            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[6]").click()
            time.sleep(5)

            seleccionarCarne = browser.find_element(By.XPATH,"//div[@class='ant-carousel']//descendant::div[@class='slick-slide slick-active slick-current']//h4[1]").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']/descendant::li[@class='categories-menu__item']").click()

            time.sleep(5)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
            try:
                siguientePagina= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[2]/a")
            except Exception as E:
                siguientePagina = 0
            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            htmlelement= browser.find_element(By.TAG_NAME,'html')
            #Loop para iterar sobre los productos carnicos.
            while (siguientePagina!=None):
                time.sleep(5)
                htmlelement.send_keys(Keys.END)
                time.sleep(5)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(5)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"prod__image__img "))):
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                    browser.implicitly_wait(20)

                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos.
                    price = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div[1]/p")
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/p[1]')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    #PRUEBA PARA EXTRAER IMMAGENES, REVISAR.
                    imagen = browser.find_element(By.XPATH,"//img[@class='sc-jKJlTe hLtlKH carousel__img ']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    #PRUEBA PARA EXTRAER links, REVISAR.
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"D1","Carnes",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                    browser.execute_script("window.scrollBy(0,50)") 
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                
                try:
                    siguientePagina = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[last()]/button").click()
                except Exception as E:
                    print("not exist")
                    siguientePagina = None

            
            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_D1_rescerdo.csv', index = False)
            browser.close()

#############################################################################################################
        if self.tipo == "despensa" or self.tipo == "all":

            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

            action = ActionChains(browser)


            browser.get('https://domicilios.tiendasd1.com/')

            #Abrimos la seccion despensa.
            browser.maximize_window()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.CLASS_NAME,"generalHeader__mainMenuBtn").click()
            time.sleep(5)
            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[1]").click()

            seleccionarCarne = browser.find_element(By.XPATH,"//ul[@class='categories-menu']//li[1]").click()
            time.sleep(5)

            seleccionarCarne = browser.find_element(By.XPATH,"//div[@class='ant-carousel']//descendant::div[@class='slick-slide slick-active slick-current']//h4[1]").click()
            time.sleep(5)

            #Encontremos la longitud de elementos.
            productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

            try:
                siguientePagina= browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[2]/a")
            except Exception as E:
                siguientePagina = 0

            #Creamos el data frame.
            df = pd.DataFrame([[0,0,0,0,0,0]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])

            htmlelement= browser.find_element(By.TAG_NAME,'html')

            #Loop para iterar sobre los productos.
            while (siguientePagina!=None):
                time.sleep(5)
                htmlelement.send_keys(Keys.END)
                time.sleep(2)
                htmlelement.send_keys(Keys.END)
                time.sleep(5)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(2)
                htmlelement.send_keys(Keys.HOME)
                time.sleep(5)
                for i in range(len(browser.find_elements(By.CLASS_NAME,"prod__image__img "))):
                    #Es necesario predirle los elementos de nuevo en cada iteracion debido a que estos  pueden cambiar desde la primera iteracion hasta la ultima, por ende se puede caer en una excepcion de referencia.
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")

                    browser.implicitly_wait(20)

                    productos[i].click()

                    #Se obtiene el precio de cada uno de los productos.

                    price = browser.find_element(By.XPATH,"//div/div[2]/div/div[2]/div/div/div/div/div[1]/p")  
                    pricet = price.text
                    print("Price: " + price.text)

                    #Se encuentra el nombre del producto.
                    nombre = browser.find_element(By.XPATH,'//div/div[2]/div/div[2]/div/div/div/div/p[1]')
                    nombret = nombre.text
                    print("Nombre: " + nombre.text)

                    #PRUEBA PARA EXTRAER IMMAGENES, REVISAR.
                    imagen = browser.find_element(By.XPATH,"//img[@class='sc-jKJlTe hLtlKH carousel__img ']")
                    imagen_link = (imagen.get_attribute('src'))
                    imagen_link

                    #PRUEBA PARA EXTRAER links, REVISAR.
                    pagina = browser.current_url
                    pagina

                    #Se almacena la informacion en un data frame.
                    df_aux = pd.DataFrame([[nombret,pricet,"D1","Despensa",imagen_link,pagina]], columns=["Producto","Precio","Supermercado","Categoria","IMG","Pagina"])
                    df=df.append(df_aux, ignore_index=True)

                    #Se espera para volver a la pagina donde se enncuentran todos los productos.
                    browser.implicitly_wait(20)
                    browser.back()
                    browser.execute_script("window.scrollBy(0,50)") 
                    browser.implicitly_wait(20)
                    productos = browser.find_elements(By.CLASS_NAME,"prod__image__img ")
                    
            #Solucion: que si siguiente pagina es igual, si no ha cambiado, que no unda el boton sino que sea None  para que acabe el  loop
                
                try:
                    siguientePagina = browser.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[3]/div/ul/li[last()]/button")
                    if siguientePagina.is_enabled() is not True: siguientePagina = None
                    siguientePagina.click()
                except Exception as E:
                    print("Not exist")
                    siguientePagina = None

            df.to_csv('C:/Users/urbi1/Desktop/scrapy/Clases/Bases/PriceList_D1_despensa.csv', index = False)
            browser.close() 

        



