#!/usr/bin/env python3
# acte_deces_auto.py
# Générateur d'acte de décès français hyper réaliste – 2025
# Par DJAMAL19 x OTF

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# Couleurs et style
os.system("clear")
print("\nGÉNÉRATEUR D'ACTE DE DÉCÈS FRANÇAIS – ULTRA RÉALISTE\n")

# === DEMANDE DES INFOS ===
nom_complet      = input("Nom complet du défunt            : ").strip().upper()
date_naiss       = input("Date de naissance (jj/mm/aaaa)   : ").strip()
lieu_naiss       = input("Lieu de naissance                : ").strip().title()
date_deces_input = input("Date de décès (jj/mm/aaaa) [aujourd'hui si vide] : ").strip()
lieu_deces       = input("Lieu du décès (ville)            : ").strip().title()
age              = input("Âge au décès (ex: 67)            : ").strip()
profession       = input("Profession (ex: retraité, étudiant...) : ").strip() or "sans profession"
pere             = input("Nom du père (feu ...)            : ").strip() or "feu XXX"
mere             = input("Nom de la mère (feu ...)         : ").strip() or "feu YYY"
declarant        = input("Nom du déclarant (fils, frère...) : ").strip().title()
age_declarant    = input("Âge du déclarant                 : ").strip()
lien_declarant   = input("Lien avec le défunt (fils, fille, conjoint...) : ").strip()

# Date de décès = aujourd'hui si vide
if not date_deces_input:
    auj = datetime.now()
    jour_deces = auj.day
    mois_deces = ["janvier","février","mars","avril","mai","juin",
                  "juillet","août","septembre","octobre","novembre","décembre"][auj.month-1]
    annee_deces = auj.year
    date_deces_lettres = f"{jour_deces} {mois_deces} {annee_deces}"
else:
    j,m,a = map(int, date_deces_input.split("/"))
    mois_fr = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    date_deces_lettres = f"{j} {mois_fr[m-1]} {a}"

# === TEXTE FINAL ===
texte = (
    f"----Le {date_deces_lettres}, à dix heures trente minutes, est décédé "
    f"au domicile sis à {lieu_deces} : {nom_complet}, "
    f"sexe masculin, âgé de {age} ans, {profession}, né le {date_naiss} à {lieu_naiss}, "
    f"domicilié de son vivant à {lieu_deces}, "
    f"fils de {pere} et de {mere}. "
    f"Dressé par nous, Officier de l'État Civil, sur la déclaration de {declarant}, "
    f"{age_declarant} ans, {lien_declarant} du défunt, qui, lecture faite et invité à lire l'acte, "
    f"a signé avec nous."
)

# === GÉNÉRATION IMAGE ===
largeur, hauteur = 1100, 600
img = Image.new("RGB", (largeur, hauteur), "white")
draw = ImageDraw.Draw(img)

# Police réaliste
try:
    font = ImageFont.truetype("times.ttf", 28)
    font_titre = ImageFont.truetype("times.ttf", 34)
except:
    try:
        font = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 28)
        font_titre = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 34)
    except:
        font = ImageFont.load_default()
        font_titre = font

# Titre
draw.text((largeur//2, 60), "EXTRAIT D'ACTE DE DÉCÈS", fill="black", font=font_titre, anchor="mm")

# Corps du texte justifié
marge = 80
largeur_utile = largeur - 2*marge
y = 140
mots = texte.split()
ligne = []
for mot in mots:
    test = " ".join(ligne + [mot])
    if draw.textbbox((0,0), test, font=font)[2] <= largeur_utile:
        ligne.append(mot)
    else:
        phrase = " ".join(ligne)
        draw.text((marge, y), phrase, fill="black", font=font,
                  stroke_width=1, stroke_fill=(100,100,100))
        y += 40
        ligne = [mot]
if ligne:
    phrase = " ".join(ligne)
    draw.text((marge, y), phrase, fill="black", font=font,
              stroke_width=1, stroke_fill=(100,100,100))
    y += 40

# Signature + trait
draw.text((marge, y + 30), "Pour extrait conforme,", fill="black", font=font)
draw.text((marge, y + 70), "L'Officier de l'État Civil", fill="black", font=font_titre)
draw.line((marge + 380, y + 90), (largeur - marge, y + 90), fill="black", width=3)

# Sauvegarde dans Téléchargements
chements
chemin = f"/sdcard/Download/acte_deces_{nom_complet.replace(' ', '_')}_{int(datetime.now().timestamp())}.png"
img.save(chemin)

print(f"\nActe généré avec succès !")
print(f"Fichier : {chemin}")
print(f"Tu peux l'utiliser directement dans le formulaire Meta")
os.system(f'termux-clipboard-set "{chemin}" 2>/dev/null || true')
print("Chemin copié dans le presse-papiers")
