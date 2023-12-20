import sqlite3

# Create a database connection
conn = sqlite3.connect('students.db')

# Create a cursor object
cursor = conn.cursor()

# Create the student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    family TEXT,
    age INTEGER
)
''')

# Insert a student into the table
def create_student( name, family, age):
    cursor.execute('''
    INSERT INTO student ( name, family, age) VALUES (?, ?, ?)
    ''', ( name, family, age))
    conn.commit()

# Read a student from the table
def read_student(name):
    cursor.execute('''
    SELECT * FROM student WHERE name = ?
    ''', (name,))
    return cursor.fetchone()

# Update a student in the table
def update_student(id, name, family, age):
    cursor.execute('''
    UPDATE student SET name = ?, family = ?, age = ? WHERE id = ?
    ''', (name, family, age, id))
    conn.commit()

# Delete a student from the table
def delete_student(id):
    cursor.execute('''
    DELETE FROM student WHERE id = ?
    ''', (id,))
    conn.commit()