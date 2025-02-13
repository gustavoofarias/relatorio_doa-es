from codigo_fonte.database import Database
from codigo_fonte.services import DonationService
import json

def mostrar_menu():
    print("\n--- Relatório de Doações ---")
    print("1. Buscar Doações")
    print("2. Sair")

def obter_filtros():
    """
    Permite que o usuário insira filtros personalizados.
    """
    filters = {}
    print("\n--- Filtros Personalizados ---")
    filters["start_date"] = input("Data inicial (YYYY-MM-DD, deixe em branco para ignorar): ") or None
    filters["end_date"] = input("Data final (YYYY-MM-DD, deixe em branco para ignorar): ") or None
    filters["payment_method"] = input("Método de pagamento (deixe em branco para ignorar): ") or None
    filters["status"] = input("Status (deixe em branco para ignorar): ") or None
    filters["search_text"] = input("Busca livre (nome, e-mail ou igreja, deixe em branco para ignorar): ") or None
    filters["limit"] = int(input("Número máximo de registros por página: "))
    filters["offset"] = int(input("Número de registros a ignorar (offset): "))
    return filters

def main():
    # Configuração do banco de dados
    db = Database()
    service = DonationService(db)

    while True:
        mostrar_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "2":
            print("Saindo...")
            break

        elif escolha == "1":
            manager_id = int(input("Digite o ID do manager: "))
            filters = obter_filtros()

            # Buscar doações
            resultado = service.get_filtered_donations(manager_id, filters)

            # Exibir resultados
            print("\n--- Resultados ---")
            print(json.dumps(resultado, indent=2))

            # Salvar resultados em um arquivo JSON
            salvar = input("\nDeseja salvar os resultados em um arquivo JSON? (s/n): ").lower()
            if salvar == "s":
                nome_arquivo = input("Digite o nome do arquivo (ex.: relatorio.json): ")
                with open(nome_arquivo, "w", encoding="utf-8") as json_file:
                    json.dump(resultado, json_file, indent=2, ensure_ascii=False)
                print(f"Relatório salvo em '{nome_arquivo}'.")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()