import sqlite3

##connect to sqlite
connection=sqlite3.connect("student.db")

##create cursor object to insert record,create,tabel etc
cursor = connection.cursor()

#create the table
table ="""CREATE TABLE STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25),MARKS INT);"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Samay', 'Data Science', 'A',98)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Jeet', 'Data Science', 'B',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Manav', 'Devops', 'C',89)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Rishabh', 'Data Science', 'C',78)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Aayush', 'Software Devloper', 'C',88)''') 

##display all the records
print("the inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)
    
#close the connection
connection.commit()
connection.close()
