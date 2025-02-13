import unittest
from codigo_fonte.database import Database
from codigo_fonte.services import DonationService

class TestDonationService(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.service = DonationService(self.db)

    def test_get_filtered_donations(self):
        filters = {
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "limit": 5,
        }
        donations = self.service.get_filtered_donations(manager_id=1, filters=filters)
        self.assertIsInstance(donations, list)
        self.assertTrue(len(donations) <= 5)

if __name__ == "__main__":
    unittest.main()