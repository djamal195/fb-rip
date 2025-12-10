#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime

# CORRECTION ICI : on importe PIL, pas datetime !
from PIL import Image, ImageDraw, ImageFont

# Dossier de sortie visible sur Android
OUTPUT_DIR = "/sdcard/Download"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = f"{OUTPUT_DIR}/acte_deces_{int(time.time())}.png"

def generer_acte(nom, date_naiss, ville_naiss, ville_deces, email, profil_url):
    aujourd_hui = datetime.now()
    mois_fr = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    jour = aujourd_hui.day
    mois = mois_fr[aujourd_hui.month - 1]
    annee = aujourd_hui.year

    # Calcul âge approximatif
    try:
        jour_n, mois_n, annee_n = map(int, date_naiss.split("/"))
        age = aujourd_hui.year - annee_n - ((aujourd_hui.month, aujourd_hui.day) < (mois_n, jour_n))
    except:
        age = 45  # valeur par défaut si erreur

    texte = (
        f"----Le {jour} {mois} {annee}, à dix heures trente minutes, est décédé "
        f"au domicile sis à {ville_deces} : {nom.upper()}, né(e) le {date_naiss} "
        f"à {ville_naiss}, âgé(e) de {age} ans, célibataire/divorcé(e), sans profession connue. "
        f"Fils/Fille de feu(e) XXX et de feu(e) YYY. Dressé par nous Officier d'État Civil "
        f"sur déclaration de la famille, lecture faite, les parties ont signé avec nous."
    )

    # Création image
    img = Image.new('RGB', (1000, 460), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Police
    try:
        font = ImageFont.truetype("times.ttf", 28)
    except:
        try:
            font = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 28)
        except:
            font = ImageFont.load_default()

    # Découpage en lignes justifiées
    mots = texte.split()
    lignes = []
    ligne = []
    for mot in mots:
        test = " ".join(ligne + [mot])
        if draw.text((0,0), test, font=font)  # dummy pour calcul
        if draw.textbbox((0,0), test, font=font)[2] < 920:
            ligne.append(mot)
        else:
            lignes.append(" ".join(ligne))
            ligne = [mot]
    if ligne:
        lignes.append(" ".join(ligne))

    y = 60
    for ligne in lignes:
        draw.text((40, y), ligne, fill=(0,0,0), font=font, stroke_width=1, stroke_fill=(100,100,100))
        y += 40

    # Trait final
    draw.line([(40, y-10), (960, y-10)], fill=(0,0,0), width=2)

    img.save(OUTPUT_PATH)
    print(f"Acte généré → {OUTPUT_PATH}")
    return OUTPUT_PATH

# ========================= MAIN =========================
os.system("clear")
print("SUPPRESSION COMPTE FACEBOOK - ACTE DE DÉCÈS AUTO")
print("═" * 50)

nom = input("Nom complet de la personne : ")
date_naiss = input("Date naissance (jj/mm/aaaa) : ")
ville_naiss = input("Ville de naissance : ")
ville_deces = input("Ville actuelle/décès : ")
email = input("Ton email pour Meta : ")
profil = input("Lien du profil Facebook : ")

print("\nGénération de l'acte de décès...")
generer_acte(nom, date_naiss, ville_naiss, ville_deces, email, profil)

print("\nOuverture du formulaire Meta...")
time.sleep(4)

url = "https://www.facebook.com/help/contact/234739086860192"
if 'TERMUX_VERSION' in os.environ:
    os.system(f"termux-open-url '{url}'")
else:
    import webbrowser
    webbrowser.open(url)

print(f"""
TERMINÉ !
→ Acte sauvegardé dans Téléchargements
→ Formulaire ouvert
→ Remplis :
   • Nom : {nom}
   • Date décès : aujourd'hui
   • Email : {email}
   • Joindre l'image générée
→ Envoi = compte supprimé en 24-72h

Partage ce script, plus personne ne t'embêtera jamais
""")
