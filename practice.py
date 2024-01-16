import mysql.connector
from mysql.connector import IntegrityError
import streamlit as st
import pandas as pd
def connect_to_database():
    return mysql.connector.connect(
        host="34.132.247.25",  # Replace with your database host
        user="root",  # Replace with your database username
        passwd="CaltransDatabase#1",  # Replace with your database password
        database="FiberOptic"
    )

def view_students():
    db = connect_to_database()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    # Convert to a pandas DataFrame for better visualization
    df = pd.DataFrame(data, columns=columns)

    cursor.close()
    db.close()

    # Display the DataFrame in Streamlit
    st.dataframe(df)

def add_student(student_id, name, major):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "INSERT INTO student (student_id, name, major) VALUES (%s, %s, %s)"
        values = (student_id, name, major)
        
        cursor.execute(query, values)
        db.commit()

        st.success("Student added successfully.")

    except IntegrityError:
        st.error("Student ID already exists. Please use a different ID.")

    finally:
        cursor.close()
        db.close()
    
def student_id_exists(student_id):
    db = connect_to_database()
    cursor = db.cursor()
    query = "SELECT EXISTS(SELECT 1 FROM student WHERE student_id = %s)"
    cursor.execute(query, (student_id,))
    exists = cursor.fetchone()[0]
    cursor.close()
    db.close()
    return exists

def main():
    st.title("Fiber Optic Database")
    st.subheader("Enter data")

    student_id = st.number_input("Enter student ID: ", key="id1")
    name = st.text_input("Enter name: ", key="name2")
    major = st.text_input("Enter major: ", key="major1")
    
    if st.button("Add Student"):
        if student_id_exists(student_id):
            st.error("Student ID already exists.")
        else:
            add_student(student_id, name, major)
            st.success("Student added successfully.")

    if st.button("View Database"):
        view_students()


if __name__ == "__main__":
    main()
