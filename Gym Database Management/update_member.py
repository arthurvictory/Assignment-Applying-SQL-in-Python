# call module from connect mysql to connect to database
from connect_mysql import connect_database

# function to update member age
def update_member_age(member_id, age):
    query = "UPDATE Members SET age = %s WHERE id = %s"
    cursor.execute(query, (age, member_id))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # calling function to update member age
        update_member_age(1, 40)

        conn.commit()
        print("Age has been updated to the database.")
    
    except Exception as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")