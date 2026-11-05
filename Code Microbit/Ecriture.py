import Trame_NMEA.Capter_trame_once_GGA as ct
import folium
import subprocess
import json
import os

name = subprocess.run(["hostname"], stdout=subprocess.PIPE, text=True)
machine = name.stdout.strip().lower()
# f = open(f"/media/{machine}/MICROBIT/DETAILS.TXT")
# info = f.read().split('\n')
info = "99063602000528206efd7dc625f65b0a000000006e052820"
repertoire_script = os.path.dirname(os.path.abspath(__file__)) # Sert à trouver l'emplacement du code exécuté
chemin_json = os.path.join(repertoire_script, 'Trame_NMEA/ID.json')

localisation = ct.calcul_coords(ct.recup_position())
carte = folium.Map(location=[50.433333, 2.833333], zoom_start=15)

if localisation is None:
    folium.Marker([50.433333, 2.9], popup="GOOD").add_to(carte)
else:
    with open(chemin_json, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)
    folium.Marker([localisation[0],localisation[1]], popup=donnees[info[2][11:]]+2).add_to(carte)

html_content = carte._repr_html_()
refresh = '<meta http-equiv="refresh">'
full_html = refresh + html_content
with open("/var/www/html/index.html", "w", encoding="utf-8") as f:
    f.write(full_html)