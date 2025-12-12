#!/usr/bin/env python3
# death_certificate_hd.py
# Générateur HD pour Termux (Télécharge la police automatiquement)

from PIL import Image, ImageDraw, ImageFont
import os
import sys
import time
from datetime import datetime

# ==========================================
# 1. TÉLÉCHARGEMENT AUTOMATIQUE DE LA POLICE
# ==========================================
# On a besoin d'une vraie police (.ttf) pour que ce soit beau.
# Si elle n'est pas là, on la télécharge depuis internet.

FONT_URL = "https://github.com/matomo-org/travis-scripts/raw/master/fonts/Arial.ttf"
FONT_NAME = "arial.ttf"

if not os.path.exists(FONT_NAME):
    print("⚠️ Police manquante. Téléchargement de Arial.ttf...")
    os.system(f"curl -L -o {FONT_NAME} {FONT_URL}")
    print("✅ Police installée !")

# ==========================================
# CONFIGURATION
# ==========================================
SIGNATURE_PATH = "signatur.jpg" 

def clear():
    os.system("clear")

clear()
print("\nENGLISH DEATH CERTIFICATE GENERATOR – HD TERMUX EDITION\n")

if not os.path.exists("/sdcard"):
    print("❌ ERREUR : Tapez 'termux-setup-storage' et réessayez.")
    sys.exit()

# === INPUT ===
full_name       = input("Full name of deceased             : ").strip().upper()
birth_date       = input("Date of birth (dd/mm/yyyy)       : ").strip()
birth_place      = input("Place of birth                   : ").strip().title()
death_date_input = input("Date of death (dd/mm/yyyy)       : ").strip()
death_place      = input("Place of death (city)            : ").strip().title()
age              = input("Age at death                     : ").strip()
occupation       = input("Occupation                       : ").strip() or "none"
father           = input("Father's name                    : ").strip() or "late XXX"
mother           = input("Mother's name                    : ").strip() or "late YYY"
informant        = input("Name of informant                : ").strip().title()
informant_age    = input("Informant's age                  : ").strip()
relation         = input("Relationship                     : ").strip()

# Date auto formatting
if not death_date_input:
    today = datetime.now()
    month_en = ["January","February","March","April","May","June","July",
                "August","September","October","November","December"]
    death_date_letters = f"{today.day} {month_en[today.month-1]} {today.year}"
else:
    try:
        d, m, y = map(int, death_date_input.split("/"))
        month_en = ["January","February","March","April","May","June","July",
                    "August","September","October","November","December"]
        death_date_letters = f"{d} {month_en[m-1]} {y}"
    except:
        death_date_letters = death_date_input

# === TEXTE ===
text = (
    f"On this {death_date_letters}, at 10:30 a.m., died at his/her residence "
    f"located in {death_place}: {full_name}, "
    f"male, aged {age} years, {occupation}, born on {birth_date} in {birth_place}, "
    f"resident of {death_place}, "
    f"son of {father} and {mother}. "
    f"Drawn up by us, Civil Registrar, upon the declaration of {informant}, "
    f"aged {informant_age}, {relation} of the deceased, who having heard the act read, "
    f"signed it with us."
)

# === CRÉATION IMAGE HD ===
# On garde les dimensions mais on charge la vraie police
width, height = 1100, 700
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Chargement de la police Arial téléchargée
try:
    font_body = ImageFont.truetype(FONT_NAME, 28)  # Taille 28 pour le texte
    font_title = ImageFont.truetype(FONT_NAME, 40) # Taille 40 pour le titre
except Exception as e:
    print(f"❌ Erreur police : {e}")
    print("Utilisation police par défaut (Moche)")
    font_body = ImageFont.load_default()
    font_title = font_body

# Titre centré
draw.text((width//2, 70), "DEATH CERTIFICATE EXTRACT", fill="black", font=font_title, anchor="mm")

# --- ALGORITHME DE RETOUR À LA LIGNE (WORD WRAP) ---
# C'est ce qui empêche le texte de dépasser sur les côtés
margin = 80
max_width = width - (2 * margin)
current_h = 160
words = text.split()
line = []

for word in words:
    # On teste la largeur de la ligne avec le nouveau mot
    test_line = ' '.join(line + [word])
    bbox = draw.textbbox((0, 0), test_line, font=font_body)
    w_line = bbox[2] - bbox[0]
    
    if w_line <= max_width:
        line.append(word)
    else:
        # On dessine la ligne et on passe à la suivante
        draw.text((margin, current_h), ' '.join(line), font=font_body, fill="black")
        current_h += 45 # Espace entre les lignes
        line = [word]

# Dessiner la dernière ligne
if line:
    draw.text((margin, current_h), ' '.join(line), font=font_body, fill="black")
    current_h += 80 # Marge après le texte

# Signature Text
draw.text((margin, current_h), "For certified true copy,", fill="black", font=font_body)
draw.text((margin, current_h + 40), "The Civil Registrar", fill="black", font=ImageFont.truetype(FONT_NAME, 32))

# === SIGNATURE IMAGE ===
if os.path.exists(SIGNATURE_PATH):
    try:
        sign = Image.open(SIGNATURE_PATH).convert("RGBA")
        # On redimensionne proprement
        sign.thumbnail((300, 150), Image.Resampling.LANCZOS)
        
        # Gestion transparence
        mask = sign.split()[-1] if 'A' in sign.mode else None
        
        # Position signature (En bas à droite)
        img.paste(sign, (width - sign.width - 100, current_h + 60), mask)
        print("Signature insérée.")
    except:
        pass
else:
    # Ligne simple si pas d'image
    draw.line([(width - 400, current_h + 150), (width - 100, current_h + 150)], fill="black", width=3)

# === SAUVEGARDE ===
clean_name = full_name.replace(' ', '_')
filename = f"Death_Certificate_{clean_name}_{int(datetime.now().timestamp())}.png"
save_path = f"/sdcard/{filename}"

img.save(save_path)

print(f"\n✅ IMAGE HD GÉNÉRÉE !")
print(f"📂 {save_path}")

# Copie auto dans le presse-papier
os.system(f'termux-clipboard-set "{save_path}"')
