#!/bin/python3

import socket
import termcolor
import ipaddress
import pyfiglet

def scan_ports(target, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def display_open_ports(ip, ports):
    if ports:
        print(f"\n Open ports for {ip}:")
        for port in ports:
            print(termcolor.colored(f"[*]   Port {port} is open", 'green'))
    else:
        print(f"No open ports found for {ip}.")

def main():
    ascii_banner = pyfiglet.figlet_format("Tony's Port Scanner")
    print(ascii_banner)
    
    targets = input("Enter the target(s) to scan (comma-separated & CIDR accepted): ")
    target_list = [target.strip() for target in targets.split(',')]

    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    
    for target in target_list:
        print(f"\nScanning ports for {target}...")
        
        if '/' in target:  # CIDR range
            ip_range = ipaddress.IPv4Network(target, strict=False)
            for ip in ip_range.hosts():
                open_ports = scan_ports(str(ip), start_port, end_port)
                display_open_ports(ip, open_ports)
        else:  # Single host
            open_ports = scan_ports(target, start_port, end_port)
            display_open_ports(target, open_ports)

    scan_another = input("\nDo you want to scan another target? (yes/no): ")
    if scan_another.lower() == "yes":
        main()
    else:
        print("Exiting the port scanner.")

if __name__ == "__main__":
    main()
