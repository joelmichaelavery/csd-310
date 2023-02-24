import mysql.connector
from mysql.connector import errorcode

# define the configuration details for the MySQL connection
config = {
  "user": "root",
  "password": "titans28",
  "host": "127.0.0.1",
  "database": "",
  "raise_on_warnings": True
}

try:
    # create a connection to the MySQL database using the configuration details
    db = mysql.connector.connect(**config)

    # print out a message confirming that the connection was successful
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    # wait for user input before continuing with the program
    input("\n\nPress any key to continue... ")

    # create a cursor object to execute SQL commands
    cursor = db.cursor()

    # create the "outland_adventures" database
    cursor.execute("CREATE DATABASE outland_adventures")

    #  connect to the "outland_adventures" database
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="titans28",
    database="outland_adventures"
  )
    cursor = db.cursor()
    # create the "employees" table
    cursor.execute("CREATE TABLE employees (employee_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255),last_name VARCHAR(255), job_title VARCHAR(255), hire_date DATE)")

    # create the "customer" table
    cursor.execute("CREATE TABLE customer (customer_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")

    # create the "guide" table
    cursor.execute("CREATE TABLE guide (guide_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), phone VARCHAR(255), email VARCHAR(255))")

    # create the "equipment" table
    cursor.execute("CREATE TABLE equipment (equipment_id INT AUTO_INCREMENT PRIMARY KEY, equipment_name VARCHAR(255), description VARCHAR(255), purchase_date DATE, purchase_price DECIMAL(10, 2), rental_price DECIMAL(10, 2), quantity INT, age INT, guide_id INT, FOREIGN KEY (guide_id) REFERENCES guide(guide_id))")

    # create the "trip" table
    cursor.execute("CREATE TABLE trip (trip_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, trip_name VARCHAR(255), location VARCHAR(255), purchase_date DATE, start_date DATE, end_date DATE, guide_id INT, FOREIGN KEY (customer_id) REFERENCES customer(customer_id), FOREIGN KEY (guide_id) REFERENCES guide(guide_id))")

    # create the "rental" table
    cursor.execute("CREATE TABLE rental (rental_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, trip_id INT, equipment_id INT, rental_date DATE, return_date DATE, FOREIGN KEY (customer_id) REFERENCES customer(customer_id), FOREIGN KEY (trip_id) REFERENCES trip(trip_id), FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id))")

    # create the "purchase" table
    cursor.execute("CREATE TABLE purchase (purchase_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, equipment_id INT, purchase_date DATE, price DECIMAL(10, 2), quantity INT, FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id))")

    # Create "completed_trips" table
    cursor.execute("CREATE TABLE completed_trips (trip_id INT, end_date DATE, total_completed_trips INT, PRIMARY KEY (trip_id, end_date), FOREIGN KEY (trip_id) REFERENCES trip(trip_id))")


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
    ins = "INSERT INTO trip (trip_name, location, purchase_date,  start_date, end_date, customer_id, guide_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    trip_data = [
        ('Kilimanjaro', 'Africa', '2023-1-1', '2023-06-15', '2023-06-30', 2, 1),
        ('Everest Base Camp', 'Asia', '2022-3-15', '2023-09-01', '2023-09-15', 3, 1),
        ('Alps Village', 'Southern Europe', '2022-8-10', '2023-11-01', '2023-11-10', 5, 2),
        ('Annapurna Circuit', 'Asia', '2021-5-18', '2024-03-01', '2024-03-15', 4, 2),
        ('Balkans Via Dinarica', 'Southern Europe', '2023-2-01', '2024-05-01', '2024-05-10', 8, 1),
        ('Italy Tuscany Tour', 'Southern Europe', '2022-12-20', '2024-09-01', '2024-09-15', 3, 1),
        ('Mount Kilimanjaro', 'Africa', '2021-6-7', '2025-01-01', '2025-01-10', 6, 2),
        ('Slovenia Julian Alps', 'Southern Europe', '2022-11-18', '2025-04-01', '2025-04-15', 9, 2),
        ('Annapurna Base Camp', 'Asia', '2022-11-10', '2025-10-01', '2025-10-15', 7, 1),
        ('Greece Trek', 'Southern Europe', '2023-02-12', '2026-02-01', '2026-02-10', 1, 1)
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

    ins = "INSERT INTO completed_trips (trip_id, end_date, total_completed_trips) VALUES (%s, %s, %s)"
    completed_trips_data = [
        (8, '2017-02-10',  15),
        (2, '2017-02-23',  4),
        (2, '2017-03-21',  9),
        (3, '2017-04-11',  9),
        (9, '2017-04-22',  11),
        (6, '2017-05-14',  6),
        (1, '2017-05-27',  11),
        (7, '2017-06-13',  14),
        (5, '2017-06-26',  4),
        (6, '2017-07-22',  9),
        (1, '2017-08-05',  13),
        (7, '2017-08-17',  5),
        (3, '2017-09-10',  9),
        (9, '2017-10-01',  7),
        (1, '2017-10-27',  5),
        (6, '2017-11-17',  14),
        (7, '2017-12-03',  2),
        (9, '2017-12-16',  3),
        (4, '2017-12-30',  8),
        (2, '2018-01-13',  3),
        (3, '2018-01-23',  5),
        (6, '2018-02-06',  8),
        (10, '2018-02-28',  5),
        (1, '2018-03-24',  10),
        (9, '2018-04-05',  13),
        (6, '2018-04-24',  4),
        (5, '2018-05-13',  8),
        (6, '2018-05-30',  9),
        (5, '2018-06-16',  10),
        (4, '2018-07-05',  4),
        (4, '2018-07-26',  10),
        (3, '2018-08-15',  13),
        (10, '2018-09-12',  15),
        (8, '2018-09-23',  9),
        (2, '2018-10-19',  15),
        (5, '2018-11-04',  14),
        (4, '2018-11-26',  11),
        (8, '2018-12-20',  2),
        (8, '2018-12-30',  5),
        (3, '2019-01-15',  10),
        (3, '2019-01-31',  8),
        (6, '2019-02-18',  4),
        (1, '2019-03-05',  8),
        (7, '2019-03-29',  8),
        (5, '2019-04-24',  8),
        (6, '2019-05-06',  12),
        (4, '2019-05-30',  5),
        (6, '2019-06-12',  3),
        (7, '2019-06-27',  5),
        (1, '2019-07-09',  6),
        (1, '2019-07-25',  5),
        (7, '2019-08-13',  4),
        (10, '2019-08-28',  14),
        (10, '2019-09-17',  9),
        (4, '2019-10-03',  2),
        (9, '2019-10-24',  14),
        (6, '2019-11-11',  12),
        (4, '2019-12-03',  10),
        (5, '2019-12-20',  14),
        (1, '2020-01-10',  6),
        (2, '2020-01-26',  13),
        (10, '2020-02-07',  15),
        (10, '2020-02-18',  10),
        (10, '2020-03-04',  15),
        (3, '2020-03-19',  8),
        (10, '2020-04-07',  12),
        (7, '2020-04-18',  11),
        (1, '2020-05-01',  14),
        (1, '2020-05-29',  14),
        (4, '2020-06-18',  12),
        (3, '2020-07-05',  10),
        (5, '2020-07-19',  5),
        (8, '2020-08-11',  12),
        (5, '2020-08-28',  2),
        (3, '2020-09-14',  9),
        (8, '2020-10-02',  9),
        (7, '2020-10-21',  2),
        (2, '2020-11-07',  10),
        (6, '2020-11-27',  10),
        (9, '2020-12-14',  4),
        (6, '2020-12-31',  7),
        (7, '2021-01-16',  15),
        (2, '2021-02-05',  5),
        (6, '2021-02-22',  3),
        (7, '2021-03-14',  13),
        (1, '2021-03-28',  11),
        (2, '2021-04-24',  9),
        (1, '2021-05-16',  13),
        (10, '2021-05-29',  14),
        (6, '2021-06-11',  8),
        (6, '2021-06-27',  13),
        (1, '2021-07-10',  5),
        (2, '2021-08-01',  11),
        (9, '2021-08-16',  14),
        (5, '2021-09-06',  12),
        (4, '2021-09-25',  10),
        (1, '2021-10-05',  12),
        (7, '2021-10-30',  13),
        (4, '2021-11-18',  7),
        (8, '2021-12-12',  4),
        (7, '2022-01-08',  10),
        (2, '2022-01-21',  9),
        (5, '2022-02-10',  14),
        (3, '2022-03-01',  7),
        (4, '2022-03-12',  12),
        (9, '2022-03-23',  7),
        (3, '2022-04-17',  13),
        (7, '2022-05-03',  2),
        (5, '2022-05-19',  6),
        (4, '2022-06-07',  7),
        (9, '2022-06-19',  13),
        (5, '2022-07-02',  15),
        (2, '2022-07-15',  2),
        (3, '2022-07-31',  2),
        (4, '2022-08-27',  14),
        (9, '2022-09-10',  6),
        (2, '2022-09-27',  15),
        (1, '2022-10-13',  7),
        (1, '2022-11-09',  14),
        (9, '2022-11-21',  6),
        (7, '2022-12-06',  4),
        (2, '2022-12-24',  5),
        (7, '2022-12-31',  9)
        ]
    cursor.executemany(ins, completed_trips_data)
    db.commit()
    
    # print a message to indicate that the tables were created successfully
    print("Tables created successfully")
    
    # close the database connection
    cursor.close()
    db.close()

# handle any MySQL errors that occur during program execution
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
