import unittest
from codigo_fonte.database import Database
from codigo_fonte.services import DonationService

class TestDonationService(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para os testes."""
        self.db = Database()
        self.service = DonationService(self.db)

    def test_get_filtered_donations(self):
        """Testa a busca de doações filtradas e paginadas."""
        filters = {
            "start_date": "2023-01-01",
            "end_date": "2023-12-31",
            "payment_method": "credit-card",
            "status": "approved",
            "search_text": "João",
            "limit": 5,
            "offset": 0,
        }
        resultado = self.service.get_filtered_donations(manager_id=1, filters=filters)
        self.assertIsInstance(resultado, dict)
        self.assertIn("total", resultado)
        self.assertIn("page", resultado)
        self.assertIn("limit", resultado)
        self.assertIn("donations", resultado)
        self.assertIsInstance(resultado["donations"], list)

if __name__ == "__main__":
    unittest.main()