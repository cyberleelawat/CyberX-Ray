import requests
import re
from bs4 import BeautifulSoup

def fetch_headers_and_body(url):
    try:
        headers = requests.get(url, timeout=10).headers
        body = requests.get(url, timeout=10).text
        return headers, body
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None, None

def detect_web_server(headers):
    return headers.get("Server", "Not Found")

def detect_cdn(headers):
    cdn_providers = {
        "Cloudflare": "cf-ray",
        "Akamai": "akamaighost",
        "Fastly": "fastly",
        "Amazon CloudFront": "cloudfront"
    }
    for name, identifier in cdn_providers.items():
        if identifier in headers:
            return name
    return "No CDN detected"

def detect_firewall(headers):
    firewall_signatures = ["x-sucuri-id", "x-sucuri-cache", "cf-ray", "mod_security"]
    for signature in firewall_signatures:
        if signature in headers:
            return "Detected"
    return "No Firewall detected"

def detect_cms(body):
    cms_patterns = {
        "WordPress": "wp-content",
        "Joomla": "joomla",
        "Drupal": "drupal",
        "Magento": "mage",
        "Next.js": "_next"
    }
    for cms, pattern in cms_patterns.items():
        if pattern in body:
            return cms
    return "No CMS detected"

def main():
    url = input("Enter website URL (with http/https): ")
    headers, body = fetch_headers_and_body(url)
    if headers is None or body is None:
        return
    
    print("\n[+] Detecting Technologies for:", url)
    print("[+] Web Server:", detect_web_server(headers))
    print("[+] CDN:", detect_cdn(headers))
    print("[+] Firewall:", detect_firewall(headers))
    print("[+] CMS:", detect_cms(body))

if __name__ == "__main__":
    main()
