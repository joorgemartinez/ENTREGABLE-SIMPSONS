
  
import requests
import json
import time
import csv
import os
import errno
import matplotlib.pyplot as plt

#Creamos el diccionario que albergará el conteo de las palabras. 
cuenta_palabras = {}
iteraciones = 0

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
      os.mkdir(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/{personaje}")
      imagen_local = f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/{personaje}/{personaje}.png"

      dict_General = {"personaje": personaje, "frase": frase}
      with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/general.csv", 'a') as f: 
        a = csv.DictWriter(f, dict_General.keys())
        a.writerow(dict_General)


      #Cuando el personaje es Lisa o Homer, introducimos también el archivo .csv dentro de la carpeta.
      if personaje == "Lisa Simpson":
        dict_Lisa = {"personaje": personaje, "frase": frase}
        with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/{personaje}/{personaje}.csv", 'a') as h: 
          a = csv.DictWriter(h, dict_Lisa.keys())
          a.writerow(dict_Lisa)

      elif personaje == "Homer Simpson":
        dict_Homer = {"personaje": personaje, "frase": frase}
        with open (f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/{personaje}/{personaje}.csv", 'a') as g:
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
  with open ('/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/BART LEVEL/ContadorPalabras.txt', 'w') as cuentapalabras:
    for clave, valor in cuenta_palabras.items():
      cuentapalabras.write(f"\n{clave}: {valor}")

  names = []
  marks = []

      
  f = open('ContadorPalabras.txt','r')
  for row in f:
    row = row.split(' ')
    names.append(row[0])
    marks.append(int(row[1]))
    
  plt.bar(names, marks, color = 'g', label = 'File Data')

  time.sleep (0)
'''with open('ContadorPalabras.txt') as f:
    lines = f.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]
    plt.bar(x,y,color = 'r')
    
    '''
  
        
      
  
