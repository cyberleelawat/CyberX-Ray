import requests
from termcolor import colored
import re

# Banner print function
def print_banner():
    print(colored("\nPROFESSOR\n", "cyan"))
    print("Made by Virendra Kumar\n")

# Fetch website headers and content
def fetch_website(url):
    try:
        response = requests.get(url, timeout=10)
        return response.headers, response.text.lower()
    except requests.RequestException as e:
        print("Error fetching website:", e)
        return None, None

# Detect technologies
def detect_technologies(url):
    headers, body = fetch_website(url)
    if not headers or not body:
        return

    print("\n[+] Detecting Technologies for:", url)

    # Detect Web Server
    print("[+] Web Server:", headers.get("Server", "Not Found"))

    # Detect CDN
    cdn_providers = {
        "Cloudflare": "cf-ray",
        "Akamai": "akamaighost",
        "Fastly": "fastly",
        "Amazon CloudFront": "cloudfront"
    }
    cdn_detected = next((name for name, identifier in cdn_providers.items() if identifier in headers), "No CDN detected")
    print("[+] CDN:", cdn_detected)

    # Detect Firewall
    firewall_signatures = ["x-sucuri-id", "x-sucuri-cache", "cf-ray", "mod_security"]
    firewall_detected = any(signature in headers for signature in firewall_signatures)
    print("[+] Firewall:", "Detected" if firewall_detected else "No Firewall detected")

    # **Optimized CMS Detection**
    cms_signatures = {
        "WordPress": ["wp-content", "wp-includes", "wp-json", "generator\" content=\"wordpress"],
        "Joomla": ["joomla.js", "com_content", "generator\" content=\"joomla"],
        "Drupal": ["sites/default/files", "drupal.js", "generator\" content=\"drupal"],
        "Magento": ["mage/", "magento", "skin/frontend", "varien"],
        "Shopify": ["shopify", "cdn.shopify.com", "shopify.js"],
        "Wix": ["wix.com", "wix-static", "wixapps.net"],
        "Blogger": ["blogspot", "blogger"],
        "Squarespace": ["squarespace"],
        "Ghost": ["ghost/content"],
    }

    detected_cms = None  # Start with no CMS detected

    for cms, signatures in cms_signatures.items():
        matches = [sig for sig in signatures if sig in body]

        # If multiple matches found, select highest priority CMS
        if len(matches) > 1:
            detected_cms = cms
            break  # Stop checking once we get a strong match

        # If no strong match, take the first one found
        if not detected_cms and matches:
            detected_cms = cms

    print("[+] CMS:", detected_cms if detected_cms else "No CMS detected")

if __name__ == "__main__":
    print_banner()
    url = input("Enter website URL (with http/https): ")
    detect_technologies(url)

