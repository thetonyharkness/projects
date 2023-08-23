#!/bin/python3

import socket
import termcolor
import ipaddress
import pyfiglet

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    ascii_banner = pyfiglet.figlet_format("tony's port scanner")
    print(ascii_banner)
    
    targets = input("Enter the target(s) to scan: ")
    target_list = targets.split(',')
    
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    for target in target_list:
        target = target.strip()
        print(f"\nScanning ports for {target}...")
        
        if '/' in target:  # CIDR range
            ip_range = ipaddress.IPv4Network(target, strict=False)
            for ip in ip_range.hosts():
                open_ports = scan_ports(str(ip), start_port, end_port)
                if open_ports:
                    print(f"\n Open ports for {ip}:")
                    for port in open_ports:
                        print(termcolor.colored(f"[*]   Port {port} is open", 'green'))
        else:  # Single host
            open_ports = scan_ports(target, start_port, end_port)
            if open_ports:
                print("\n[*] Open ports:")
                for port in open_ports:
                    print(termcolor.colored(f"[*]   Port {port} is open", 'green'))
            else:
                print(f"No open ports found for {target}.")

    scan_another = input("\nDo you want to scan another target? (yes/no): ")
    if scan_another.lower() == "yes":
        main()
    else:
        print("Exiting the port scanner.")

if __name__ == "__main__":
    main()
