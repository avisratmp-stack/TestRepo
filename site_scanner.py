#!/usr/bin/env python3
"""
Site Scanner - Monitors ynet.co.il for the Hebrew word "יש"
Scans every 1 minute and alerts when the word is found.
"""

import requests
import time
import sys
from datetime import datetime

# Configuration
URL = "https://confluence/spaces/IPAAS/overview"
SEARCH_WORD = "Yisrealian"
SCAN_INTERVAL_SECONDS = 60  # 1 minute


def fetch_page(url):
    """Fetch the webpage content."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[{get_timestamp()}] Error fetching page: {e}")
        return None


def get_timestamp():
    """Get current timestamp for logging."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def search_word(content, word):
    """Search for the word in the content and return occurrences count."""
    if content is None:
        return 0
    return content.count(word)


def alert_user(word, count, url):
    """Alert the user that the word was found."""
    print("\n" + "=" * 60)
    print("🚨 ALERT! WORD FOUND! 🚨")
    print("=" * 60)
    print(f"Time: {get_timestamp()}")
    print(f"Word searched: '{word}'")
    print(f"Occurrences found: {count}")
    print(f"Data source: {url}")
    print("=" * 60 + "\n")

    # Try to play a system beep/sound for alert
    try:
        print('\a')  # Terminal bell
    except:
        pass


def run_scanner():
    """Main scanner loop."""
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║                    YNET SITE SCANNER                         ║
║                                                              ║
║  Target URL: {URL:<47} ║
║  Search word: {SEARCH_WORD:<46} ║
║  Scan interval: {SCAN_INTERVAL_SECONDS} seconds{' ' * 36}║
╚══════════════════════════════════════════════════════════════╝
""")

    print(f"[{get_timestamp()}] Scanner started. Press Ctrl+C to stop.\n")

    scan_count = 0
    total_finds = 0

    try:
        while True:
            scan_count += 1
            print(f"[{get_timestamp()}] Scan #{scan_count} - Fetching {URL}...")

            content = fetch_page(URL)

            if content:
                count = search_word(content, SEARCH_WORD)
                total_finds += count

                if count > 0:
                    alert_user(SEARCH_WORD, count, URL)
                else:
                    print(f"[{get_timestamp()}] Word '{SEARCH_WORD}' not found in this scan.")
            else:
                print(f"[{get_timestamp()}] Failed to fetch page content.")

            print(f"[{get_timestamp()}] Next scan in {SCAN_INTERVAL_SECONDS} seconds...\n")
            time.sleep(SCAN_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print(f"\n[{get_timestamp()}] Scanner stopped by user.")
        print(f"Total scans performed: {scan_count}")
        print(f"Total occurrences found: {total_finds}")
        sys.exit(0)


if __name__ == "__main__":
    run_scanner()
