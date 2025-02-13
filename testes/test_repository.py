import unittest
from codigo_fonte.database import Database
from codigo_fonte.repository import DonationRepository

class TestDonationRepository(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para os testes."""
        self.db = Database()
        self.repository = DonationRepository(self.db)

    def test_get_total_donations(self):
        """Testa a contagem total de doações."""
        total = self.repository.get_total_donations(manager_id=1)
        self.assertIsInstance(total, int)
        self.assertGreaterEqual(total, 0)

    def test_get_donations(self):
        """Testa a busca de doações com filtros básicos."""
        donations = self.repository.get_donations(manager_id=1, limit=5)
        self.assertIsInstance(donations, list)
        self.assertTrue(len(donations) <= 5)

    def test_get_donations_with_filters(self):
        """Testa a busca de doações com filtros personalizados."""
        donations = self.repository.get_donations(
            manager_id=1,
            start_date="2023-01-01",
            end_date="2023-12-31",
            payment_method="credit-card",
            status="approved",
            search_text="João",
            limit=10,
            offset=0
        )
        self.assertIsInstance(donations, list)
        for donation in donations:
            self.assertIn("id", donation)
            self.assertIn("createdAt", donation)
            self.assertIn("netAmountChurch", donation)
            self.assertIn("status", donation)
            self.assertIn("paymentMethod", donation)
            self.assertIn("church", donation)
            self.assertIn("user", donation)

if __name__ == "__main__":
    unittest.main()