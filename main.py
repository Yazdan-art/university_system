from model import Student
from database import create_student, read_student, update_student, delete_student



# # Insert students into the table
create_student("yazdan", "Doe", 20)

# Read a student
student = read_student("yazdan")
print(student)

# # Update a student
# update_student(1, "John", "Smith", 21)



# # Delete a student
# delete_student(1)



# # Close the connection to the database
# # conn.close()