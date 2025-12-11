#!/usr/bin/env python3
import os
import sys
import getpass
import time
import random
import re
import string
from datetime import datetime
from playwright.sync_api import sync_playwright

# ==========================================
# 1. HACKER STYLE CONFIG
# ==========================================
R = "\033[91m" # Rouge
G = "\033[92m" # Vert
Y = "\033[93m" # Jaune
C = "\033[96m" # Cyan
W = "\033[97m" # Blanc
X = "\033[0m"  # Reset

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
      ║     SYSTEM OVERRIDE • GHOST PROTOCOL      ║
      ║         DEV BY: {Y}OTF x DJAMAL19{R}            ║
      ╚═══════════════════════════════════════════╝{X}
""")

def loading(percent, status=""):
    """Barre de chargement cryptique"""
    bar_len = 25
    filled_len = int(round(bar_len * percent / 100))
    bar = f"{G}█{X}" * filled_len + f"{C}░{X}" * (bar_len - filled_len)
    sys.stdout.write(f'\r  {C}[{bar}{C}] {G}{percent}%{X} :: {status}\033[K')
    sys.stdout.flush()

def type_human(page, selector, text):
    """Frappe invisible mais réaliste"""
    try:
        page.click(selector)
    except: pass
    
    time.sleep(random.uniform(0.5, 1.0))
    chars = string.ascii_lowercase + string.digits
    
    for char in text:
        if random.random() < 0.05: 
            wrong_char = random.choice(chars)
            page.type(selector, wrong_char)
            time.sleep(random.uniform(0.15, 0.4))
            page.keyboard.press("Backspace")
            time.sleep(random.uniform(0.1, 0.2))
        page.type(selector, char)
        time.sleep(random.uniform(0.05, 0.25))

# ==========================================
# 2. CONFIGURATION (GHOST MODE)
# ==========================================
banner()
print(f"  {Y}[KERNEL] INITIALIZING GHOST PROTOCOL (HEADLESS)...{X}\n")

while True:
    sys.stdout.write(f"  {C}root@otf:~# {X}SET LHOST_USER : {G}")
    sys.stdout.flush()
    EMAIL = input().strip()
    print(f"{X}", end="") 
    if EMAIL: break

while True:
    sys.stdout.write(f"  {C}root@otf:~# {X}SET LHOST_PASS : {G}")
    sys.stdout.flush()
    PASSWORD = getpass.getpass("").strip()
    print(f"{X}", end="") 
    if PASSWORD: break

print(f"\n  {R}[SYSTEM] TARGET CONFIGURATION REQUIRED{X}")

sys.stdout.write(f"  {C}root@otf:~# {X}SET RHOST_URL  : {G}")
sys.stdout.flush()
url_profil = input().strip()

sys.stdout.write(f"  {C}root@otf:~# {X}SET TIMESTAMP  : {G}")
sys.stdout.flush()
date_input = input().strip()
date_deces = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

sys.stdout.write(f"  {C}root@otf:~# {X}SET BINARY_SRC : {G}")
sys.stdout.flush()
preuve_path = input().strip().strip('"\'')

sys.stdout.write(f"  {C}root@otf:~# {X}SET PROXY_MAIL : {G}")
sys.stdout.flush()
email_temp = input().strip()

if not os.path.isfile(preuve_path):
    print(f"\n  {R}[ERROR 404] BINARY SOURCE NOT FOUND.{X}")
    exit(1)

banner()
print(f"\n  {Y}[*] RUNNING BACKGROUND PROCESS (NO GUI)...{X}\n")

# ==========================================
# 3. EXÉCUTION INVISIBLE
# ==========================================
with sync_playwright() as p:
    loading(5, "ALLOCATING VIRTUAL MEMORY...")
    
    # HEADLESS = TRUE (Le navigateur est invisible)
    browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
    
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}, # Grand écran pour belle capture
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    page = context.new_page()

    try:
        loading(10, "ESTABLISHING SECURE TUNNEL...")
        page.goto("https://www.facebook.com/", timeout=60000)

        try:
            cookie_btn = page.get_by_role("button", name=re.compile("(autoriser|accept|allow|tout accepter)", re.I))
            if cookie_btn.count() > 0:
                cookie_btn.first.click(timeout=3000)
            else:
                page.locator("button[data-cookiebanner='accept_button']").click(timeout=3000)
        except: pass

        # AUTHENTICATION
        loading(20, "INJECTING ENCRYPTED CREDENTIALS...")
        page.wait_for_selector("input[name='email']", state="visible")
        type_human(page, "input[name='email']", EMAIL)
        time.sleep(0.5)
        type_human(page, "input[name='pass']", PASSWORD)
        
        loading(35, "BYPASSING AUTH GATEWAY...")
        try:
            page.click("button[name='login']", timeout=5000)
        except:
            page.keyboard.press("Enter")
        
        # Attente silencieuse (pas de pause visuelle possible en headless)
        loading(40, "VERIFYING SESSION TOKENS...")
        time.sleep(8) 

        # Vérification si bloqué
        if "checkpoint" in page.url or "two_step" in page.url:
            sys.stdout.write("\r" + " " * 80 + "\r")
            print(f"\n  {R}[ERROR] 2FA DETECTED IN GHOST MODE.{X}")
            print(f"  {W}Screenshot saved to 'error_2fa.png'. Cannot proceed invisible.{X}")
            page.screenshot(path="error_2fa.png")
            sys.exit()

        # FORMULAIRE
        loading(50, "RESOLVING TARGET NODE...")
        time.sleep(1)
        page.goto("https://www.facebook.com/help/contact/234739086860192")
        
        # URL
        loading(60, "INJECTING PAYLOAD [TARGET_ID]...")
        try:
            page.wait_for_selector('input[name="FBUrl"]', timeout=10000)
            page.fill('input[name="FBUrl"]', url_profil)
        except:
            page.locator("input[type='text']").first.fill(url_profil)

        # DATE
        loading(70, "SPOOFING METADATA (DATE)...")
        try:
            yyyy, mm, dd = date_deces.split("-")
            date_fr = f"{dd}/{mm}/{yyyy}" 
            date_field = page.locator("input._3smp").first
            date_field.click()
            date_field.clear()
            date_field.press_sequentially(date_fr, delay=80)
            page.keyboard.press("Enter")
        except: pass

        # UPLOAD
        loading(80, "TRANSFERRING BINARY EVI...")
        page.set_input_files('input[type="file"]', preuve_path)
        
        # EMAIL
        loading(85, "ROUTING PROXY CONNECTION...")
        try:
            page.fill('input[name="email"]', email_temp)
        except:
            inputs = page.locator("input[type='text']")
            if inputs.count() > 0:
                inputs.nth(inputs.count() - 1).fill(email_temp)

        # ENVOI
        loading(90, "EXECUTING FINAL PAYLOAD...")
        time.sleep(2)
        
        try:
            bouton = page.locator("button").filter(has_text=re.compile("(Envoyer|Submit|Send)", re.I)).first
            if bouton.is_visible():
                bouton.click()
            else:
                page.locator("button[type='submit']").click()
        except: pass

        # === CAPTURE DE PREUVE (3 SECONDES APRÈS CLIC) ===
        loading(95, "AWAITING CONFIRMATION SNAPSHOT...")
        time.sleep(10) # Attente demandée
        save_path = "D:/Haxor/cyber-security/PROOF_OF_DEATH.png"
        
        # Capture de l'écran (Preuve visuelle que le formulaire est parti)
        page.screenshot(path=save_path, full_page=True)
        loading(98, "SNAPSHOT SAVED: PROOF_OF_DEATH.png")
        
        # VÉRIFICATION TEXTE
        time.sleep(1)
        if "merci" in page.content().lower() or "thank" in page.content().lower():
            loading(100, "OPERATION COMPLETED.")
            print(f"\n\n  {G}╔════════════════════════════════════════╗")
            print(f"  ║   ✔ SYSTEM STATUS: TARGET DOWN        ║")
            print(f"  ║     PROOF SAVED IN LOCAL DIR          ║")
            print(f"  ╚════════════════════════════════════════╝{X}")
        else:
            loading(99, "PACKET SENT.")
            print(f"\n\n  {Y}[!] PACKET SENT. CHECK 'PROOF_OF_DEATH.png'.{X}")
        
        print(f"\n  {C}Closing encrypted kalinux tunnel in 3s...{X}")
        time.sleep(3)
        browser.close()

    except Exception as e:
        sys.stdout.write("\r" + " " * 80 + "\r")
        print(f"\n  {R}[KERNEL PANIC] {e}{X}")
        print(f"  {Y}Creating Crash Dump 'crash.png'...{X}")
        page.screenshot(path="crash.png")
        browser.close()
