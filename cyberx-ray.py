import requests
from termcolor import colored

def print_banner():
    print(colored("\nPROFESSOR\n", "cyan"))
    print("Made by Virendra Kumar\n")

def fetch_website(url):
    try:
        response = requests.get(url, timeout=10)
        return response.headers, response.text
    except requests.RequestException as e:
        print("Error fetching website:", e)
        return None, None

def detect_technologies(url):
    headers, body = fetch_website(url)
    if headers is None:
        return
    
    print("\n[+] Detecting Technologies for:", url)
    
    # Detect Web Server
    web_server = headers.get("Server", "Not Found")
    print(f"[+] Web Server: {web_server}")
    
    # Detect CDN
    cdn_providers = {
        "Cloudflare": "cf-ray",
        "Akamai": "akamaighost",
        "Fastly": "fastly",
        "Amazon CloudFront": "cloudfront",
    }
    cdn_detected = "No CDN detected"
    for name, identifier in cdn_providers.items():
        if identifier in headers or identifier in body.lower():
            cdn_detected = name
            break
    print(f"[+] CDN: {cdn_detected}")
    
    # Detect Firewall
    firewall_detected = "No Firewall detected"
    firewall_signatures = ["x-sucuri-id", "x-sucuri-cache", "cf-ray", "mod_security"]
    for signature in firewall_signatures:
        if signature in headers:
            firewall_detected = "Detected"
            break
    print(f"[+] Firewall: {firewall_detected}")
    
    # Detect CMS
    cms_detected = "No CMS detected"
    cms_signatures = {
        "WordPress": ["wp-content", "wp-includes", "wp-json"],
        "Joomla": ["joomla", "Joomla.js"],
        "Drupal": ["drupal", "sites/default/files"],
        "Magento": ["Mage", "Magento", "skin/frontend"],
        "Next.js": ["_next", "__NEXT_DATA__"],
    }
    
    for name, signatures in cms_signatures.items():
        if any(sig.lower() in body.lower() for sig in signatures):
            cms_detected = name
            break
    print(f"[+] CMS: {cms_detected}")

if __name__ == "__main__":
    print_banner()
    url = input("Enter website URL (with http/https): ")
    detect_technologies(url)
