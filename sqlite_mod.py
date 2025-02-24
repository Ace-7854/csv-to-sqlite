import sqlite3

con = sqlite3.Connection("new_database.db")

def create_table():
    cur = con.cursor("""CREATE TABLE "Employees" ("UID"	INTEGER UNIQUE,	"Name"	TEXT NOT NULL,
                 	"Salary" REAL NOT NULL,	
                 PRIMARY KEY("UID" AUTOINCREMENT));""") #sets schema for a table

def ins_new_rec(name, salary):
    query = "INSERT INTO Employees (Name, Salary) VALUES (?, ?);" # use placeholders for parameterized query
    con.execute(query, (name, salary)) # pass the values as a tuple
    con.commit()

def get_uid(name):
    query = f"SELECT UID FROM Employees WHERE Name={name};"
    rec = con.execute(query)
    rec.fetchall()

def ins_new_record(data, destination, email, name, number_of_people,phone,tripid):
    query = "INSERT INTO booking (data, Destination, Email, Name,Phone ,NumberPeople, TripID) VALUES (?,?,?,?,?,?,?)"
    con.execute(query,(data, destination, email, name, phone, number_of_people, tripid))
    con.commit()
