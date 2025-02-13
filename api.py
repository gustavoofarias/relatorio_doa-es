from flask import Flask, request, jsonify
from codigo_fonte.services import DonationService
from codigo_fonte.database import Database

# Configuração do Flask
app = Flask(__name__)

# Configuração do banco de dados e serviço
db = Database()
service = DonationService(db)

@app.route("/donations", methods=["GET"])
def get_donations():
    """
    Rota para buscar doações com filtros e paginação.
    """
    # Obter parâmetros da URL
    manager_id = request.args.get("manager_id", type=int)
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    payment_method = request.args.get("payment_method")
    status = request.args.get("status")
    search_text = request.args.get("search_text")
    limit = request.args.get("limit", default=10, type=int)
    offset = request.args.get("offset", default=0, type=int)

    # Aplicar filtros
    filters = {
        "start_date": start_date,
        "end_date": end_date,
        "payment_method": payment_method,
        "status": status,
        "search_text": search_text,
        "limit": limit,
        "offset": offset,
    }

    # Buscar doações
    donations = service.get_filtered_donations(manager_id, filters)
    return jsonify(donations)

if __name__ == "__main__":
    # Executar o servidor Flask
    app.run(debug=True)