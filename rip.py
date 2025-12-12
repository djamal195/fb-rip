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
# 1. CONFIGURATION VISUELLE
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
      TERMUX EDITION • JS INJECTION FIX
      {R}╔═══════════════════════════════════════════╗
      ║    FORCE DATE VALIDATION (JAVASCRIPT)     ║
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
    chars = string.ascii_lowercase + string.digits
    for char in text:
        if random.random() < 0.05:
            try:
                wrong_char = random.choice(chars)
                element.send_keys(wrong_char)
                time.sleep(random.uniform(0.1, 0.3))
                element.send_keys(Keys.BACK_SPACE)
            except: pass
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# ==========================================
# 2. CONFIGURATION
# ==========================================
banner()
print(f"  {Y}[KERNEL] CHECKING STORAGE PERMISSIONS...{X}\n")

if not os.path.exists("/sdcard"):
    print(f"  {R}[ERROR] ACCÈS STOCKAGE REFUSÉ.{X}")
    print(f"  Tapez: {Y}termux-setup-storage{X} dans Termux.")
    exit()

while True:
    sys.stdout.write(f"  {C}root@termux:~# {X}SET LHOST_USER : {G}")
    sys.stdout.flush()
    EMAIL = input().strip()
    print(f"{X}", end="") 
    if EMAIL: break

while True:
    sys.stdout.write(f"  {C}root@termux:~# {X}SET LHOST_PASS : {G}")
    sys.stdout.flush()
    PASSWORD = getpass.getpass("").strip()
    print(f"{X}", end="") 
    if PASSWORD: break

print(f"\n  {R}[SYSTEM] TARGET CONFIGURATION REQUIRED{X}")

sys.stdout.write(f"  {C}root@termux:~# {X}SET RHOST_URL  : {G}")
sys.stdout.flush()
url_profil = input().strip()

sys.stdout.write(f"  {C}root@termux:~# {X}SET TIMESTAMP  : {G}")
sys.stdout.flush()
date_input = input().strip()
date_deces = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

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

    # Navigation
    loading(10, "CONNECTING TO META SERVERS...")
    driver.get("https://www.facebook.com/")

    # Cookies
    try:
        time.sleep(2)
        cookie_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Autoriser') or contains(text(), 'Accept') or contains(text(), 'Allow')]")
        if cookie_btns:
            cookie_btns[0].click()
    except: pass

    # Auth
    loading(20, "INJECTING CREDENTIALS...")
    try:
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        type_human(email_field, EMAIL)
        time.sleep(0.5)
        
        pass_field = driver.find_element(By.NAME, "pass")
        type_human(pass_field, PASSWORD)
        
        loading(35, "BYPASSING GATEWAY...")
        try:
            driver.find_element(By.NAME, "login").click()
        except:
            pass_field.send_keys(Keys.ENTER)
    except: pass

    loading(40, "VERIFYING SESSION...")
    time.sleep(10)

    # Formulaire
    loading(50, "RESOLVING TARGET NODE...")
    driver.get("https://www.facebook.com/help/contact/234739086860192")
    
    # URL (FBUrl)
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
    loading(70, "FORCE INJECTING DATE (JS)...")
    try:
        # Conversion
        yyyy, mm, dd = date_deces.split("-")
        date_fr = f"{dd}/{mm}/{yyyy}" # 12/05/2025
        
        # Trouver le champ (Classe _3smp)
        date_field = None
        try:
            date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
        except:
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            if len(inputs) >= 2: date_field = inputs[1]

        if date_field:
            # TECHNIQUE HACKER : On force la valeur directement dans le moteur du navigateur
            # On utilise JavaScript pour dire "La valeur est X" et "J'ai fini de taper"
            driver.execute_script(f"arguments[0].value = '{date_fr}';", date_field)
            
            # On simule l'événement 'input' pour que Facebook React réagisse
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", date_field)
            
            # On clique ailleurs pour valider (Blur)
            driver.find_element(By.TAG_NAME, "body").click()
            time.sleep(1)
            
    except Exception as e: 
        print(f"\n[DEBUG DATE] {e}")

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
        # On utilise JS pour cliquer aussi, c'est plus sûr
        driver.execute_script("arguments[0].click();", submit_btn)
    except:
        try:
            btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            driver.execute_script("arguments[0].click();", btn)
        except: pass

    # Capture
    loading(95, "AWAITING CONFIRMATION...")
    time.sleep(8) # On attend un peu plus pour l'upload
    
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
        # Si ça a échoué, on sauvegarde aussi le HTML pour comprendre
        with open("/sdcard/debug_page.html", "w") as f:
            f.write(driver.page_source)

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
