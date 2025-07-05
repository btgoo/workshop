import psutil
import os

print("CPU usage (%):", psutil.cpu_percent(interval=1))
current_dir_stats = psutil.disk_usage(os.getcwd())
print(f"Total disk space: {current_dir_stats.total / (1024**3):.2f} GB")
print(f"Used disk space: {current_dir_stats.used / (1024**3):.2f} GB")
print(f"Free disk space: {current_dir_stats.free / (1024**3):.2f} GB")
print(f"Percentage used: {current_dir_stats.percent}%\n")

mem_info = psutil.virtual_memory()

print(f"Total RAM: {mem_info.total / (1024**3):.2f} GB")
print(f"Available RAM: {mem_info.available / (1024**3):.2f} GB")
print(f"Used RAM: {mem_info.used / (1024**3):.2f} GB")
print(f"Free RAM: {mem_info.free / (1024**3):.2f} GB")
print(f"RAM Usage Percentage: {mem_info.percent}%")
