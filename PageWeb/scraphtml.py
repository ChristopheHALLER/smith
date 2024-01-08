import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
import time

app = Flask(__name__)

def scrap_sensor1temp():
    url = "http://192.168.1.91:81/state.xml"
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
            return {
                "sensor1temp": sensor1temp_value,
                "sensor2temp": sensor2temp_value,
                "count1": count1_value,
                "count2": count2_value,
            }
        else:
            return {"error": "La balise <sensor1temp> n'a pas été trouvée."}
    else:
        return {"error": "La balise <datavalues> n'a pas été trouvée."}

@app.route('/')
def index():
    sensor_data = scrap_sensor1temp()
    return render_template('index.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
