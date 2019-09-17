from bs4 import BeautifulSoup
import requests, urllib3, time, json, datetime, os
from openpyxl import *



def tiempo(ciudad):
    mes = str(datetime.datetime.now().month)
    if(not os.path.isfile(mes + '.xlsx')):
        fichero = requests.get("http://www.ine.es/daco/daco42/codmun/codmunmapa.htm")
        bs = BeautifulSoup(fichero.text,'html.parser')
        encuentra = bs.find('a',{'class':'w'})

        url = "http://www.ine.es" + encuentra['href']

        r = requests.get(url, allow_redirects=True)
        
        open(mes + '.xlsx', 'wb').write(r.content)

    wb = load_workbook('fichero.xlsx')
    ws = wb.active
    cod = None
    for row in ws.iter_rows(min_row=2, max_col=5, values_only=True):
        r = row[4]
        if ciudad.lower() in r.lower():
            cod = row[1] + row[2]
            break

    if(cod is None):
        return None

    url = f"https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/{cod}"

    querystring = {"api_key": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJndWlsbGVybW9tdW5vemNyZXNwb0BnbWFpbC5jb20iLCJqdGkiOiI5N2QxMWI2NC0xZGRiLTRjZTgtYmIzNC0xNTk0YTRmNjVkZTMiLCJpc3MiOiJBRU1FVCIsImlhdCI6MTU2NDk5OTEzOSwidXNlcklkIjoiOTdkMTFiNjQtMWRkYi00Y2U4LWJiMzQtMTU5NGE0ZjY1ZGUzIiwicm9sZSI6IiJ9.-4Mw1sVVSJAmT8X9KqR9KZosEktdZhrcz5tBgZ4b32Q"}

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

    dato = response.json()['datos']

    print(dato)


    respuesta = requests.get(dato)
    x = respuesta.json()[0]
    return x
    #for i in x['prediccion']['dia']:
    #    fecha = i['fecha']
    #    print("Dia " + fecha)
    #    y = i['probPrecipitacion'][0]
    #    if(len(y)>1):
    #        print("{} H ---> Probabilidad de precipitacion {} %".format(y['periodo'],y['value']))
    #    else:
    #        print(
    #            "00-24 H ---> Probabilidad de precipitacion {} %".format(y['value']))
 #
    #    y = i['estadoCielo'][0]
    #    if(len(y) > 2):
    #        print("{} ---> {}".format(y['periodo'], y['descripcion']))
    #    else:
    #        print("00-24 H ---> {}".format(y['descripcion']))
    #    
    #    y = i['temperatura']
    #    print("Temperatura Maxima {}\nTemperatura Minima {}".format(y['maxima'], y['minima']))
    #    
    #    y = i['sensTermica']
    #    print("Sensacion Termica Maxima {}\nSensacion Termica Minima {}".format(y['maxima'], y['minima']))

    #    y = i['humedadRelativa']
    #    print("Humedad Maxima {} %\nHumedad Minima {} %\n".format(y['maxima'], y['minima']))


