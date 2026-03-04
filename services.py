from database import get_connection

def add_item(name: str, quantity: int, category: str):
    """
    Add a new item to the database.
    Returns a dict with confirmation message.
    """
    with get_connection() as db:
        with db.cursor() as cursor:
            sql = "INSERT INTO items (name, quantity, category) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, quantity, category))
            db.commit()

    return {"message": "Item added successfully"}


def list_items():
    """
    Retrieve all items from the database.
    Returns a list of dicts representing each item.
    """
    with get_connection() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, name, quantity, category FROM items")
            rows = cursor.fetchall()
    return rows


def delete_item(item_id: int):
    """
    Delete an item by ID.
    Returns a confirmation dict if successful,
    or a dict with an 'error' key if item does not exist.
    """
    with get_connection() as db:
     with db.cursor() as cursor:
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        db.commit()
        if cursor.rowcount == 0:
            # No row deleted, item not found
            raise ValueError("Item not found")
        return {"message": "Item deleted successfully"}
