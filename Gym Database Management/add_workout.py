from connect_mysql import connect_database

# function to add workout session to WorkoutSessions
def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    query = "INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (member_id, session_date, duration_minutes, calories_burned))

# Establishing connection
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        # Add a workout to WorkoutSessions database
        add_workout_session(1, "2024-12-21", 35, 120)

        conn.commit()
        print("Workout has been added to the database.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")