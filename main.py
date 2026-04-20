import platform
import psutil

def get_system_info():
    print("=== SYSTEM INFO ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")

def get_cpu_info():
    print("\n=== CPU INFO ===")
    print(f"Processor: {platform.processor()}")
    print(f"Cores: {psutil.cpu_count(logical=False)}")
    print(f"Threads: {psutil.cpu_count(logical=True)}")
    print(f"Usage: {psutil.cpu_percent(interval=1)}%")

def get_ram_info():
    print("\n=== RAM INFO ===")
    ram = psutil.virtual_memory()
    print(f"Total: {ram.total / (1024**3):.2f} GB")
    print(f"Used: {ram.used / (1024**3):.2f} GB")
    print(f"Usage: {ram.percent}%")

def get_disk_info():
    print("\n=== STORAGE INFO ===")
    disk = psutil.disk_usage('/')
    print(f"Total: {disk.total / (1024**3):.2f} GB")
    print(f"Used: {disk.used / (1024**3):.2f} GB")
    print(f"Usage: {disk.percent}%")

def get_battery_info():
    print("\n=== BATTERY INFO ===")
    battery = psutil.sensors_battery()
    if battery:
        print(f"Percentage: {battery.percent}%")
        print(f"Charging: {battery.power_plugged}")
    else:
        print("No battery detected")

if __name__ == "__main__":
    get_system_info()
    get_cpu_info()
    get_ram_info()
    get_disk_info()
    get_battery_info()
