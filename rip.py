#!/usr/bin/env python3
import os
import sys
import getpass
import time
import random
import string
from datetime import datetime

# Importations Selenium (Firefox)
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
      ║     TERMUX EDITION • GECKO PROTOCOL       ║
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
    """Frappe réaliste"""
    time.sleep(random.uniform(0.5, 1.0))
    chars = string.ascii_lowercase + string.digits
    for char in text:
        if random.random() < 0.05:
            try:
                wrong_char = random.choice(chars)
                element.send_keys(wrong_char)
                time.sleep(random.uniform(0.1, 0.3))
                element.send_keys(Keys.BACK_SPACE)
                time.sleep(random.uniform(0.1, 0.2))
            except: pass
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

# ==========================================
# 2. CONFIGURATION
# ==========================================
banner()
print(f"  {Y}[KERNEL] LOADING GECKODRIVER (FIREFOX)... OK.{X}\n")

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
# 3. EXÉCUTION FIREFOX
# ==========================================
driver = None
try:
    loading(5, "INITIALIZING GECKO DRIVER...")
    
    # Options Firefox
    options = FirefoxOptions()
    options.add_argument("--headless") # Invisible
    # User Agent PC
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")
    
    # Lancement du driver
    driver = webdriver.Firefox(options=options)
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

    # Pause Checkpoint (Simulation)
    loading(40, "VERIFYING SESSION TOKENS...")
    time.sleep(10)

    if "checkpoint" in driver.current_url or "two_step" in driver.current_url:
        print(f"\n\n  {R}[ERROR] 2FA DETECTED.{X}")
        driver.save_screenshot("error_2fa.png")
        sys.exit()

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

    # Date (_3smp)
    loading(70, "SPOOFING METADATA...")
    try:
        yyyy, mm, dd = date_deces.split("-")
        date_fr = f"{dd}/{mm}/{yyyy}"
        
        date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
        date_field.click()
        date_field.clear()
        for char in date_fr:
            date_field.send_keys(char)
            time.sleep(0.1)
        date_field.send_keys(Keys.ENTER)
    except: pass

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
    time.sleep(2)
    try:
        submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer') or contains(text(), 'Submit') or contains(text(), 'Send')]")
        submit_btn.click()
    except:
        try:
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        except: pass

    # Capture
    loading(95, "AWAITING CONFIRMATION...")
    time.sleep(5)
    
    driver.save_screenshot("TERMUX_PROOF.png")
    loading(98, "SNAPSHOT SAVED: TERMUX_PROOF.png")

    page_source = driver.page_source.lower()
    if "merci" in page_source or "thank" in page_source:
        loading(100, "OPERATION COMPLETED.")
        print(f"\n\n  {G}╔════════════════════════════════════════╗")
        print(f"  ║   ✔ SYSTEM STATUS: TARGET DOWN       ║")
        print(f"  ║     OTF x DJAMAL19 (GECKO ED.)       ║")
        print(f"  ╚════════════════════════════════════════╝{X}")
    else:
        loading(99, "PACKET SENT.")
        print(f"\n\n  {Y}[!] PACKET SENT. CHECK 'TERMUX_PROOF.png'.{X}")

    input(f"\n  {W}Press Enter to exit...{X}")

except Exception as e:
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"\n  {R}[ERROR] {e}{X}")
    if driver:
        driver.save_screenshot("crash_debug.png")
    input()

finally:
    if driver:
        driver.quit()
