from connect_mysql import connect_database

# function to add member to Members database
def add_member(id, name, age):
    query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (id, name, age))

# Establishing connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add a member to Members database
        add_member(3, "Bob Doe", 28)

        conn.commit()
        print("Member has been added to the database.")

    except Exception as e:
        print(f"Error: {e}")    
    
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")