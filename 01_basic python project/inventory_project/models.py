from db import get_connection

def execute_query(query, values=None, fetch=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(query, values or ())

    if fetch:
        result = cursor.fetchall()
    else:
        conn.commit()
        result = None

    cursor.close()
    conn.close()

    return result