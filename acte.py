#!/usr/bin/env python3
# death_certificate_english.py
# English Death Certificate Generator + Real Signature – 2025
# DJAMAL19 x OTF

from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

# YOUR REAL SIGNATURE (change only if you move the file)
SIGNATURE_PATH = r"signatur.jpg"

os.system("cls" if os.name == "nt" else "clear")
print("\nENGLISH DEATH CERTIFICATE GENERATOR – ULTRA REALISTIC\n")

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
    d, m, y = map(int, death_date_input.split("/"))
    month_en = ["January","February","March","April","May","June","July",
                "August","September","October","November","December"]
    death_date_letters = f"{d} {month_en[m-1]} {y}"

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

# Font
try:
    font = ImageFont.truetype("times.ttf", 28)
    font_title = ImageFont.truetype("times.ttf", 38)
except:
    try:
        font = ImageFont.truetype("arial.ttf", 28)
        font_title = ImageFont.truetype("arial.ttf", 38)
    except:
        font = ImageFont.load_default()
        font_title = font

# Title
draw.text((width//2, 60), "DEATH CERTIFICATE EXTRACT", fill="black", font=font_title, anchor="mm")

# Justified body text
margin = 80
max_width = width - 2*margin
y = 150
words = text.split()
line = []
for word in words:
    test = " ".join(line + [word])
    if draw.textbbox((0,0), test, font=font)[2] <= max_width:
        line.append(word)
    else:
        draw.text((margin, y), " ".join(line), fill="black", font=font,
                  stroke_width=1, stroke_fill=(110,110,110))
        y += 42
        line = [word]
if line:
    draw.text((margin, y), " ".join(line), fill="black", font=font,
              stroke_width=1, stroke_fill=(110,110,110))
    y += 70

# Signature text
draw.text((margin, y), "For certified true copy,", fill="black", font=font)
draw.text((margin, y + 45), "The Civil Registrar", fill="black", font=font_title)

# === PASTE YOUR REAL HANDWRITTEN SIGNATURE ===
if os.path.exists(SIGNATURE_PATH):
    try:
        sign = Image.open(SIGNATURE_PATH).convert("RGBA")
        sign.thumbnail((320, 160), Image.Resampling.LANCZOS)
        img.paste(sign, (width - sign.width - 100, y + 100), sign)
        print("Real signature successfully added!")
    except Exception as e:
        print(f"Signature error: {e}")
else:
    print("Signature file not found → drawing line")
    draw.line([(margin + 400, y + 120), (width - margin, y + 120)], fill="black", width=3)

# === SAVE ===
filename = f"Death_Certificate_{full_name.replace(' ', '_')}_{int(datetime.now().timestamp())}.png"
img.save(filename)

print(f"\nDEATH CERTIFICATE GENERATED (ENGLISH)")
print(f"File → {os.path.abspath(filename)}")
os.system(f'termux-clipboard-set "{os.path.abspath(filename)}" 2>/dev/null || clip < "{os.path.abspath(filename)}"')
print("Path copied to clipboard – ready for Facebook form")
