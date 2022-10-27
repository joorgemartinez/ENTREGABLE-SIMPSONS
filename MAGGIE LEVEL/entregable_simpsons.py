
import requests
import time
import csv


general_list = []
homer_list = []
lisa_list = []

while True:
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    respuesta = requests.get(url = URL)
    datos = respuesta.json()
    
    frase: str = datos[0]["quote"]
    personaje: str = datos[0]["character"]
    
    if personaje == "Lisa Simpson":
        general_list.append((personaje, frase))
        lisa_list.append((personaje,frase))
        
    elif personaje == "Homer Simpson":
        general_list.append((personaje,frase))
        homer_list.append((personaje,frase))
        
    else:
        general_list.append((personaje,frase))

    #Guardamos los datos en diccionarios y a partir de ahí creamos los archivos .csv

    dict_1 = {"personaje": personaje, "frase": frase}
    with open('General/General.csv', 'a') as f: 
        a = csv.DictWriter(f, dict_1.keys())
        a.writerow(dict_1)
    
    if personaje == "Lisa Simpson":
        dict_2 = {"personaje": personaje, "frase": frase}
        with open('Lisa/Lisa.csv', 'a') as h: 
            a = csv.DictWriter(h, dict_2.keys())
            a.writerow(dict_2)
    
    if personaje == "Homer Simpson":
        dict_3 = {"personaje": personaje, "frase": frase}
        with open ('Homer/Homer.csv', 'a') as g:
            a = csv.DictWriter (g, dict_3.keys())
            a.writerow(dict_3)  
        
    time.sleep (30)


  

