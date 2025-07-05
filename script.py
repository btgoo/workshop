import psutil
import os

def bytes_to_gb(bytes_value):
    """Convert bytes to gigabytes."""
    return bytes_value / (1024 ** 3)

def display_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

def display_disk_usage():
    disk_stats = psutil.disk_usage(os.getcwd())
    print("\nDisk Usage:")
    print(f"  Total: {bytes_to_gb(disk_stats.total):.2f} GB")
    print(f"  Used: {bytes_to_gb(disk_stats.used):.2f} GB")
    print(f"  Free: {bytes_to_gb(disk_stats.free):.2f} GB")
    print(f"  Usage Percentage: {disk_stats.percent}%")

def display_memory_usage():
    mem_stats = psutil.virtual_memory()
    print("\nMemory (RAM) Usage:")
    print(f"  Total: {bytes_to_gb(mem_stats.total):.2f} GB")
    print(f"  Available: {bytes_to_gb(mem_stats.available):.2f} GB")
    print(f"  Used: {bytes_to_gb(mem_stats.used):.2f} GB")
    print(f"  Free: {bytes_to_gb(mem_stats.free):.2f} GB")
    print(f"  Usage Percentage: {mem_stats.percent}%")

def main():
    display_cpu_usage()
    display_disk_usage()
    display_memory_usage()

if __name__ == "__main__":
    main()
