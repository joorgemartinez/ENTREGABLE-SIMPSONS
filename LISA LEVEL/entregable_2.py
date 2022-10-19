
  
import requests
import json
import time
import csv
import os
import errno


general_list = []
homer_list = []
lisa_list = []

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

  if personaje == "Lisa Simpson":
    general_list.append((personaje, frase))
    lisa_list.append((personaje,frase))
        
  elif personaje == "Homer Simpson":
    general_list.append((personaje,frase))
    homer_list.append((personaje,frase))
        
  else:
    general_list.append((personaje,frase))
    

  try:
      os.mkdir(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}")
      imagen_local = f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.png"

      if personaje == "Lisa Simpson":
        dict_1 = {"personaje": personaje, "frase": frase}
        with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.csv", 'a') as h: 
          a = csv.DictWriter(h, dict_1.keys())
          a.writerow(dict_1)

      elif personaje == "Homer Simpson":
        dict_2 = {"personaje": personaje, "frase": frase}
        with open (f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/{personaje}/{personaje}.csv", 'a') as g:
          a = csv.DictWriter (g, dict_2.keys())
          a.writerow(dict_2)

      else:
        dict_3 = {"personaje": personaje, "frase": frase}
        with open(f"/Users/jorgemartinezcanet/Documents/GitHub/ENTREGABLE-SIMPSONS/LISA LEVEL/general.csv", 'a') as f: 
          a = csv.DictWriter(f, dict_3.keys())
          a.writerow(dict_3)
      
      with open(imagen_local, 'wb') as handler:
        handler.write(imagen)
        
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise
        
    time.sleep (0)
