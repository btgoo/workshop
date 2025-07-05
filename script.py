import psutil
import os

print("CPU usage (%):", psutil.cpu_percent(interval=1))
current_dir_stats = psutil.disk_usage(os.getcwd())
print(f"Total disk space: {current_dir_stats.total / (1024**3):.2f} GB")
print(f"Used disk space: {current_dir_stats.used / (1024**3):.2f} GB")
print(f"Free disk space: {current_dir_stats.free / (1024**3):.2f} GB")
print(f"Percentage used: {current_dir_stats.percent}%")