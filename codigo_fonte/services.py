from .repository import DonationRepository

class DonationService:
    def __init__(self, db):
        self.repository = DonationRepository(db)

    def get_filtered_donations(self, manager_id, filters):
        """
        Retorna as doações filtradas e paginadas no formato desejado.
        """
        # Buscar doações
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

        # Calcular o total de doações
        total = self.repository.get_total_donations(
            manager_id=manager_id,
            start_date=filters.get("start_date"),
            end_date=filters.get("end_date"),
            payment_method=filters.get("payment_method"),
            status=filters.get("status"),
            search_text=filters.get("search_text"),
        )

        # Calcular a página atual
        page = (filters.get("offset", 0) // filters.get("limit", 10)) + 1

        # Retornar no formato desejado
        return {
            "total": total,
            "page": page,
            "limit": filters.get("limit", 10),
            "donations": donations,
        }