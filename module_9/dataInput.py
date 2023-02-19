import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    user="root",
    password="titans28",
    host="localhost",
    database="outland_adventures",
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

# Insert data into employees table
ins = "INSERT INTO employees (first_name, last_name, job_title, hire_date) VALUES (%s, %s, %s, %s)"
employee_data = [
  ('Blythe', 'Timmerson', 'Co-Founder', '2010-01-01'),
  ('Jim', 'Ford', 'Co-Founder', '2010-01-01'),
  ('John', 'MacNell', 'Guide', '2011-06-01'),
  ('D.B.', 'Marland', 'Guide', '2012-01-01'),
  ('Anita', 'Gallegos', 'Marketing', '2015-07-01'),
  ('Dimitrios', 'Stravopolous', 'Equipment Mgmt', '2015-07-01'),
  ('Mei', 'Wong', 'Developer', '2019-02-01')
]
cursor.executemany(ins, employee_data)
db.commit()

# Insert data into customer table
ins = "INSERT INTO customer (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
customer_data = [
  ('John', 'Doe', 'johndoe@example.com', '555-555-1234'),
  ('Jane', 'Smith', 'janesmith@example.com', '555-555-5678'),
  ('Michael', 'Johnson', 'michaelj@example.com', '555-555-2468'),
  ('Sarah', 'Davis', 'sarahdavis@example.com', '555-555-7890'),
  ('William', 'Thompson', 'williamt@example.com', '555-555-1212'),
  ('Elizabeth', 'Rodriguez', 'elizabethr@example.com', '555-555-2323'),
  ('David', 'Garcia', 'davidgarcia@example.com', '555-555-3434'),
  ('Olivia', 'Wilson', 'oliviawilson@example.com', '555-555-4545'),
  ('James', 'Anderson', 'jamesanderson@example.com', '555-555-5656'),
  ('Emma', 'Thomas', 'emmathomas@example.com', '555-555-6767')
]
cursor.executemany(ins, customer_data)
db.commit()

# Insert data into guide table
ins = "INSERT INTO guide (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)"
guide_data = [
    ('John', 'McNell', '555-555-1212', 'johnmc@example.com'),
    ('D.B.', 'Marland', '555-555-2323', 'dbm@example.com')
]
cursor.executemany(ins, guide_data)
db.commit()

# Insert data into equipment table
ins = "INSERT INTO equipment (equipment_name, description, purchase_date, purchase_price, rental_price, quantity, age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
equipment_data = [
    ('Backpack', 'Large capacity', '2020-01-15', 100.00, 10.00, 20, 3),
    ('Tent', '2-person capacity', '2019-03-25', 150.00, 20.00, 10, 4),
    ('Sleeping bag', 'Cold weather rating -5', '2021-05-01', 75.00, 8.00, 30, 1),
    ('Stove', '2-burner', '2018-08-10', 200.00, 15.00, 15, 5),
    ('Water filter', 'Gravity-fed', '2022-02-01', 50.00, 5.00, 25, 0),
    ('Hiking boots', "Men's size 10", '2021-07-20', 120.00, 12.00, 20, 1),
    ('Trekking pole', 'Lightweight', '2019-11-30', 40.00, 4.00, 30, 2),
    ('Headlamp', 'Rechargeable', '2020-12-05', 25.00, 3.00, 50, 1),
    ('GPS device', 'Waterproof', '2018-04-10', 300.00, 20.00, 5, 4),
    ('Solar panel', '50W', '2022-01-10', 250.00, 25.00, 5, 0)
]
cursor.executemany(ins, equipment_data)
db.commit()

# Insert data into trip table
ins = "INSERT INTO trip (trip_name, location, start_date, end_date, guide_id) VALUES (%s, %s, %s, %s, %s)"
trip_data = [
    ('Kilimanjaro', 'Africa', '2023-06-15', '2023-06-30', 1),
    ('Everest Base Camp', 'Asia', '2023-09-01', '2023-09-15', 1),
    ('Machu Picchu', 'South America', '2023-11-01', '2023-11-10', 2),
    ('Annapurna Circuit', 'Asia', '2024-03-01', '2024-03-15', 2),
    ('Inca Trail to Machu Picchu', 'South America', '2024-05-01', '2024-05-10', 1),
    ('Patagonia Trek', 'South America', '2024-09-01', '2024-09-15', 1),
    ('Mount Kilimanjaro', 'Africa', '2025-01-01', '2025-01-10', 2),
    ('Torres del Paine Trek', 'South America', '2025-04-01', '2025-04-15', 2),
    ('Annapurna Base Camp', 'Asia', '2025-10-01', '2025-10-15', 1),
    ('Choquequirao Trek', 'South America', '2026-02-01', '2026-02-10', 1)
]
cursor.executemany(ins, trip_data)
db.commit()

# Insert data rental table
ins = "INSERT INTO rental (customer_id, trip_id, equipment_id, rental_date, return_date) VALUES(%s, %s, %s, %s, %s)"
rental_data = [
    (2, 1, 3, '2022-06-01', '2022-06-15'),
    (3, 2, 2, '2022-08-05', '2022-08-10'),
    (4, 1, 4, '2022-07-10', '2022-07-20'),
    (2, 3, 6, '2022-09-01', '2022-09-15'),
    (6, 3, 7, '2022-09-25', '2022-10-02'),
    (7, 2, 9, '2022-10-10', '2022-10-17'),
    (10, 3, 10, '2022-10-20', '2022-11-05'),
    (9, 1, 1, '2022-11-01', '2022-11-15'),
    (3, 1, 5, '2022-11-10', '2022-11-15'),
    (1, 2, 8, '2022-12-01', '2022-12-10')
]
cursor.executemany(ins, rental_data)
db.commit()

# Insert data into purchase table
ins = "INSERT INTO purchase (customer_id, equipment_id, purchase_date, price, quantity) VALUES (%s, %s, %s, %s, %s)"
purchase_data = [
    (2, 3, '2022-02-15', 200, 1),
    (3, 2, '2022-04-20', 100, 2),
    (4, 4, '2022-05-10', 150, 1),
    (5, 5, '2022-06-25', 250, 2),
    (7, 8, '2022-07-15', 300, 1),
    (8, 7, '2022-08-20', 175, 3),
    (6, 6, '2022-09-05', 225, 1),
    (9, 1, '2022-10-01', 150, 2),
    (10, 9, '2022-11-10', 200, 1),
    (1, 10, '2022-12-10', 250, 1)
]
cursor.executemany(ins, purchase_data)
db.commit()

# Display data from employees table
cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
print("Employees table:")
for row in result:
    print(row)

# Display data from customer table
cursor.execute("SELECT * FROM customer")
result = cursor.fetchall()
print("Customer table:")
for row in result:
    print(row)

# Display data from guide table
cursor.execute("SELECT * FROM guide")
result = cursor.fetchall()
print("Guide table:")
for row in result:
    print(row)

# Display data from equipment table
cursor.execute("SELECT * FROM equipment")
result = cursor.fetchall()
print("Equipment table:")
for row in result:
    print(row)

# Display data from trip table
cursor.execute("SELECT * FROM trip")
result = cursor.fetchall()
print("Trip table:")
for row in result:
    print(row)

# Display data from rental table
cursor.execute("SELECT * FROM rental")
result = cursor.fetchall()
print("Rental table:")
for row in result:
    print(row)

# Display data from purchase table
cursor.execute("SELECT * FROM purchase")
result = cursor.fetchall()
print("Purchase table:")
for row in result:
    print(row)

