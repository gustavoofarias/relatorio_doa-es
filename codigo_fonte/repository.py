import psycopg2

class DonationRepository:
    def __init__(self, db):
        self.db = db

    def get_total_donations(self, manager_id, start_date=None, end_date=None, payment_method=None, status=None, search_text=None):
        """
        Retorna o total de doações com base nos filtros fornecidos.
        """
        query = """
        SELECT 
            COUNT(*)
        FROM 
            donations d
        JOIN 
            users u ON d.user_id = u.id
        JOIN 
            churches c ON d.church_id = c.id
        JOIN 
            managers m ON c.manager_id = m.id
        WHERE 
            c.manager_id = %(manager_id)s
            AND (d.created_at BETWEEN %(start_date)s AND %(end_date)s OR %(start_date)s IS NULL)
            AND (d.payment_method = %(payment_method)s OR %(payment_method)s IS NULL)
            AND (d.status = %(status)s OR %(status)s IS NULL)
            AND (
                u.full_name ILIKE %(search_text)s 
                OR u.email ILIKE %(search_text)s 
                OR c.name ILIKE %(search_text)s 
                OR %(search_text)s IS NULL
            );
        """

        params = {
            "manager_id": manager_id,
            "start_date": start_date,
            "end_date": end_date,
            "payment_method": payment_method,
            "status": status,
            "search_text": f"%{search_text}%" if search_text else None,
        }

        connection = self.db.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            total = cursor.fetchone()[0]
            return total
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            return 0
        finally:
            cursor.close()
            self.db.release_connection(connection)

    def get_donations(self, manager_id, start_date=None, end_date=None, payment_method=None, status=None, search_text=None, limit=10, offset=0):
        """
        Busca as doações com base nos filtros fornecidos.
        """
        query = """
        SELECT 
            d.id AS donation_id,
            d.amount,
            d.payment_method,
            d.status,
            d.created_at,
            u.id AS user_id,
            u.full_name AS user_name,
            u.email AS user_email,
            c.id AS church_id,
            c.name AS church_name,
            c.username AS church_username
        FROM 
            donations d
        JOIN 
            users u ON d.user_id = u.id
        JOIN 
            churches c ON d.church_id = c.id
        JOIN 
            managers m ON c.manager_id = m.id
        WHERE 
            c.manager_id = %(manager_id)s
            AND (d.created_at BETWEEN %(start_date)s AND %(end_date)s OR %(start_date)s IS NULL)
            AND (d.payment_method = %(payment_method)s OR %(payment_method)s IS NULL)
            AND (d.status = %(status)s OR %(status)s IS NULL)
            AND (
                u.full_name ILIKE %(search_text)s 
                OR u.email ILIKE %(search_text)s 
                OR c.name ILIKE %(search_text)s 
                OR %(search_text)s IS NULL
            )
        ORDER BY 
            d.created_at DESC
        LIMIT %(limit)s OFFSET %(offset)s;
        """

        params = {
            "manager_id": manager_id,
            "start_date": start_date,
            "end_date": end_date,
            "payment_method": payment_method,
            "status": status,
            "search_text": f"%{search_text}%" if search_text else None,
            "limit": limit,
            "offset": offset,
        }

        connection = self.db.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()

            # Formatar os resultados
            donations = []
            for row in results:
                donations.append({
                    "id": row[0],
                    "createdAt": row[4].isoformat() + "Z",  # Formato ISO 8601 com "Z"
                    "netAmountChurch": str(row[1]),  # Convertendo para string
                    "status": row[3],
                    "paymentMethod": row[2],
                    "church": {
                        "id": row[8],
                        "name": row[9],
                        "username": row[10],
                    },
                    "user": {
                        "id": row[5],
                        "name": row[6],
                        "email": row[7],
                    }
                })

            return donations
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            return []
        finally:
            cursor.close()
            self.db.release_connection(connection)