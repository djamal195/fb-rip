#!/usr/bin/env python3
# acte.py - HACKER EDITION (LOCATION FIX)
# OTF x DJAMAL19

from PIL import Image, ImageDraw, ImageFont
import os
import sys
import time
import random
from datetime import datetime

# ==========================================
# CONFIG & STYLE
# ==========================================
R = "\033[91m" ; G = "\033[92m" ; Y = "\033[93m"
C = "\033[96m" ; W = "\033[97m" ; X = "\033[0m"

FONT_URL = "https://github.com/matomo-org/travis-scripts/raw/master/fonts/Arial.ttf"
FONT_NAME = "arial.ttf"
SIGNATURE_PATH = "signatur.jpg" 

def clear(): os.system("clear")

def banner():
    clear()
    print(f"""{G}
   ██████  ▄▄▄█████▓ █████▒
 ▒██    ▒  ▓  ██▒ ▓▒▓██   ▒ 
 ░ ▓██▄    ▒ ▓██░ ▒░▒████ ░ 
   ▒   ██▒ ░ ▓██▓ ░ ░▓█▒  ░ 
 ▒██████▒▒   ▒██▒ ░ ░▒█░    
 ▒ ▒▓▒ ▒ ░   ▒ ░░    ▒ ░    
 ░ ░▒  ░ ░     ░     ░      
 ░  ░  ░     ░       ░ 
      {R}╔════════════════════════════════════════╗
      ║   IDENTITY FORGERY • BLACK OPS TOOL    ║
      ║       OTF  x  DJAMAL19  x  HACK        ║
      ╚════════════════════════════════════════╝{X}
""")

def fake_loading(text):
    sys.stdout.write(f"\r  {C}[*] {text}...{X}")
    sys.stdout.flush()
    time.sleep(random.uniform(0.5, 1.5))
    print(f"\r  {G}[+] {text} [OK]{X}   ")

# ==========================================
# INITIALISATION
# ==========================================
banner()

if not os.path.exists(FONT_NAME):
    print(f"  {Y}[!] Downloading System Fonts...{X}")
    os.system(f"curl -L -s -o {FONT_NAME} {FONT_URL}")

if not os.path.exists("/sdcard"):
    print(f"  {R}[ERROR] STORAGE PERMISSION DENIED.{X}")
    print(f"  {W}Please run: termux-setup-storage{X}")
    sys.exit()

print(f"  {C}[SYSTEM] INITIALIZING FORGERY ENGINE...{X}\n")

# ==========================================
# INPUTS STYLE TERMINAL
# ==========================================
def ask(prompt):
    sys.stdout.write(f"  {G}root@otf:~/forge# {W}{prompt} : {C}")
    sys.stdout.flush()
    val = input().strip()
    print(f"{X}", end="")
    return val

full_name = ask("SUBJECT NAME").upper()
birth_date = ask("BIRTH DATE (DD/MM/YYYY)")
birth_place = ask("BIRTH PLACE").title()
death_date_input = ask("DEATH DATE (DD/MM/YYYY)")
death_place = ask("DEATH PLACE").title()
age = ask("SUBJECT AGE")
occupation = ask("OCCUPATION") or "none"
father = ask("FATHER NAME") or "late XXX"
mother = ask("MOTHER NAME") or "late YYY"
informant = ask("INFORMANT NAME").title()
informant_age = ask("INFORMANT AGE")
relation = ask("RELATIONSHIP")

# Logic Date
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
    except: death_date_letters = death_date_input

# Text Content
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

print(f"\n  {Y}[!] GENERATING DOCUMENT...{X}")

# ==========================================
# GENERATION
# ==========================================
width, height = 1100, 700
img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)

try:
    font_body = ImageFont.truetype(FONT_NAME, 28)
    font_title = ImageFont.truetype(FONT_NAME, 40)
except:
    font_body = ImageFont.load_default()
    font_title = font_body

fake_loading("Injecting Watermarks")
draw.text((width//2, 70), "DEATH CERTIFICATE EXTRACT", fill="black", font=font_title, anchor="mm")

margin = 80; max_width = width - (2 * margin); current_h = 160
words = text.split(); line = []

for word in words:
    test_line = ' '.join(line + [word])
    bbox = draw.textbbox((0, 0), test_line, font=font_body)
    if bbox[2] - bbox[0] <= max_width: line.append(word)
    else:
        draw.text((margin, current_h), ' '.join(line), font=font_body, fill="black")
        current_h += 45; line = [word]
if line: draw.text((margin, current_h), ' '.join(line), font=font_body, fill="black"); current_h += 80

fake_loading("Signing Document")
draw.text((margin, current_h), "For certified true copy,", fill="black", font=font_body)
draw.text((margin, current_h + 40), "The Civil Registrar", fill="black", font=ImageFont.truetype(FONT_NAME, 32))

if os.path.exists(SIGNATURE_PATH):
    try:
        sign = Image.open(SIGNATURE_PATH).convert("RGBA")
        sign.thumbnail((300, 150), Image.Resampling.LANCZOS)
        mask = sign.split()[-1] if 'A' in sign.mode else None
        img.paste(sign, (width - sign.width - 100, current_h + 60), mask)
    except: pass
else:
    draw.line([(width - 400, current_h + 150), (width - 100, current_h + 150)], fill="black", width=3)

# Save
clean_name = full_name.replace(' ', '_')
filename = f"Death_Certificate_{clean_name}_{int(datetime.now().timestamp())}.png"
save_path = f"/sdcard/{filename}"

fake_loading("Finalizing Export")
try:
    img.save(save_path)
    os.system(f'termux-clipboard-set "{save_path}"')
    
    # --- AFFICHAGE CLAIR DU CHEMIN ---
    print(f"""
  {G}╔═══════════════════════════════════════════════════╗
  ║      ✔ DOCUMENT FORGED SUCCESSFULLY               ║
  ║                                                   ║
  ║  📂 FILE SAVED AT :                               ║
  ║  {Y}{save_path}{G}
  ║                                                   ║
  ║  📋 PATH COPIED TO CLIPBOARD                      ║
  ╚═══════════════════════════════════════════════════╝{X}
    """)

except Exception as e:
    print(f"\n  {R}[ERROR] COULD NOT SAVE TO SDCARD: {e}{X}")
