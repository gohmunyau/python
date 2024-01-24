

import psutil
import socket
import requests
 
class SystemMonitor:
    @staticmethod
    def check_disk_usage(threshold_percent=20):
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > threshold_percent
 
    @staticmethod
    def check_cpu_utilization(threshold_percent=75):
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < threshold_percent
 
    @staticmethod
    def check_localhost_availability():
        try:
            socket.create_connection(("localhost", 80), timeout=1)
            return True
        except (socket.error, ConnectionRefusedError):
            return False
 
    @staticmethod
    def check_internet_availability():
        try:
            requests.get("http://www.google.com", timeout=1)
            return True
        except requests.ConnectionError:
            return False
 
def main():
    monitor = SystemMonitor()
 
    disk_check = monitor.check_disk_usage()
    cpu_check = monitor.check_cpu_utilization()
    localhost_check = monitor.check_localhost_availability()
    internet_check = monitor.check_internet_availability()
 
    if not (disk_check and cpu_check):
        print("ERROR! Disk usage or CPU usage failed.")
    elif localhost_check and internet_check:
        print("Everything is OK.")
    else:
        print("Network checks failed. Localhost or internet access is not operational.")
 
if __name__ == "__main__":
    main()
