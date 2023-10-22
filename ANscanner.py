import subprocess 
import socket
import ipaddress

def generate_banner(tool_name):
    banner = f"""
               **************************************************
               *                                                *
               *       Welcome to Automated Network Scanner     *
               *                                                *
               * Warning: This tool is intended for educational *
               *               purposes only!                   *
               *                                                *
               *            https://github.com/Aleem20          *
               *                                                *
               *  Read more about NMAP at: https://nmap.org/    *    
               **************************************************
"""
    print(banner)
# function to find the local ip
def find_local_ip():
    try: 
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except Exception as error:
        print("Error:", error)
        return None

# function to calculate IP subnet range based upon the local IP
def find_subnet_range(ip):
    network_obj = ipaddress.ip_network(f"{ip}/24", strict=False)
    return network_obj

# function to scan all the active hosts in the subnet

def scan_subnet(subnet, ports="1-65535", script=None):
    try:
        if script:
            command = f'nmap -p {ports} -sV --script {script} {subnet}'
        else:
            command = f'nmap -p {ports} -sV {subnet}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as error:
        print(f"Error occurred: {error}")
        return None

# function to print results about the scanned subnets

def ip_range(subnet):
    print(f"The IP range is {subnet.network_address} - {subnet.broadcast_address} ({len(list(subnet.hosts()))} hosts)")

if __name__ == "__main__":
    tool_name = ""
    
    while True:
        generate_banner(tool_name)

        local_ip = find_local_ip()

        if local_ip:
            print(f"Your local IP Address is: {local_ip}")
            subnet = find_subnet_range(local_ip)
            print(f"The calculated CIDR notation is: {subnet}")
            ip_range(subnet)
            
            # Asks users for their choice of scan
            
            print()
            print("Choose a scan option:")
            print()
            print("1. Scan all active hosts for open ports")
            print("2. Scan all active hosts for the first 1000 ports and determine the running services")
            print("3. Scan all hosts on all open ports to determine if any running services have vulnerabilities")
            print("4. Scan all active hosts for the first 1000 ports to identify if any services have vulnerabilities")

            print()
            choice = input("Enter your choice (1/2/3/4): ")
            
            #based on choice run the appropriate scan
            
            if choice == "1":
                print()
                print("Scanning all active hosts to find if there are any open ports and determine running services.....")
                scan_result = scan_subnet(subnet)
                
            elif choice == "2":
                print()
                print("Scanning all the active hosts for the first 1000 ports to determine running services.....")
                scan_result = scan_subnet(subnet, ports="1-1000")
                
            elif choice == "3":
                print()
                print("Scanning all the active hosts on all ports to determine if any running services have vulnerabilities.....")
                scan_result = scan_subnet(subnet, script="vuln")
            
            elif choice == "4":
                print()
                print("Scanning all active hosts on the first 1000 ports to determine if any running services have vulnerabilities.....")
                scan_result = scan_subnet(subnet, ports="1-1000", script="vuln")
            else:
                print("Invalid choice.") # Error handling, print invalid choice if any other option is entered
                scan_result = None

            if scan_result:
                print()
                print("Scan Results:")
                print()
                print(scan_result)
            else:
                print("Scan failed or no vulnerabilities found.") # Error handling, print error message if scan was unsuccessful
        else:
            print("Unable to retrieve local IP address.") #Error handling, print error if unable to find the local IP
        print()
        run_again = input("Do you want to run the program again? (yes/no): ") # ask the users if they wants to run the program again or exit the loop
        if run_again.lower() != 'yes':
            break
