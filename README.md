


# Automated Network Scanner
![GitHub Logo](https://github.com/Aleem20/Automated-Network-Scanner/blob/main/images/main.PNG)

Automated Network Scanner is a Python-based script designed for network exploration and security auditing. This automated scanner simplifies the process of scanning local networks, allowing users to identify active hosts, open ports, running services, and potential vulnerabilities. It integrates the power of NMAP, a renowned network scanning tool, into an interactive and user-friendly interface.

# Features


**Automated Network Scanner:** This tool provides automated scanning of local networks for active hosts, services and determing vulnerabilities.

 **Interactive User Interface:** Users are presented with a menu-driven interface, allowing them to choose specific scan options based on their requirements.

**Local IP Detection:** The program automatically detects the user's local IP address, making it user-friendly and reducing manual input.

**Error Handling:** Includes error handling mechanisms to notify users about any issues during the scanning process.

**Reusability:** Allows users to re-run the program multiple times without restarting.

**Multiple Scan Options:**

![GitHub Logo](https://github.com/Aleem20/Automated-Network-Scanner/blob/main/images/sn1.PNG)
- **Scan for Open Ports:** Identifies all active hosts with open ports.

 
 ![GitHub Logo](https://github.com/Aleem20/Automated-Network-Scanner/blob/main/images/sn2.PNG)

- **Scan First 1000 Ports:** Determines running services on the first 1000 ports of active hosts.

  
![GitHub Logo](https://github.com/Aleem20/Automated-Network-Scanner/blob/main/images/sn3.PNG)
- **Comprehensive Scan:** Scans all open ports on all active hosts, checking for vulnerabilities in running services.


![GitHub Logo](https://github.com/Aleem20/Automated-Network-Scanner/blob/main/images/sn4.PNG)
- **Scan Vulnerabilities:** Identifies potential vulnerabilities on services running on the first 1000 ports of active hosts.

I will be adding more scanning options in the future.
# Requirements
- [Python 3](https://www.python.org/)
-  [NMAP](https://nmap.org/)




## Installation

Make sure to install Python and NMAP before running this script.

This script could be run on Windows or Linux systems. 
```bash
git clone https://github.com/Aleem20/Automated-Network-Scanner.git
cd Automated-Network-Scanner
python3 ANscanner.py
```
    
## Acknowledgements

 - [NMAP](https://nmap.org/)

**Usage Guidelines:**

**Educational Use Only:** This tool is meant for educational purposes only.

**Authorized Networks:** Only scan networks and hosts for which you have explicit authorization.

**Respect Privacy:** Avoid scanning private networks or systems without permission.

**No Malicious Intent:** Do not use this tool for any harmful or malicious activities.
