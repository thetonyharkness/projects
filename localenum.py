import platform
import psutil

def get_system_info():
    system_info = platform.uname()
    print("System Information")
    print("------------------")
    print(f"System: {system_info.system}")
    print(f"Node Name: {system_info.node}")
    print(f"Release: {system_info.release}")
    print(f"Version: {system_info.version}")
    print(f"Machine: {system_info.machine}")
    print(f"Processor: {system_info.processor}")

def get_memory_info():
    memory_info = psutil.virtual_memory()
    print("\nMemory Information")
    print("------------------")
    print(f"Total Memory: {round(memory_info.total / (1024**3), 2)} GB")
    print(f"Available Memory: {round(memory_info.available / (1024**3), 2)} GB")
    print(f"Used Memory: {round(memory_info.used / (1024**3), 2)} GB")

def get_cpu_info():
    print("\nCPU Information")
    print("----------------")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical)")
    print(f"CPU Threads: {psutil.cpu_count(logical=True)} (Logical)")

def get_disk_info():
    disk_info = psutil.disk_usage('/')
    print("\nDisk Information")
    print("----------------")
    print(f"Total Disk Space: {round(disk_info.total / (1024**3), 2)} GB")
    print(f"Used Disk Space: {round(disk_info.used / (1024**3), 2)} GB")
    print(f"Free Disk Space: {round(disk_info.free / (1024**3), 2)} GB")

def get_network_info():
    network_info = psutil.net_if_addrs()
    print("\nNetwork Information")
    print("-------------------")
    for interface, addresses in network_info.items():
        print(f"Interface: {interface}")
        for address in addresses:
            print(f"  Address: {address.address}")

def get_installed_software():
    software_info = psutil.disk_partitions()
    print("\nInstalled Software")
    print("------------------")
    for software in software_info:
        print(f"Drive: {software.device}")
        print(f"  Mountpoint: {software.mountpoint}")
        print(f"  File System Type: {software.fstype}")

if __name__ == "__main__":
    get_system_info()
    get_memory_info()
    get_cpu_info()
    get_disk_info()
    get_network_info()
    get_installed_software()
