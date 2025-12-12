#!/usr/bin/env python3
import os
import sys
import getpass
import time
import random
import string
from datetime import datetime

# Importations Selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# 1. HACKER STYLE CONFIG
# ==========================================
R = "\033[91m" ; G = "\033[92m" ; Y = "\033[93m"
C = "\033[96m" ; W = "\033[97m" ; X = "\033[0m"

def clear(): os.system('clear')

def banner():
    clear()
    print(f"""{G}
   ▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄   ██▓    
   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓██▒    
   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒██░    
   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒██░    
     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░██████▒
     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░ ▒░▓  ░
       ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░ ▒  ░
     ░        ░░   ░   ░   ▒   ░          ░ ░   
              ░            ░  ░░ ░          ░  ░
                              ░                 
      {R}╔═══════════════════════════════════════════╗
      ║    TERMUX EDITION • CLUMSY HUMAN V2       ║
      ║         DEV BY: {Y}OTF x DJAMAL19{R}            ║
      ╚═══════════════════════════════════════════╝{X}
""")

def loading(percent, status=""):
    bar_len = 20
    filled_len = int(round(bar_len * percent / 100))
    bar = f"{G}█{X}" * filled_len + f"{C}░{X}" * (bar_len - filled_len)
    sys.stdout.write(f'\r  {C}[{bar}{C}] {G}{percent}%{X} :: {status}\033[K')
    sys.stdout.flush()

# ==========================================
# 🔥 IA DE FRAPPE "CLUMSY" (Anti-Checkpoint)
# ==========================================
def type_clumsy(element, text):
    """
    Simule un humain fatigué qui fait des fautes et s'arrête pour réfléchir.
    """
    # Pause de réflexion avant de commencer à taper
    time.sleep(random.uniform(1.0, 3.0))
    
    chars = string.ascii_lowercase + string.digits
    
    for char in text:
        # 15% de chance de faire une faute de frappe
        if random.random() < 0.15:
            try:
                # 1. Tape une lettre au pif
                wrong_char = random.choice(chars)
                element.send_keys(wrong_char)
                
                # 2. LA GROSSE PAUSE DEMANDÉE (2 à 4 secondes)
                # "Merde j'ai fait une faute..."
                time.sleep(random.uniform(2.0, 4.0))
                
                # 3. Efface
                element.send_keys(Keys.BACK_SPACE)
                
                # 4. Petite pause de reprise
                time.sleep(random.uniform(0.2, 0.5))
            except: pass
        
        # Tape la bonne lettre
        element.send_keys(char)
        
        # Rythme irrégulier (jamais la même vitesse)
        time.sleep(random.uniform(0.08, 0.35))

# ==========================================
# 2. CONFIGURATION
# ==========================================
banner()
print(f"  {Y}[KERNEL] CONFIGURATION DE LA CIBLE...{X}\n")

if not os.path.exists("/sdcard"):
    print(f"  {R}[ERROR] ACCÈS STOCKAGE REFUSÉ.{X}")
    exit()

sys.stdout.write(f"  {C}root@termux:~# {X}SET RHOST_URL  : {G}")
sys.stdout.flush()
url_profil = input().strip()

sys.stdout.write(f"  {C}root@termux:~# {X}SET DATE (Ex: 11/12/2005) : {G}")
sys.stdout.flush()
date_input = input().strip()
date_deces = date_input if date_input else datetime.now().strftime("%d/%m/%Y")

sys.stdout.write(f"  {C}root@termux:~# {X}SET BINARY_SRC : {G}")
sys.stdout.flush()
preuve_path = input().strip().strip('"\'')

sys.stdout.write(f"  {C}root@termux:~# {X}SET PROXY_MAIL : {G}")
sys.stdout.flush()
email_temp = input().strip()

if not os.path.isfile(preuve_path):
    print(f"\n  {R}[ERROR 404] FILE NOT FOUND.{X}")
    exit(1)

banner()
print(f"\n  {Y}[*] STARTING FIREFOX ENGINE...{X}\n")

# ==========================================
# 3. EXÉCUTION
# ==========================================
driver = None
try:
    loading(5, "LOCATING DRIVER...")
    gecko_path = "/data/data/com.termux/files/usr/bin/geckodriver"
    if not os.path.exists(gecko_path):
        gecko_path = "/usr/bin/geckodriver"
    
    service = Service(executable_path=gecko_path)
    options = FirefoxOptions()
    options.add_argument("--headless") 
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")
    
    loading(8, "INITIALIZING SERVICE...")
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1080, 2400)
    wait = WebDriverWait(driver, 30)

    # ==========================================
    # 🔥 LOGIN LOOP (AVEC TYPE CLUMSY) 🔥
    # ==========================================
    while True:
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"\n  {Y}[AUTH] IDENTIFICATION REQUISE{X}")
        
        EMAIL = input(f"  {C}[USER] Email : {G}").strip()
        PASSWORD = input(f"  {C}[PASS] Pass  : {G}").strip() 
        print(f"{X}", end="")

        loading(10, "CONNECTING TO LOGIN PAGE...")
        driver.get("https://www.facebook.com/")

        try:
            time.sleep(2)
            cookie_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Autoriser') or contains(text(), 'Accept') or contains(text(), 'Allow')]")
            if cookie_btns: cookie_btns[0].click()
        except: pass

        loading(20, "INJECTING CREDENTIALS (CLUMSY MODE)...")
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.clear() 
            # Utilisation de la frappe maladroite
            type_clumsy(email_field, EMAIL)
            
            pass_field = driver.find_element(By.NAME, "pass")
            pass_field.clear()
            # Utilisation de la frappe maladroite
            type_clumsy(pass_field, PASSWORD)
            
            loading(35, "ATTEMPTING LOGIN...")
            try:
                driver.find_element(By.NAME, "login").click()
            except:
                pass_field.send_keys(Keys.ENTER)
        except: pass

        loading(40, "VERIFYING STATUS...")
        time.sleep(8) 

        current_url = driver.current_url
        page_source = driver.page_source.lower()

        if "login_attempt" in current_url or "incorrect" in page_source:
            print(f"\n\n  {R}[!] ERREUR : Identifiants incorrects !{X}")
            time.sleep(2)
            continue 
        
        elif "checkpoint" in current_url or "two_step" in current_url:
            print(f"\n  {R}[!] CHECKPOINT / 2FA DÉTECTÉ.{X}")
            print(f"  {W}Validez le code sur votre appareil, puis appuyez sur Entrée.{X}")
            input()
            break 
            
        else:
            print(f"\n  {G}[SUCCESS] CONNEXION RÉUSSIE.{X}")
            break 

    # ==========================================
    # SUITE DU SCRIPT
    # ==========================================
    loading(50, "RESOLVING TARGET NODE...")
    driver.get("https://www.facebook.com/help/contact/234739086860192")
    
    # URL
    loading(60, "INJECTING PAYLOAD [FBUrl]...")
    try:
        try:
            url_field = wait.until(EC.presence_of_element_located((By.NAME, "FBUrl")))
        except:
            url_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        url_field.send_keys(url_profil)
    except: pass

    # ====================================================
    # 🔥 CORRECTION DATE (INJECTION JS) 🔥
    # ====================================================
    loading(70, f"FORCE INJECTING DATE ({date_deces})...")
    try:
        # Conversion AAAA-MM-JJ vers JJ/MM/AAAA (Format Français)
        if "-" in date_deces:
            yyyy, mm, dd = date_deces.split("-")
            date_fr = f"{dd}/{mm}/{yyyy}" 
        else:
            date_fr = date_deces # Déjà au bon format

        date_field = None
        try:
            date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
        except:
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            if len(inputs) >= 2: date_field = inputs[1]

        if date_field:
            # TECHNIQUE HACKER JS (Imparable)
            driver.execute_script(f"arguments[0].value = '{date_fr}';", date_field)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", date_field)
            # Blur pour valider
            driver.find_element(By.TAG_NAME, "body").click()
            
    except Exception as e: pass

    # Upload
    loading(80, "UPLOADING BINARY...")
    try:
        abs_path = os.path.abspath(preuve_path)
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(abs_path)
    except: pass

    # Email
    loading(85, "ROUTING PROXY...")
    try:
        try:
            email_field = driver.find_element(By.NAME, "email")
        except:
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            email_field = inputs[-1]
        email_field.send_keys(email_temp)
    except: pass

    # Envoi
    loading(90, "EXECUTING FINAL PAYLOAD...")
    time.sleep(3)
    try:
        # Clic JS pour être sûr
        submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer') or contains(text(), 'Submit') or contains(text(), 'Send')]")
        driver.execute_script("arguments[0].click();", submit_btn)
    except:
        try:
            btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            driver.execute_script("arguments[0].click();", btn)
        except: pass

    # Capture
    loading(95, "AWAITING CONFIRMATION...")
    time.sleep(8)
    
    save_path = "/sdcard/TERMUX_PROOF.png"
    driver.save_screenshot(save_path)
    loading(98, f"SAVED TO: {save_path}")

    page_source = driver.page_source.lower()
    if "merci" in page_source or "thank" in page_source:
        loading(100, "OPERATION COMPLETED.")
        print(f"\n\n  {G}╔════════════════════════════════════════╗")
        print(f"  ║   ✔ SUCCÈS : FORMULAIRE ENVOYÉ       ║")
        print(f"  ║   📁 PREUVE: /sdcard/TERMUX_PROOF.png║")
        print(f"  ╚════════════════════════════════════════╝{X}")
    else:
        loading(99, "PACKET SENT.")
        print(f"\n\n  {Y}[!] PACKET SENT. VÉRIFIEZ L'IMAGE 'TERMUX_PROOF.png'.{X}")

    input(f"\n  {W}Press Enter to exit...{X}")

except Exception as e:
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"\n  {R}[ERROR] {e}{X}")
    if driver:
        driver.save_screenshot("/sdcard/termux_crash.png")
    input()

finally:
    if driver:
        driver.quit()
