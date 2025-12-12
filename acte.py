#!/usr/bin/env python3
# death_certificate_english.py
# English Death Certificate Generator + Real Signature
# Sauvegarde directe sur /sdcard/ pour que Firefox puisse le lire

from PIL import Image, ImageDraw, ImageFont
import os
import sys
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================
# Ta signature doit aussi être accessible. 
# Mets-la dans le même dossier que le script ou sur sdcard.
SIGNATURE_PATH = "signatur.jpg" 

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
print("\nENGLISH DEATH CERTIFICATE GENERATOR – SDCARD EDITION\n")

# Vérification accès stockage
if not os.path.exists("/sdcard"):
    print("❌ ERREUR : Accès au stockage refusé.")
    print("Tapez 'termux-setup-storage' dans Termux puis relancez.")
    sys.exit()

# === INPUT (English) ===
full_name       = input("Full name of deceased             : ").strip().upper()
birth_date       = input("Date of birth (dd/mm/yyyy)       : ").strip()
birth_place      = input("Place of birth                   : ").strip().title()
death_date_input = input("Date of death (dd/mm/yyyy) [today if empty] : ").strip()
death_place      = input("Place of death (city)            : ").strip().title()
age              = input("Age at death                     : ").strip()
occupation       = input("Occupation (retired, student...) : ").strip() or "none"
father           = input("Father's name (late ...)         : ").strip() or "late XXX"
mother           = input("Mother's name (late ...)         : ").strip() or "late YYY"
informant        = input("Name of informant                : ").strip().title()
informant_age    = input("Informant's age                  : ").strip()
relation         = input("Relationship to deceased         : ").strip()

# Auto today if empty
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
        death_date_letters = death_date_input # Fallback si format bizarre

# === ENGLISH TEXT ===
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

# === CREATE IMAGE ===
width, height = 1100, 700
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

# Font loading logic
try:
    # On essaie de charger une font système standard
    font = ImageFont.truetype("/system/fonts/Roboto-Regular.ttf", 28)
    font_title = ImageFont.truetype("/system/fonts/Roboto-Bold.ttf", 38)
except:
    try:
        font = ImageFont.truetype("arial.ttf", 28)
        font_title = ImageFont.truetype("arial.ttf", 38)
    except:
        font = ImageFont.load_default()
        font_title = font

# Title
draw.text((width//2, 60), "DEATH CERTIFICATE EXTRACT", fill="black", font=font_title, anchor="mm")

# Justified body text logic
margin = 80
max_width = width - 2*margin
y = 150
words = text.split()
line = []
for word in words:
    test = " ".join(line + [word])
    bbox = draw.textbbox((0,0), test, font=font)
    if bbox[2] <= max_width:
        line.append(word)
    else:
        draw.text((margin, y), " ".join(line), fill="black", font=font)
        y += 42
        line = [word]
if line:
    draw.text((margin, y), " ".join(line), fill="black", font=font)
    y += 70

# Signature text
draw.text((margin, y), "For certified true copy,", fill="black", font=font)
draw.text((margin, y + 45), "The Civil Registrar", fill="black", font=font_title)

# === PASTE SIGNATURE ===
if os.path.exists(SIGNATURE_PATH):
    try:
        sign = Image.open(SIGNATURE_PATH).convert("RGBA")
        sign.thumbnail((320, 160)) # Thumbnail est mieux que resize pour garder ratio
        
        # On crée un masque pour la transparence si c'est un jpg
        mask = sign.split()[-1] if 'A' in sign.mode else None
        
        img.paste(sign, (width - sign.width - 100, y + 100), mask)
        print("Signature ajoutée.")
    except Exception as e:
        print(f"Erreur signature: {e}")
else:
    print("Signature introuvable (pas grave).")
    draw.line([(margin + 400, y + 120), (width - margin, y + 120)], fill="black", width=3)

# === SAVE TO SDCARD (SOLUTION) ===
# Nom du fichier
clean_name = full_name.replace(' ', '_')
timestamp = int(datetime.now().timestamp())
filename = f"Death_Certificate_{clean_name}_{timestamp}.png"

# Chemin vers la SDCARD (Accessible par Firefox)
save_path = f"/sdcard/{filename}"

try:
    img.save(save_path)
    print(f"\n✅ SUCCÈS : CERTIFICAT GÉNÉRÉ !")
    print(f"📂 EMPLACEMENT : {save_path}")
    print(f"👉 Copie ce chemin pour le script FB : {save_path}")
    
    # Copier dans le presse-papier Termux automatiquement
    os.system(f'termux-clipboard-set "{save_path}"')
    print("(Chemin copié dans le presse-papier !)")
    
except Exception as e:
    print(f"\n❌ ERREUR SAUVEGARDE SDCARD : {e}")
    print("Essaie de lancer 'termux-setup-storage' et réessaie.")
    # Fallback local
    img.save(filename)
    print(f"Sauvegardé localement à la place : {os.path.abspath(filename)}")
