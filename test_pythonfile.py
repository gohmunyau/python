"""
Module docstring explaining the purpose of the pythonfile module.
"""

import socket
import unittest
import psutil
import requests

from pythonfile import SystemMonitor

class TestSystemMonitor(unittest.TestCase):
    def test_disk_usage(self):
        # Your test code here
        pass

    def test_cpu_utilization(self):
        # Your test code here
        pass


class SystemMonitor:
    """
    A class to monitor system resources and network availability.
    """

    @staticmethod
    def check_disk_usage(threshold_percent=20):
        """
        Check disk usage and return True if it's below the threshold.

        :param threshold_percent: Disk usage threshold percentage.
        :return: True if disk usage is below the threshold, False otherwise.
        """
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > threshold_percent

    @staticmethod
    def check_cpu_utilization(threshold_percent=75):
        """
        Check CPU utilization and return True if it's below the threshold.

        :param threshold_percent: CPU utilization threshold percentage.
        :return: True if CPU utilization is below the threshold, False otherwise.
        """
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < threshold_percent

    @staticmethod
    def check_localhost_availability():
        """
        Check if localhost is reachable on port 80.

        :return: True if localhost is reachable, False otherwise.
        """
        try:
            socket.create_connection(("localhost", 80), timeout=1)
            return True
        except (socket.error, ConnectionRefusedError):
            return False

    @staticmethod
    def check_internet_availability():
        """
        Check if internet is reachable by making a request to google.com.

        :return: True if internet is reachable, False otherwise.
        """
        try:
            requests.get("http://www.google.com", timeout=1)
            return True
        except requests.ConnectionError:
            return False

def main():
    """
    The main function to run system and network checks.
    """
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
