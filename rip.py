#!/usr/bin/env python3
import os
import sys
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
# 1. STYLE & CONFIG
# ==========================================
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
C = "\033[96m"
W = "\033[97m"
X = "\033[0m"

def clear():
    os.system('clear')

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
      ║   TERMUX EDITION • CLUMSY HUMAN TYPING    ║
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
# 🔥 IA DE FRAPPE MALADROITE (ANTI-CHECKPOINT) 🔥
# ==========================================
def type_clumsy_human(element, text):
    """
    Simule un humain très lent qui fait des fautes et réfléchit.
    """
    # Pause initiale avant de commencer à taper
    time.sleep(random.uniform(0.5, 1.5))
    
    chars = string.ascii_lowercase + string.digits
    
    for char in text:
        # 15% de chance de faire une faute (C'est beaucoup, pour faire vrai)
        if random.random() < 0.15:
            try:
                # 1. On tape une mauvaise lettre
                wrong_char = random.choice(chars)
                element.send_keys(wrong_char)
                
                # 2. PAUSE DE RÉFLEXION (DEMANDÉE : ~3 SECONDES)
                # Le bot s'arrête comme s'il disait "Ah merde..."
                time.sleep(random.uniform(2.0, 3.5))
                
                # 3. On efface
                element.send_keys(Keys.BACK_SPACE)
                
                # 4. Petite pause après correction
                time.sleep(random.uniform(0.2, 0.5))
            except: pass
        
        # On tape la bonne lettre
        element.send_keys(char)
        
        # Vitesse de frappe très irrégulière (entre 0.1s et 0.4s par lettre)
        time.sleep(random.uniform(0.1, 0.45))

# ==========================================
# 2. CONFIGURATION CIBLE
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
    # 🔥 BOUCLE DE CONNEXION (LOGIN LOOP) 🔥
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
            type_clumsy_human(email_field, EMAIL)
            
            pass_field = driver.find_element(By.NAME, "pass")
            pass_field.clear()
            # Utilisation de la frappe maladroite
            type_clumsy_human(pass_field, PASSWORD)
            
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

    # Date
    loading(70, f"SPOOFING DATE ({date_deces})...")
    try:
        date_field = None
        try:
            date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
        except:
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            if len(inputs) >= 2: date_field = inputs[1]

        if date_field:
            date_field.click()
            time.sleep(0.5)
            date_field.send_keys(date_deces)
            time.sleep(0.5)
            date_field.send_keys(Keys.TAB) # Validation TAB
            
            if not date_field.get_attribute("value"):
                 driver.execute_script(f"arguments[0].value = '{date_deces}';", date_field)
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
        submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer') or contains(text(), 'Submit') or contains(text(), 'Send')]")
        submit_btn.click()
    except:
        try:
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
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
