from datetime import datetime
from codigo_fonte.database import Database
from codigo_fonte.services import DonationService
import json

def main():
    # Configuração do banco de dados
    db = Database()

    # Definir as datas de início e fim do ano
    start_date = datetime(2025, 1, 1).date()  # 01/01/2025
    end_date = datetime(2025, 12, 31).date()  # 31/12/2025

    # Exemplo de uso
    service = DonationService(db)
    filters = {
        "start_date": start_date,
        "end_date": end_date,
        "payment_method": "credit-card",  # Exemplo de filtro
        "status": "approved",             # Exemplo de filtro
        "limit": 10,
        "offset": 0,
    }
    donations = service.get_filtered_donations(manager_id=1, filters=filters)

    # Exibe os dados no console
    print(json.dumps(donations, indent=2))

    # Salva os dados em um arquivo JSON
    with open("relatorio_doacoes.json", "w", encoding="utf-8") as json_file:
        json.dump(donations, json_file, indent=2, ensure_ascii=False)

    print(f"Relatório de doações de {start_date} até {end_date} salvo em 'relatorio_doacoes.json'.")

if __name__ == "__main__":
    main()