import telebot
import time
import prueba
import aemet
import canciones
import os
import stat
import datetime
from os import remove


modTimesinceEpoc = os.path.getmtime("/Users/alejandrosanzperez/Desktop/botpy/testfile.txt")
modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))

añoMod = int(modificationTime[0:modificationTime.find("-")])
newMT = modificationTime[modificationTime.find("-")+1:len(modificationTime)]
mesMod =int(newMT[0:newMT.find("-")])
newMT = newMT[newMT.find("-")+1:len(newMT)]
diaMod = int(newMT[0:newMT.find(" ")])

now = datetime.datetime.now()
currentyear = (now.year)
currentmonth = (now.month)
currentday = (now.day)


print((currentday))
print("dia actual")
print((currentmonth))
print("mes actual")
print((currentyear))
print("año actual")

print((añoMod))
print("año modificacion")
print((diaMod))
print("dia modificacion")
print((mesMod))
print("mes modificacion")

if(currentday == diaMod | currentmonth == mesMod | currentyear == añoMod):
    file = open("testfile.txt", "w")
    file.write("0")
    file.close()
    file = open("testfile.txt", "r")
    numero = file.read()

print(numero)

