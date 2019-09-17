import requests, json

API_KEY = "5a704a445293e030d4057a43a8a605fc"


url = "http://api.openweathermap.org/data/2.5/forecast?"



def tiempo(city):

    #ciudad = input("Introduce ciudad : \n")
    ciudad = city
    url_final= url + "q=" + ciudad + "&APPID={}".format(API_KEY)


    respuesta = requests.get(url_final)
    x = respuesta.json()
    return x
    