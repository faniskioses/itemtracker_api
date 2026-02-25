from database import get_connection

def add_item(name: str, quantity: int, category: str):
    """
    Add a new item to the database.
    Returns a dict with confirmation message.
    """
    db = get_connection()
    cursor = db.cursor()

    sql = "INSERT INTO items (name, quantity, category) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, quantity, category))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Item added successfully"}


def list_items():
    """
    Retrieve all items from the database.
    Returns a list of dicts representing each item.
    """
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT id, name, quantity, category FROM items")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return rows


def delete_item(item_id: int):
    """
    Delete an item by ID.
    Returns a confirmation dict if successful,
    or a dict with an 'error' key if item does not exist.
    """
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    # Check if the item exists
    cursor.execute("SELECT id FROM items WHERE id = %s", (item_id,))
    item = cursor.fetchone()
    if not item:
        cursor.close()
        db.close()
        return {"error": "Item not found"}

    # Delete the item
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Item deleted successfully"}