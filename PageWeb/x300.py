import requests
from bs4 import BeautifulSoup
import time

def scrap_sensor1temp():
    
    url = "http://192.168.1.91:81/state.xml"

    # Obtenir le contenu de la page web
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml-xml")
    datavalues_tag = soup.find("datavalues")
    
    if datavalues_tag:
      
        sensor1temp_tag = datavalues_tag.find("sensor1")
        sensor2temp_tag = datavalues_tag.find("sensor2")
        count1 = datavalues_tag.find("count1")
        count2 = datavalues_tag.find("count2")
        
        if sensor1temp_tag:  
            sensor1temp_value = sensor1temp_tag.text.strip()
            sensor2temp_value = sensor2temp_tag.text.strip()
            count1_value = count1.text.strip()
            count2_value = count2.text.strip()
            print(f"Temperature Exerieure: {sensor1temp_value}")
            print(f"Temperature Salle Musculation: {sensor2temp_value}")
            print(f"Eau: {count1_value}")
            print(f"Gaz: {count2_value}")
        else:
            print("La balise <sensor1temp> n'a pas été trouvée.")
    else:
        print("La balise <datavalues> n'a pas été trouvée.")

while True:
    scrap_sensor1temp()
    time.sleep(4)
    print("Nous attendons 1 secondes")
