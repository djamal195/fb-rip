from PIL import Image, ImageDraw, ImageFont

# --- 1. LE TEXTE (Français - Acte de Décès) ---
# Format standard administratif : Date -> Lieu -> Identité -> Parents -> Déclarant
texte_complet = (
    "----Le dix décembre deux mille vingt-cinq, à dix heures trente minutes, est décédé "
    "au domicile familial sis à Mahabibo Mahajanga : RAKOTOMALALA Jean Baptiste, "
    "sexe masculin, âgé de soixante-sept ans, retraité, né le dix juin mil neuf cent "
    "cinquante-huit à Antananarivo, domicilié de son vivant à Mahabibo Mahajanga, "
    "fils de feu RAKOTO Jean et de RASOA Suzanne. Dressé par nous, Officier de "
    "l'État Civil, sur la déclaration de RAKOTOMALALA Eric, quarante ans, fils du "
    "défunt, domicilié à Tsararano Ambony, qui, lecture faite et invité à lire l'acte, "
    "a signé avec nous ."
)

# --- 2. DIMENSIONS ET STYLE ---
largeur_img = 1000
hauteur_img = 380

marge_gauche = 25
marge_droite = 25
marge_haut = 40

largeur_utile = largeur_img - marge_gauche - marge_droite

background_color = (255, 255, 255) # Fond blanc
text_color = (10, 10, 10) # Noir presque pur

# --- REGLAGE DU SEMI-GRAS ---
# Contour GRIS pour un effet "encre" réaliste (pas trop gras, pas trop fin)
stroke_color = (150, 150, 150) 

font_size = 24 
interligne = 13

# --- 3. FONCTIONS TECHNIQUES ---
def get_width(text, font, draw_dummy):
    bbox = draw_dummy.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

def decouper_lignes(text, font, draw_dummy, max_width):
    mots = text.split(' ')
    lignes = []
    ligne_actuelle = []
    largeur_actuelle = 0
    espace_width = get_width(" ", font, draw_dummy)

    for mot in mots:
        mot_width = get_width(mot, font, draw_dummy)
        
        # On garde +2 car on a un stroke_width=1
        mot_width_reel = mot_width + 2 
        
        if largeur_actuelle + mot_width_reel + (espace_width if ligne_actuelle else 0) <= max_width:
            ligne_actuelle.append(mot)
            largeur_actuelle += mot_width_reel + (espace_width if ligne_actuelle else 0)
        else:
            lignes.append(ligne_actuelle)
            ligne_actuelle = [mot]
            largeur_actuelle = mot_width_reel
    
    if ligne_actuelle:
        lignes.append(ligne_actuelle)
    return lignes

# --- 4. CHARGEMENT POLICE (TIMES NEW ROMAN) ---
dummy_img = Image.new('RGB', (1, 1))
dummy_draw = ImageDraw.Draw(dummy_img)

try:
    # Police type administration standard
    font = ImageFont.truetype("times.ttf", font_size)
except IOError:
    font = ImageFont.truetype("arial.ttf", font_size)
    print("Times New Roman non trouvée. Utilisation de Arial.")

lignes = decouper_lignes(texte_complet, font, dummy_draw, largeur_utile)
print(f"Lignes générées : {len(lignes)}")

# --- 5. DESSIN DE L'IMAGE ---
image = Image.new('RGB', (largeur_img, hauteur_img), background_color)
draw = ImageDraw.Draw(image)

cursor_y = marge_haut

for i, ligne_mots in enumerate(lignes):
    is_last_line = (i == len(lignes) - 1)
    
    if is_last_line:
        # Dernière ligne (Alignement gauche + Trait)
        phrase = " ".join(ligne_mots)
        
        # Semi-gras (stroke_width=1 + couleur grise)
        draw.text((marge_gauche, cursor_y), phrase, fill=text_color, font=font, stroke_width=1, stroke_fill=stroke_color)
        
        # Le trait _________
        w_texte = get_width(phrase, font, dummy_draw)
        x_debut_trait = marge_gauche + w_texte + 8
        x_fin_trait = largeur_img - marge_droite
        y_trait = cursor_y + (font_size * 0.8)
        
        draw.line([(x_debut_trait, y_trait), (x_fin_trait, y_trait)], fill=text_color, width=2)
        
    else:
        # Lignes Justifiées
        total_width_mots = sum([get_width(mot, font, dummy_draw) for mot in ligne_mots])
        espace_vide_total = largeur_utile - total_width_mots
        nb_espaces = len(ligne_mots) - 1
        
        if nb_espaces > 0:
            largeur_espace = espace_vide_total / nb_espaces
            cursor_x = marge_gauche
            for mot in ligne_mots:
                draw.text((cursor_x, cursor_y), mot, fill=text_color, font=font, stroke_width=1, stroke_fill=stroke_color)
                cursor_x += get_width(mot, font, dummy_draw) + largeur_espace
        else:
            # Cas un seul mot
            draw.text((marge_gauche, cursor_y), ligne_mots[0], fill=text_color, font=font, stroke_width=1, stroke_fill=stroke_color)

    cursor_y += font_size + interligne

# Sauvegarde
image.save("acte_deces_francais.png")
print("Image générée : acte_deces_francais.png")
