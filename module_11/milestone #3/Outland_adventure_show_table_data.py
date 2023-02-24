import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="titans28",
  database="outland_adventures"
)

# Define a function to display the data in a table
def show_table_data(table_name):
  cursor = db.cursor()
  cursor.execute(f"SELECT * FROM {table_name}")
  table_data = cursor.fetchall()
  print(f"\nTable '{table_name}':")
  for row in table_data:
    print(row)

# Call the show_table_data function for each table
show_table_data("employees")
show_table_data("customer")
show_table_data("guide")
show_table_data("equipment")
show_table_data("trip")
show_table_data("rental")
show_table_data("purchase")

#instance of cursor outside of function
cursor = db.cursor()
cursor.execute("SELECT* FROM equipment WHERE age >=5 ") #query for selcting to find equipment over 5 years old.
result = cursor.fetchall()

print()
print("The equipment that is over five years old is: ")
print(result)#prints the result of the query.

#query to select how much equipment has been purhchased.


input("Press Enter to Exit")
