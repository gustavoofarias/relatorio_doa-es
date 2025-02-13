import unittest
from codigo_fonte.database import Database
from codigo_fonte.repository import DonationRepository

class TestDonationRepository(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.repository = DonationRepository(self.db)

    def test_get_donations(self):
        donations = self.repository.get_donations(manager_id=1, limit=5)
        self.assertIsInstance(donations, list)
        self.assertTrue(len(donations) <= 5)

if __name__ == "__main__":
    unittest.main()