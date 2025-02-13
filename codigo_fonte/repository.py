import psycopg2

class DonationRepository:
    def __init__(self, db):
        self.db = db

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
            u.full_name AS user_name,
            u.email AS user_email,
            c.name AS church_name,
            m.name AS manager_name
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
                    "donation_id": row[0],
                    "amount": float(row[1]),
                    "payment_method": row[2],
                    "status": row[3],
                    "created_at": row[4].isoformat(),
                    "user_name": row[5],
                    "user_email": row[6],
                    "church_name": row[7],
                    "manager_name": row[8],
                })

            return donations
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            return []
        finally:
            cursor.close()
            self.db.release_connection(connection)


class DynamicReportRepository:
    def __init__(self, db):
        self.db = db

    def build_dynamic_query(self, table, columns, filters, order_by, limit, offset):
        """
        Constrói uma query SQL dinamicamente com base nos parâmetros fornecidos.
        """
        # Seleção das colunas
        selected_columns = ", ".join(columns)

        # Construção dos filtros
        filter_clauses = []
        params = {}
        for key, value in filters.items():
            if value is not None:
                filter_clauses.append(f"{key} = %({key})s")
                params[key] = value

        where_clause = " AND ".join(filter_clauses) if filter_clauses else "1=1"

        # Construção da query
        query = f"""
        SELECT 
            {selected_columns}
        FROM 
            {table}
        WHERE 
            {where_clause}
        ORDER BY 
            {order_by}
        LIMIT %(limit)s OFFSET %(offset)s;
        """

        # Adiciona limit e offset aos parâmetros
        params["limit"] = limit
        params["offset"] = offset

        return query, params

    def execute_dynamic_query(self, table, columns, filters, order_by, limit, offset):
        """
        Executa uma query dinâmica e retorna os resultados.
        """
        query, params = self.build_dynamic_query(table, columns, filters, order_by, limit, offset)

        connection = self.db.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            results = cursor.fetchall()

            # Formatar os resultados
            rows = []
            for row in results:
                row_dict = {}
                for i, column in enumerate(columns):
                    row_dict[column] = row[i]
                rows.append(row_dict)

            return rows
        except psycopg2.Error as e:
            print(f"Erro ao executar a query: {e}")
            return []
        finally:
            cursor.close()
            self.db.release_connection(connection)