# CyberX-Ray

## 🔥 Overview
CyberX-Ray is an advanced technology detection tool that helps identify a website's **Web Server, CDN, Firewall, and CMS**. It is designed for security researchers and penetration testers to gather information about target websites efficiently.

## 🚀 Features
- ✅ Detects **Web Server** type
- ✅ Identifies **CDN (Content Delivery Network)**
- ✅ Recognizes **Firewall Protection**
- ✅ Determines **CMS (WordPress, Joomla, Drupal, Magento, etc.)**
- ✅ Fast and efficient scanning
- ✅ Easy-to-use command-line interface

## 📌 Installation
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/Professor1711/CyberX-Ray.git
cd CyberX-Ray
```

### **Step 2: Install Dependencies**
Make sure you have Python 3 installed.
```bash
chmod +x install.sh
./install.sh
```
This will install all required dependencies automatically.

### **Manual Installation** (if needed)
```bash
pip3 install -r requirements.txt
```

## 🔍 Usage
Run CyberX-Ray using the following command:
```bash
python3 cyberx-ray.py
```
Enter the website URL when prompted:
```
Enter website URL (with http/https): https://example.com
```
The tool will then display:
- **Web Server:** Apache/Nginx/Pepyaka/etc.
- **CDN Provider:** Cloudflare, Akamai, Fastly, etc.
- **Firewall Status:** Detected or Not Detected
- **CMS Platform:** WordPress, Joomla, Drupal, etc.

## 📌 Example Output
```
PROFESSOR
Made by Virendra Kumar

Enter website URL (with http/https): https://wix.com

[+] Detecting Technologies for: https://wix.com
[+] Web Server: Pepyaka
[+] CDN: Cloudflare
[+] Firewall: Detected
[+] CMS: Wix
```

## 🛠️ Troubleshooting
- **ModuleNotFoundError**: Run `pip3 install -r requirements.txt` again.
- **Permission Denied**: Use `chmod +x install.sh` and run again.
- **Python Not Found**: Make sure Python 3 is installed (`python3 --version`).

## 📜 License
This project is open-source and distributed under the **MIT License**.

## 🤝 Credits
Developed by **Virendra Kumar**.
