#!/usr/bin/env python3
import os
import sys
from datetime import Image, ImageDraw, ImageFont
from datetime import datetime
import time

# Chemin de sortie accessible sur Android
OUTPUT_DIR = "/sdcard/Download"
OUTPUT_PATH = f"{OUTPUT_DIR}/acte_deces_{int(time.time())}.png"

def generer_acte_deces(nom_complet, date_naissance, ville_naissance, ville_deces, age=None):
    # Date du jour en toutes lettres
    mois = ["janvier","février","mars","avril","mai","juin",
            "juillet","août","septembre","octobre","novembre","décembre"]
    aujourd_hui = datetime.now()
    jour = aujourd_hui.day
    mois_str = mois[aujourd_hui.month - 1]
    annee = aujourd_hui.year

    # Calcul âge si pas donné
    if not age:
        naissance = datetime.strptime(date_naissance, "%d/%m/%Y")
        age = aujourd_hui.year - naissance.year - ((aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day))

    texte = (
        f"----Le {jour} {mois_str} {annee}, à dix heures trente minutes, est décédé "
        f"au domicile familial sis à {ville_deces} : {nom_complet.upper()}, "
        f"sexe masculin, âgé de {age} ans, retraité, né le {date_naissance} à {ville_naissance}, "
        f"domicilié de son vivant à {ville_deces}, fils de feu RAKOTO Jean et de RASOA Suzanne. "
        f"Dressé par nous, Officier de l'État Civil, sur la déclaration de RAKOTOMALALA Eric, "
        f"quarante ans, fils du défunt, qui, lecture faite et invité à lire l'acte, a signé avec nous."
    )

    # === Génération image (même code que toi, optimisé) ===
    largeur_img, hauteur_img = 1000, 420
    marge_gauche, marge_haut = 30, 50
    largeur_utile = largeur_img - 60

    image = Image.new('RGB', (largeur_img, hauteur_img), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("times.ttf", 26)
    except:
        try:
            font = ImageFont.truetype("/system/fonts/DroidSans.ttf", 26)
        except:
            font = ImageFont.load_default()

    # Découpage justifié
    mots = texte.split()
    lignes = []
    ligne = []
    for mot in mots:
        test = " ".join(ligne + [mot])
        if draw.textbbox((0,0), test, font=font)[2] <= largeur_utile:
            ligne.append(mot)
        else:
            lignes.append(" ".join(ligne))
            ligne = [mot]
    if ligne:
        lignes.append(" ".join(ligne))
    lignes.append("")

    y = marge_haut
    for i, ligne in enumerate(lignes):
        if i == len(lignes) - 2:  # Avant-dernière ligne → signature
            draw.text((marge_gauche, y), ligne, fill=(0,0,0), font=font, stroke_width=1, stroke_fill=(100,100,100))
            # Trait signature
            w = draw.textbbox((marge_gauche, y), ligne, font=font)[2]
            draw.line([(marge_gauche + w + 10, y + 20), (largeur_img - 50, y + 20)], fill=(0,0,0), width=2)
        else:
            draw.text((marge_gauche, y), ligne, fill=(0,0,0), font=font, stroke_width=1, stroke_fill=(120,120,120))
        y += 38

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    image.save(OUTPUT_PATH)
    print(f"Acte de décès généré → {OUTPUT_PATH}")
    return OUTPUT_PATH

# =============================================
# =================== MAIN ====================
# =============================================
os.system('clear')
print("SUPPRESSION COMPTE FB - MÉTHODE ACTE DE DÉCÈS (Ultra efficace)")

print("\nRemplis les infos de la personne (même approximatives)")
nom = input("Nom complet : ").strip()
date_naiss = input("Date de naissance (jj/mm/aaaa) : ").strip()
ville_naiss = input("Ville de naissance : ").strip()
ville_deces = input("Ville actuelle / décès (ex: Mahajanga) : ").strip()
email = input("Ton e-mail pour la réponse Meta : ").strip()
profil = input("Lien du profil Facebook à supprimer : ").strip()

print("\nGénération de l'acte de décès en cours...")
chemin_image = generer_acte_deces(nom, date_naiss, ville_naiss, ville_deces)

print("\nOuverture du formulaire officiel Meta dans 5 secondes...")
print("Connecte-toi à Facebook avant si besoin !")
time.sleep(5)

# Ouvre le formulaire officiel
form_url = "https://www.facebook.com/help/contact/234739086860192"
if 'TERMUX_VERSION' in os.environ:
    os.system(f"termux-open-url '{form_url}'")
else:
    import webbrowser
    webbrowser.open(form_url)

print(f"""
FINI !
→ Formulaire ouvert
→ Acte de décès généré ici : {chemin_image}
→ Ouvre l'image depuis tes Téléchargements
→ Remplis le formulaire :
   • Nom : {nom}
   • Date décès : aujourd'hui
   • Email : {email}
   • Joindre l'image générée
   • Envoyer

Compte supprimé en 24–72h max.

Tu peux partager ce script, plus personne ne t'embêtera jamais
""")
