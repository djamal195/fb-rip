#!/usr/bin/env python3
# acte_deces_auto.py – Version finale avec signature réelle
# Par DJAMAL19 x OTF – 2025

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# Chemin de ta signature (change si tu veux)
SIGNATURE_PATH = r"D:\Haxor\signatur.jpg"  # <-- TA SIGNATURE ICI

os.system("cls" if os.name == "nt" else "clear")
print("\nGÉNÉRATEUR D'ACTE DE DÉCÈS + SIGNATURE RÉELLE – 2025\n")

# === DEMANDE DES INFOS ===
nom_complet      = input("Nom complet du défunt            : ").strip().upper()
date_naiss       = input("Date de naissance (jj/mm/aaaa)   : ").strip()
lieu_naiss       = input("Lieu de naissance                : ").strip().title()
date_deces_input = input("Date de décès (jj/mm/aaaa) [Enter = aujourd'hui] : ").strip()
lieu_deces       = input("Lieu du décès (ville)            : ").strip().title()
age              = input("Âge au décès                     : ").strip()
profession       = input("Profession (retraité, étudiant...) : ").strip() or "sans profession"
pere             = input("Père (feu ...)                   : ").strip() or "feu XXX"
mere             = input("Mère (feu ...)                   : ").strip() or "feu YYY"
declarant        = input("Nom du déclarant                 : ").strip().title()
age_declarant    = input("Âge du déclarant                 : ").strip()
lien_declarant   = input("Lien avec le défunt (fils, etc.) : ").strip()

# Date de décès auto
if not date_deces_input:
    auj = datetime.now()
    mois_fr = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    date_deces_lettres = f"{auj.day} {mois_fr[auj.month-1]} {auj.year}"
else:
    j,m,a = map(int, date_deces_input.split("/"))
    mois_fr = ["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
    date_deces_lettres = f"{j} {mois_fr[m-1]} {a}"

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

# === CRÉATION IMAGE ===
largeur, hauteur = 1100, 700  # un peu plus haut pour la signature
img = Image.new("RGB", (largeur, hauteur), "white")
draw = ImageDraw.Draw(img)

# Police
try:
    font = ImageFont.truetype("times.ttf", 28)
    font_titre = ImageFont.truetype("times.ttf", 36)
except:
    try:
        font = ImageFont.truetype("arial.ttf", 28)
        font_titre = ImageFont.truetype("arial.ttf", 36)
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
        draw.text((marge, y), " ".join(ligne), fill="black", font=font,
                  stroke_width=1, stroke_fill=(100,100,100))
        y += 40
        ligne = [mot]
if ligne:
    draw.text((marge, y), " ".join(ligne), fill="black", font=font,
              stroke_width=1, stroke_fill=(100,100,100))
    y += 60

# Texte signature
draw.text((marge, y), "Pour extrait conforme,", fill="black", font=font)
draw.text((marge, y + 40), "L'Officier de l'État Civil", fill="black", font=font_titre)

# === COLLAGE DE LA VRAIE SIGNATURE ===
if os.path.exists(SIGNATURE_PATH):
    try:
        sign = Image.open(SIGNATURE_PATH).convert("RGBA")
        # Redimensionne proprement (max 300px de large, garde ratio)
        sign.thumbnail((300, 150), Image.Resampling.LANCZOS)
        
        # Position : bas à droite
        pos_x = largeur - sign.width - 100
        pos_y = y + 100
        
        img.paste(sign, (pos_x, pos_y), sign)  # le 4e paramètre = masque alpha
        print("Signature réelle collée avec succès !")
    except Exception as e:
        print(f"Erreur signature : {e}")
else:
    print("Signature non trouvée → trait classique")
    draw.line([(marge + 380, y + 110), (largeur - marge, y + 110)], fill="black", width=3)

# === SAUVEGARDE ===
nom_fichier = f"acte_deces_{nom_complet.replace(' ', '_')}_{int(datetime.now().timestamp())}.png"
img.save(nom_fichier)

print(f"\nACTE GÉNÉRÉ AVEC TA SIGNATURE RÉELLE !")
print(f"Fichier → {os.path.abspath(nom_fichier)}")
os.system(f'termux-clipboard-set "{os.path.abspath(nom_fichier)}" 2>/dev/null || clip < "{os.path.abspath(nom_fichier)}"')
print("Chemin copié dans le presse-papiers")
