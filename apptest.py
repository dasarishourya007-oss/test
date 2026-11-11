import unittest

class TestApp(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(10 + 20, 30)

if _name_ == "_main_":
    unittest.main()