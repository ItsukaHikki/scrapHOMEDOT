# %%
import requests
import json 
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# %%
# Configuración del navegador
driver = webdriver.Chrome()
url = 'https://www.homedepot.com.mx/'
driver.get(url)
driver.maximize_window()

productos = []

# Configuración de espera para la ubicación
try:
    ubicación = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Usar mi ubicación']"))
    )
    ubicación.click()
except Exception as e:
    print("No se pudo encontrar el botón de ubicación:", e)
time.sleep(5)
# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Accesorios de pared" 1
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios de pared')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página
def extraer_datos_pagina_pared():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final
datos_totales1 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales1.extend(extraer_datos_pagina_pared())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Cortinas y cortineros" 2
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Cortinas y cortineros')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página
def extraer_datos_pagina_cortinas():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final
datos_totales2 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales2.extend(extraer_datos_pagina_cortinas())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Ganchos para toalla" 3
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Ganchos para toalla')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_ganchos():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales3 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales3.extend(extraer_datos_pagina_ganchos())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#3FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Jaboneras" 4
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Jaboneras')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_jaboneras():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales4 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales4.extend(extraer_datos_pagina_jaboneras())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#4FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Juegos de accesorios" 5
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Juegos de accesorios')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_Juegos_de_accesorios():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales5 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales5.extend(extraer_datos_pagina_Juegos_de_accesorios())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#5FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Organizadores para baño" 6
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Organizadores para baño')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_Organizadores_para_baño():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales6 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales6.extend(extraer_datos_pagina_Organizadores_para_baño())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#6FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Porta papel" 7
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Porta papel')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_Porta_papel():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales7 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales7.extend(extraer_datos_pagina_Porta_papel())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#7FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Seguridad para baños" 8
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Seguridad para baños')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_Seguridad_para_baños():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales8 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales8.extend(extraer_datos_pagina_Seguridad_para_baños())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#8FINAL

# Navegación en "Departamentos" > "Baños" > "Accesorios para baño" > "Toalleros" 9
try:
    departamentos_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='Departamentos' and contains(text(), 'Departamentos')]"))
    )
    departamentos_button.click()
    
    baños_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[@id='menu_dept_10003' and contains(text(),'Baños')]"))
    )
    baños_button.click()
    
    accesorios_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Accesorios para baño')]"))
    )
    accesorios_button.click()
    
    pared_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Toalleros')]"))
    )
    pared_button.click()
except Exception as e:
    print("Error en navegación del menú:", e)

# Función para extraer datos de la página, esta funcion siempre cambia de nombre
def extraer_datos_pagina_Toalleros():
    productos = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    product_container = soup.find('div', class_='product-listing-container productListingWidget top-margin-3')
    
    if product_container:
        items = product_container.find_all('div', class_='styled--productcard-container')
        for item in items:
            nombre = item.find('span', class_='product-name').text.strip() if item.find('span', class_='product-name') else 'N/A'
            precio_actual = item.find('p', class_='product-price').text.strip()[:-2] if item.find('p', class_='product-price') else 'N/A'
            precio_anterior = item.find('p', class_='colorGray300Line').text.strip()[:-2] if item.find('p', class_='colorGray300Line') else 'N/A'
            
            productos.append({
                'Nombre': nombre,
                'Precio Actual': precio_actual,
                'Precio Anterior': precio_anterior
            })
    return productos

# Bucle para extraer datos y navegar por las páginas hasta llegar al final, la variable siempre cambia de nombre
datos_totales9 = []
while True:
    time.sleep(2)  # Espera extra para garantizar carga completa de la página
    datos_totales9.extend(extraer_datos_pagina_Toalleros())
    
    try:
        # Verificar si el botón "Siguiente" está deshabilitado antes de hacer clic
        siguiente_boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'arrow-button') and .//p[text()='Siguiente']]"))
        )
        
        # Si el botón "Siguiente" está deshabilitado, terminamos el bucle
        if "disabled" in siguiente_boton.get_attribute("class"):
            print("Última página alcanzada.")
            break
        
        # Hacer clic en el botón "Siguiente" si está habilitado
        siguiente_boton.click()
        time.sleep(2)  # Tiempo para asegurar carga completa
    except Exception as e:
        print("No se pudo hacer clic en el botón 'Siguiente':", e)
        break
#9FINAL

# Cerrar el navegador
driver.quit()

# Convertir a DataFrames
df_datos1 = pd.DataFrame(datos_totales1)
df_datos2 = pd.DataFrame(datos_totales2)
df_datos3 = pd.DataFrame(datos_totales3)
df_datos4 = pd.DataFrame(datos_totales4)
df_datos5 = pd.DataFrame(datos_totales5)
df_datos6 = pd.DataFrame(datos_totales6)
df_datos7 = pd.DataFrame(datos_totales7)
df_datos8 = pd.DataFrame(datos_totales8)
df_datos9 = pd.DataFrame(datos_totales9)
# Guardar en distintas hojas del mismo archivo Excel
with pd.ExcelWriter("Accesorios_para_baño.xlsx") as writer:
    df_datos1.to_excel(writer, sheet_name="Accesorios de pared", index=False)
    df_datos2.to_excel(writer, sheet_name="Cortinas y cortineros", index=False)
    df_datos3.to_excel(writer, sheet_name="Ganchos para toalla", index=False)
    df_datos4.to_excel(writer, sheet_name="Jaboneras",index=False)
    df_datos5.to_excel(writer, sheet_name="Juegos de accesorios", index=False)
    df_datos6.to_excel(writer, sheet_name="Organizadores par baño", index=False)
    df_datos7.to_excel(writer, sheet_name="Porta papel", index=False)
    df_datos8.to_excel(writer, sheet_name="Seguridad para baños", index=False)
    df_datos9.to_excel(writer, sheet_name="Toalleros", index=False)

print("Archivo Excel con múltiples hojas creado con éxito.")


