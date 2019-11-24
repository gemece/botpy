def cache(cancion):
    directorio = './cache'
    cancion = cancion.lower()
    cancion = cancion.strip()
    for root, dir, ficheros in os.walk(directorio):
        for fichero in ficheros:
            fichero = fichero.strip()
            if(cancion in fichero.lower()):
                rutai = root+"/"+fichero
                shutil.copy(rutai, './mp3')
                return 1

    return 0