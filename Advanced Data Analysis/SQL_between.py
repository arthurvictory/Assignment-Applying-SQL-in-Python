from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))

    # Fetch all results from the query
    results = cursor.fetchall() 
    for row in results: 
        print(row)

# Establishing connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add a member to Members database
        get_members_in_age_range(25, 30)

        print("Member between the ages of 25 and 30 have been fetched.")

    except Exception as e:
        print(f"Error: {e}")    
    
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")