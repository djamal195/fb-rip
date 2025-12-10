#!/usr/bin/env python3
import os
import sys
import urllib.parse
import time
from datetime import datetime

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_profile_id(url):
    # Extrait l'ID du profil Facebook (gère les liens username ou ID)
    if "facebook.com" not in url:
        return None
    if "profile.php?id=" in url:
        return url.split("profile.php?id=")[1].split("&")[0]
    parts = url.rstrip("/").split("/")
    for part in reversed(parts):
        if part and part.isdigit() and len(part) > 5:  # ID typique FB
            return part
    return None

clear()
print("""
╔══════════════════════════════════════════╗
║        RIP ACCOUNT FACEBBOK              ║
║               BY OTF                     ║
║              DJAMAL19                    ║
╚══════════════════════════════════════════╝
""")

lien = input("🔗 URL du profil Facebook à supprimer : ").strip()
if not lien.startswith("https://www.facebook.com/"):
    print("❌ Lien invalide ! Doit commencer par https://www.facebook.com/")
    sys.exit(1)

nom = input("👤 Nom complet de la personne décédée : ").strip()
date_deces = datetime.now().strftime("%Y-%m-%d")  # Date auto = aujourd'hui
print(f"📅 Date de décès (auto-remplie) : {date_deces}")

print("\n📸 Prépare une preuve : nécrologie, certificat de décès, carte commémorative")
print("   ou photo claire (scan/PDF/jpg) confirmant le décès")
piece = input("📂 Chemin complet du fichier (ex: /sdcard/Download/certificat.jpg) : ").strip()

if not os.path.exists(piece):
    print("❌ Fichier introuvable ! Vérifie le chemin et relance.")
    sys.exit(1)

email = input("📧 Ton e-mail pour les suivis Meta (réponse arrive là) : ").strip()

profile_id = get_profile_id(lien)
if not profile_id:
    print("❌ Impossible d'extraire l'ID du profil. Vérifie le lien (ex: facebook.com/username ou ?id=123).")
    sys.exit(1)

# Pas de pré-remplissage URL possible (formulaire derrière login), mais on prépare les infos
print(f"\n📝 Infos prêtes pour le formulaire :")
print(f"   - Profil ID : {profile_id}")
print(f"   - Nom : {nom}")
print(f"   - Date décès : {date_deces}")
print(f"   - Preuve : {piece}")
print(f"   - Email : {email}")

print("\n⚠️  IMPORTANT : Sois connecté à Facebook sur ton navigateur avant de continuer.")
print("   Si pas connecté, ça ouvrira la page login (5 sec max).")

print("\n⏳ Ouverture du formulaire dans 5 secondes...")
time.sleep(5)

# Ouvre le formulaire officiel
form_url = "https://www.facebook.com/help/contact/234739086860192"

if os.name == 'posix' and 'TERMUX_VERSION' in os.environ:
    os.system(f"termux-open-url \"{form_url}\"")
else:
    import webbrowser
    webbrowser.open(form_url)

print("""
✅ FORMULAIRE OUVERT !
   → Remplis manuellement : colle le nom, date ({date_deces}), ID profil ({profile_id})
   → Joins le fichier preuve ({piece})
   → Indique ton email ({email})
   → Clique "Envoyer"

Vérifie le compte en question ou ton email pour suivre la demande.
Meta traite en 24-72h → compte supprimé définitivement !

Bonne aide, tu sauves des vies numériques ❤️
""".format(date_deces=date_deces, profile_id=profile_id, piece=piece, email=email))
