import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "root",
	"password": "titans28",
	"host": "127.0.0.1",
	"database": "",
	"raise_on_warnings": True
}

try:
  db = mysql.connector.connect(**config)

  print("\n Database user {} connnected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                     config["database"]))

  input("\n\nPress any key to continue... ")

  #create database
  cursor = db.cursor ()
  cursor.execute ("CREATE DATABASE outland_adventures")

  #connect to outland_adventures database
  db = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "titans28",
  database = "outland_adventures"
  )

  #create employees table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE employees (employee_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), "
                 "last_name VARCHAR(255), job_title VARCHAR(255), hire_date DATE)")


  #create customer table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE customer (customer_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), "
                 "last_name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))")


  #create guide table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE guide (guide_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name "
                 "VARCHAR(255), phone VARCHAR(255), email VARCHAR(255))")


  #create equipment table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE equipment (equipment_id INT AUTO_INCREMENT PRIMARY KEY, equipment_name VARCHAR(255), description "
   "VARCHAR(255), purchase_date DATE, purchase_price DECIMAL(10, 2), rental_price DECIMAL(10, 2), "
   "quantity INT, age INT, guide_id INT, FOREIGN KEY (guide_id) REFERENCES guide(guide_id))")


  #create trip table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE trip (trip_id INT AUTO_INCREMENT PRIMARY KEY, trip_name VARCHAR(255), location "
                 "VARCHAR(255), start_date DATE, end_date DATE, guide_id INT, FOREIGN KEY (guide_id) "
                 "REFERENCES guide(guide_id))")


  #create rental table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE rental (rental_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, trip_id INT, "
                 "equipment_id INT, rental_date DATE, return_date DATE, FOREIGN KEY (customer_id) REFERENCES "
                 "customer(customer_id), FOREIGN KEY (trip_id) REFERENCES trip(trip_id), FOREIGN KEY (equipment_id) "
                 "REFERENCES equipment(equipment_id))")


  #create purchase table
  cursor = db.cursor ()
  cursor.execute("CREATE TABLE purchase (purchase_id INT AUTO_INCREMENT PRIMARY KEY, customer_id INT, equipment_id INT, "
                 "purchase_date DATE, price DECIMAL(10, 2), quantity INT, FOREIGN KEY (customer_id) REFERENCES "
                 "customer(customer_id), FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id))")


  print ("Tables created successfully")
  db.close()

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")

	else:
		print(err)
