import serial
import time

def recup_position():

    '''
        Code qui permet la récupération d'une trame GLL au complet afin de calculer la position
    '''

    port_serie = "/dev/ttyACM0" # Permet l'accès au port série grâce au module Serial
    try:
        microbit = serial.Serial(port_serie, 115200, timeout=0.1) # Permet d'écouter tout ce qui est reçu sur la carte microbit
        print("A L'ÉCOUTE D'UNE TRAME...")
        buffer = ""
        GGA = []
        essaye_GGA = False
        while True:
            if microbit.in_waiting > 0:
                buffer = microbit.read(microbit.in_waiting).decode('utf-8', errors='ignore')
                if "\n" in buffer:
                    lignes = buffer.split("\n")
                    buffer = lignes.pop()
                    for ligne in lignes:
                        trame = ligne.strip()
                        if essaye_GGA:
                            GGA.append(trame)
                            if len(GGA) == 3:
                                renvoi = ''.join(GGA)
                                return (f"Position et heure = {renvoi}")
                        if trame.startswith("$"):
                            if len(trame) == 1:
                                GGA.append(trame)
                                essaye_GGA = True
                        print(GGA)
            time.sleep(0.05)
    except Exception as e:
        return(f"Erreur : {e}")
    finally:
        if 'microbit' in locals():
            microbit.close()


def calcul_latitude(latitude, position):

    '''
        Permet de calculer la latitude selon la trame GLL et sa position
    '''

    degre = int(latitude[0]+latitude[1])
    minutes = float(latitude[2:])
    res = degre + minutes / 60
    if position == 'S' :
        return -res
    return res

def calcul_longitude(longitude, position):

    '''
        Permet de calculer la longitude selon la trame GLL et sa position
    '''

    print(longitude)
    degre = int(longitude[:3])
    minutes = float(longitude[3:])
    res = degre + minutes / 60
    if position == 'W' :
        return -res
    return res

def calcul_coords(trame):

    '''
        Permet de calculer la position de la carte microbit
    '''

    liste_trame = trame.split(',')
    liste_trame = ['Position et heure = $GNGGA', '084824.000', '5026.17797', 'N', '00249.33169', 'E', '1', '07', '2.3', '48.6', 'M', '44.6', 'M', '', '*75']
    latitude = liste_trame[2]
    pos_latitude = liste_trame[3]
    longitude = liste_trame[4]
    pos_longitude = liste_trame[5]
    return [calcul_latitude(latitude, pos_latitude), calcul_longitude(longitude, pos_longitude)]