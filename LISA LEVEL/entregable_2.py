
  
import requests
import json
import time
import csv
import os
import errno

#Creamos el diccionario que albergará el conteo de las palabras. 
cuenta_palabras = {}

while True:
  URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
  respuesta = requests.get(url = URL)
  datos = respuesta.json()
    
  frase: str = datos[0]["quote"]
  personaje: str = datos[0]["character"]

  #Obtenemos la url de la imagen y la guardamos en el directorio

  imagen_url: str = datos [0]["image"]
  imagen_local = f'{personaje}.png'
  imagen = requests.get (imagen_url).content

    
  #Creamos carpetas para cada cliente en el que se introducirá su imagen.
  try:
      os.mkdir(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}")
      imagen_local = f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.png"

      dict_General = {"personaje": personaje, "frase": frase}
      with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/general.csv", 'a') as f: 
        a = csv.DictWriter(f, dict_General.keys())
        a.writerow(dict_General)


      #Cuando el personaje es Lisa o Homer, introducimos también el archivo .csv dentro de la carpeta.
      if personaje == "Lisa Simpson":
        dict_Lisa = {"personaje": personaje, "frase": frase}
        with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.csv", 'a') as h: 
          a = csv.DictWriter(h, dict_Lisa.keys())
          a.writerow(dict_Lisa)

      elif personaje == "Homer Simpson":
        dict_Homer = {"personaje": personaje, "frase": frase}
        with open (f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.csv", 'a') as g:
          a = csv.DictWriter (g, dict_Homer.keys())
          a.writerow(dict_Homer)

      with open(imagen_local, 'wb') as handler:
        handler.write(imagen)
        
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise
        

  #Con la función frase.split() separamos cada palabra y se guarda en lista
  palabras = frase.split()
  
  #Mediante el bucle for vamos actualizando el valor del diccionario
  for palabra in palabras:
    value = 0

    if palabra not in cuenta_palabras:
      cuenta_palabras[palabra] = value

    value = palabras.count(palabra)
    cuenta_palabras[palabra] += value

  #Creación del archivo .txt en el que se introducirá el conteo de las palabras
  with open ('/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/ContadorPalabras.txt', 'w') as cuentapalabras:
      for clave, valor in cuenta_palabras.items():
        cuentapalabras.write(f"\n{clave}: {valor}")
        
  time.sleep (0)
