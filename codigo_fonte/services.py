from .repository import DonationRepository

class DonationService:
    def __init__(self, db):
        self.repository = DonationRepository(db)

    def get_filtered_donations(self, manager_id, filters):
        """
        Retorna as doações filtradas e paginadas.

        :param manager_id: ID do manager.
        :param filters: Dicionário com os filtros (start_date, end_date, payment_method, status, search_text, limit, offset).
        :return: Lista de doações no formato JSON.
        """
        donations = self.repository.get_donations(
            manager_id=manager_id,
            start_date=filters.get("start_date"),
            end_date=filters.get("end_date"),
            payment_method=filters.get("payment_method"),
            status=filters.get("status"),
            search_text=filters.get("search_text"),
            limit=filters.get("limit", 10),
            offset=filters.get("offset", 0),
        )
        return donations