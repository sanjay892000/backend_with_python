from models import execute_query

def add_product(name, quantity, price):
    query = """
    INSERT INTO products (name, quantity, price)
    VALUES (%s, %s, %s)
    """
    execute_query(query, (name, quantity, price))


def get_products():
    return execute_query("SELECT * FROM products", fetch=True)


def update_stock(product_id, quantity):
    query = "UPDATE products SET quantity=%s WHERE id=%s"
    execute_query(query, (quantity, product_id))


def delete_product(product_id):
    query = "DELETE FROM products WHERE id=%s"
    execute_query(query, (product_id,))


def low_stock(threshold=5):
    query = "SELECT * FROM products WHERE quantity < %s"
    return execute_query(query, (threshold,), fetch=True)