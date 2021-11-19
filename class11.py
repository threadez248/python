import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Test123",
    database = "employees"
)

cursor = db.cursor()
# cursor.execute("SHOW DATABASES")

####Showing databases

# databases = cursor.fetchall()

# for database in databases:
#     print(database)

# ###Create a DB 
# cursor.execute("create DATABASE ItMunk")

# for database in databases:
#     print(database)
# ## defining the Query
query = "select  distinct  emp_no, salary from salaries where salary > 150000;"

# ## getting records from the table
cursor.execute(query)

# ## fetching all records from the 'cursor' object
records = cursor.fetchall()
print(type(records))

# ## Showing the data
for record in records:
    print(record)