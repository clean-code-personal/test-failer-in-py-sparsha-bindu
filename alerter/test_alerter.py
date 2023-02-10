import unittest
from alerter import *

class TestAlertModule(unittest.TestCase):
    def test_alert_in_celcius(self):
        alert_failure_count = alert_in_celcius(400, network_alert_stub)
        alert_failure_count = alert_in_celcius(303.6,network_alert_stub)

        self.assertEqual(alert_failure_count, 2)

if __name__ == '__main__':
    unittest.main()
