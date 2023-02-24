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

    # Get the column headers
    headers = [desc[0] for desc in cursor.description]

    # Get the maximum width of each column
    max_widths = [len(header) for header in headers]
    for row in table_data:
        for i, cell in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(cell)))

    # Print the headers
    header_str = " | ".join(header.center(max_widths[i]) for i, header in enumerate(headers))
    print(header_str)

    # Print the separator row
    separator_str = "-+-".join("-" * width for width in max_widths)
    print(separator_str)

    # Print the data rows
    for row in table_data:
        row_str = " | ".join(str(cell).center(max_widths[i]) for i, cell in enumerate(row))
        print(row_str)

# Call the show_table_data function for each table
show_table_data("employees")
print()
show_table_data("customer")
print()
show_table_data("guide")
print()
show_table_data("equipment")
print()
show_table_data("trip")
print()
show_table_data("rental")
print()
show_table_data("purchase")

#instance of cursor outside of function
cursor = db.cursor()
cursor.execute("SELECT* FROM equipment WHERE age >=5 ") #query for selcting to find equipment over 5 years old.
result = cursor.fetchall()

print()
print()
print("The equipment that is over five years old is: ")
headers = [desc[0] for desc in cursor.description]
max_widths = [len(header) for header in headers]
for row in result:
    for i, cell in enumerate(row):
        max_widths[i] = max(max_widths[i], len(str(cell)))
header_str = " | ".join(header.center(max_widths[i]) for i, header in enumerate(headers))
separator_str = "-+-".join("-" * width for width in max_widths)
print(header_str)
print(separator_str)
for row in result:
    row_str = " | ".join(str(cell).center(max_widths[i]) for i, cell in enumerate(row))
    print(row_str)

# Query to select how many trips were taken to each location.
cursor.execute("SELECT trip_id, SUM(total_completed_trips) AS total_completed_trips FROM completed_trips GROUP BY trip_id")
result = cursor.fetchall()

print()
print()
print("Total completed trips per trip id: ")
headers = [desc[0] for desc in cursor.description]
max_widths = [len(header) for header in headers]
for row in result:
    for i, cell in enumerate(row):
        max_widths[i] = max(max_widths[i], len(str(cell)))
header_str = " | ".join(header.center(max_widths[i]) for i, header in enumerate(headers))
separator_str = "-+-".join("-" * width for width in max_widths)
print(header_str)
print(separator_str)
for row in result:
    row_str = " | ".join(str(cell).center(max_widths[i]) for i, cell in enumerate(row))
    print(row_str)
# Query to select the top 3 trip names and locations with the sums from trips in order from least to greatest.
cursor.execute("SELECT trip_name, location, SUM(total_completed_trips) AS total_completed_trips FROM trip t JOIN "
               "completed_trips ct ON t.trip_id = ct.trip_id GROUP BY t.trip_id ORDER BY total_completed_trips LIMIT 3")
result = cursor.fetchall()


# Get the column headers
headers = [desc[0] for desc in cursor.description]

# Get the maximum width of each column
max_widths = [len(header) for header in headers]
for row in result:
    for i, cell in enumerate(row):
        max_widths[i] = max(max_widths[i], len(str(cell)))
print()
print()
# Print the headers
header_str = " | ".join(header.center(max_widths[i]) for i, header in enumerate(headers))
print(header_str)

# Print the separator row
separator_str = "-+-".join("-" * width for width in max_widths)
print(separator_str)

# Print the data rows
for row in result:
    row_str = " | ".join(str(cell).center(max_widths[i]) for i, cell in enumerate(row))
    print(row_str)
print()
print()

#Query to select the equipment name, purchase date equipment was bought by customer, price, and the quantity.
cursor.execute("SELECT e.equipment_name, p.purchase_date, p.price, p.quantity FROM equipment e  "
               "INNER JOIN purchase p ON e.equipment_id = p.equipment_id")
result = cursor.fetchall() #fetches all the data from the query and stores it in result.

# Get the column headers
headers = [desc[0] for desc in cursor.description]

# Get the maximum width of each column
max_widths = [len(header) for header in headers]
for row in result:
    for i, cell in enumerate(row):
        max_widths[i] = max(max_widths[i], len(str(cell)))
print()
print()
# Print the headers
header_str = " | ".join(header.center(max_widths[i]) for i, header in enumerate(headers))
print(header_str)

# Print the separator row
separator_str = "-+-".join("-" * width for width in max_widths)
print(separator_str)

# Print the data rows
for row in result:
    row_str = " | ".join(str(cell).center(max_widths[i]) for i, cell in enumerate(row))
    print(row_str)
print()
print()

input("Enter to exit")
db.close() #closes the database.