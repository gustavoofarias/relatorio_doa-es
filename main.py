from codigo_fonte.database import Database
from codigo_fonte.services import DynamicReportService
import json

def mostrar_menu_tabelas():
    print("\nEscolha a tabela para o relatório:")
    print("1. Doações (donations)")
    print("2. Igrejas (churches)")
    print("3. Saques (withdrawals)")
    print("4. Usuários (users)")
    print("5. Sair")

def obter_colunas(tabela):
    """
    Retorna as colunas disponíveis para a tabela escolhida.
    """
    if tabela == "donations":
        return ["id", "amount", "payment_method", "status", "created_at", "user_id", "church_id"]
    elif tabela == "churches":
        return ["id", "name", "cnpj", "manager_id", "created_at"]
    elif tabela == "withdrawals":
        return ["id", "amount", "status", "created_at", "manager_id"]
    elif tabela == "users":
        return ["id", "full_name", "email", "created_at"]
    else:
        return []

def obter_filtros():
    """
    Permite que o usuário insira filtros personalizados.
    """
    filters = {}
    print("\n--- Filtros Personalizados ---")
    while True:
        coluna = input("Digite o nome da coluna para filtrar (ou deixe em branco para parar): ")
        if not coluna:
            break
        valor = input(f"Digite o valor para filtrar na coluna '{coluna}': ")
        filters[coluna] = valor
    return filters

def main():
    # Configuração do banco de dados
    db = Database()

    while True:
        mostrar_menu_tabelas()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "5":
            print("Saindo...")
            break

        tabelas = ["donations", "churches", "withdrawals", "users"]
        if escolha in ["1", "2", "3", "4"]:
            tabela = tabelas[int(escolha) - 1]
            colunas = obter_colunas(tabela)

            print(f"\nColunas disponíveis para a tabela '{tabela}': {', '.join(colunas)}")
            colunas_selecionadas = input("Digite as colunas desejadas (separadas por vírgula): ").split(",")
            colunas_selecionadas = [col.strip() for col in colunas_selecionadas if col.strip() in colunas]

            filtros = obter_filtros()

            ordenacao = input("Digite a coluna para ordenação (ex.: 'created_at DESC'): ")
            limite = int(input("Digite o número máximo de registros por página: "))
            offset = int(input("Digite o número de registros a ignorar (offset): "))

            # Gerar o relatório
            service = DynamicReportService(db)
            relatorio = service.generate_dynamic_report(
                table=tabela,
                columns=colunas_selecionadas,
                filters=filtros,
                order_by=ordenacao,
                limit=limite,
                offset=offset
            )

            # Salvar o relatório em um arquivo JSON
            nome_arquivo = f"relatorio_{tabela}.json"
            with open(nome_arquivo, "w", encoding="utf-8") as json_file:
                json.dump(relatorio, json_file, indent=2, ensure_ascii=False)

            print(f"\nRelatório salvo em '{nome_arquivo}'.")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()