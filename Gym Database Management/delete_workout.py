from connect_mysql import connect_database

def delete_workout_session(session_id):
    query = "DELETE FROM WorkoutSessions WHERE Session_id = %s"
    cursor.execute(query, (session_id, ))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add a workout to WorkoutSessions database
        delete_workout_session(1)

        conn.commit()
        print("Workout session has been deleted from the database.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")