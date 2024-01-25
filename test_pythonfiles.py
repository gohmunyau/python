import unittest
from unittest.mock import patch
from pythonfile.py import SystemMonitor

class PythonFile(unittest.TestCase):
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_disk_usage())

if __name__ == '__main__':
    unittest.main()
