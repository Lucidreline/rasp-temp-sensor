from flask import Flask, jsonify 
import Adafruit_DHT
from time import sleep

sensor = Adafruit_DHT.DHT11
pin = 4

app = Flask(__name__) # creates an instance of Flask; the argument is the applications module/package

@app.route("/") # tells flask what url should trigger our function
def hello_world():
  return "<p>You found me! Qpz</p>" # this html will show on the user's browser

@app.route("/temperature")
def getTemperatureAndHumidity():
    nullResponse = True
    while nullResponse is True:
        humidity, temperature = Adafruit_DHT.read(sensor, pin)
        if temperature is None:
            sleep(1)
        else:
            return jsonify(
                temperature=temperature,
                humidity=humidity
    )

if __name__ == "__main__":
    app.run(debug=True)
