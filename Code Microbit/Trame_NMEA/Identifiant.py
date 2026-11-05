import subprocess
import json
import os

name = subprocess.run(["hostname"], stdout=subprocess.PIPE, text=True)
machine = name.stdout.strip().lower()

f = open(f"/media/{machine}/MICROBIT/DETAILS.TXT")
info = f.read().split('\n')
#print(info[2][11:])

repertoire_script = os.path.dirname(os.path.abspath(__file__)) # Sert à trouver l'emplacement du code exécuté
chemin_json = os.path.join(repertoire_script, 'ID.json')

with open(chemin_json, 'r', encoding='utf-8') as fichier:
    donnees = json.load(fichier)

print(donnees["99063602000528206efd7dc625f65b0a000000006e052820"])