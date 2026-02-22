import unittest
from quantum_log import QuantumLog  # Assuming 'quantum_log' is the module name where the QuantumLog class is defined


class TestQuantumLog(unittest.TestCase):

    def setUp(self):
        self.log = QuantumLog()

    def test_initialize_log(self):
        self.assertIsNotNone(self.log)

    def test_add_entry(self):
        entry = "Test Entry"
        self.log.add_entry(entry)
        self.assertIn(entry, self.log.get_entries())

    def test_get_entries(self):
        self.log.add_entry("First Entry")
        self.log.add_entry("Second Entry")
        entries = self.log.get_entries()
        self.assertEqual(len(entries), 2)
        self.assertIn("First Entry", entries)
        self.assertIn("Second Entry", entries)

    def test_add_invalid_entry(self):
        with self.assertRaises(ValueError):  # Assuming a ValueError is raised for invalid entries
            self.log.add_entry(12345)  # Attempting to add a non-string entry

    def test_clear_log(self):
        self.log.add_entry("Clear Me")
        self.log.clear()
        self.assertEqual(len(self.log.get_entries()), 0)

    def test_performance(self):
        import time
        start_time = time.time()
        for i in range(1000):
            self.log.add_entry(f"Entry {i}")
        duration = time.time() - start_time
        self.assertLess(duration, 1)  # Ensure the entries can be added in under 1 second


if __name__ == '__main__':
    unittest.main()