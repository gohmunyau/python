import unittest
from unittest.mock import patch
import psutil
import requests


class SystemMonitor:
    @staticmethod
    def check_disk_usage():
        disk_usage = psutil.disk_usage('/')
        return disk_usage.percent > 20

    @staticmethod
    def check_cpu_utilization():
        cpu_utilization = psutil.cpu_percent()
        return cpu_utilization < 75

    @staticmethod
    def check_localhost_availability():
        try:
            socket_info = psutil.net_if_addrs()
            return 'lo' in socket_info
        except Exception as e:
            print(f"Error checking localhost availability: {e}")
            return False

    @staticmethod
    def check_internet_availability():
        try:
            response = requests.get("http://www.google.com", timeout=5)
            return response.status_code == 200
        except requests.ConnectionError:
            return False


class TestSystemMonitor(unittest.TestCase):
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        self.assertTrue(SystemMonitor.check_disk_usage())
        mock_disk_usage.assert_called_once_with('/')

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 70
        self.assertTrue(SystemMonitor.check_cpu_utilization())
        mock_cpu_percent.assert_called_once()

    @patch('psutil.net_if_addrs')
    def test_check_localhost_availability(self, mock_net_if_addrs):
        mock_net_if_addrs.return_value = {'lo': [1, 2, 3]}
        self.assertTrue(SystemMonitor.check_localhost_availability())
        mock_net_if_addrs.assert_called_once()

    @patch('requests.get')
    def test_check_internet_availability(self, mock_requests_get):
        response_mock = unittest.mock.Mock()
        response_mock.status_code = 200
        mock_requests_get.return_value = response_mock
        self.assertTrue(SystemMonitor.check_internet_availability())
        mock_requests_get.assert_called_once_with("http://www.google.com", timeout=5)

    def main():
    monitor = SystemMonitor()
    disk_status = monitor.check_disk_usage()
    cpu_status = monitor.check_cpu_utilization()
    localhost_status = monitor.check_localhost_availability()
    internet_status = monitor.check_internet_availability()
    if not disk_status or not cpu_status:
        print("ERROR! Disk usage or CPU utilization exceeded thresholds.")
    elif localhost_status and internet_status:
        print("Everything is OK.")
    else:
        print("Network checks failed.")


if __name__ == '__main__':
    unittest.main()
