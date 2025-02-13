from .repository import DonationRepository, DynamicReportRepository

class DonationService:
    def __init__(self, db):
        self.repository = DonationRepository(db)

    def get_filtered_donations(self, manager_id, filters):
        """
        Retorna as doações filtradas e paginadas.
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


class DynamicReportService:
    def __init__(self, db):
        self.repository = DynamicReportRepository(db)

    def generate_dynamic_report(self, table, columns, filters, order_by, limit, offset):
        """
        Gera um relatório dinâmico com base nos parâmetros fornecidos.
        """
        return self.repository.execute_dynamic_query(table, columns, filters, order_by, limit, offset)