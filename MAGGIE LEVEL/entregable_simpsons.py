
import requests
import time
import csv


while True:
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    respuesta = requests.get(url = URL)
    datos = respuesta.json()
    
    frase: str = datos[0]["quote"]
    personaje: str = datos[0]["character"]

    #Guardamos los datos en diccionarios y a partir de ahí creamos los archivos .csv

    dict_1 = {"personaje": personaje, "frase": frase}
    with open('General/General.csv', 'a') as f: 
        a = csv.DictWriter(f, dict_1.keys())
        a.writerow(dict_1)
    
    #Si el personaje es Lisa, crea una carpeta especial y un archivo .csv diferente

    if personaje == "Lisa Simpson":
        dict_2 = {"personaje": personaje, "frase": frase}
        with open(f'Lisa/{personaje}.csv', 'a') as h: 
            a = csv.DictWriter(h, dict_2.keys())
            a.writerow(dict_2)
    
    #Si el personaje es Homer, crea una carpeta especial y un archivo .csv diferente
    
    if personaje == "Homer Simpson":
        dict_3 = {"personaje": personaje, "frase": frase}
        with open (f'Homer/{personaje}.csv', 'a') as g:
            a = csv.DictWriter (g, dict_3.keys())
            a.writerow(dict_3)  
        
    time.sleep (30)


  

