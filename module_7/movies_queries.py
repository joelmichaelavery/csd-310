import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "root", 
	"password": "titans28", 
	"host": "127.0.0.1",
	"database": "movies", 
	"raise_on_warnings": True
}

try: 
	db = mysql.connector.connect(**config)

	print("\n Database user {} connnected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\nPress any key to continue... ")

	print("-- DISPLAYING Studio RECORDS --")

	#Studio_id, and studio_name Query
	cursor = db.cursor()
	cursor.execute("SELECT studio_id, studio_name FROM studio") #selecting two field
	studios = cursor.fetchall()
	for studio_id, studio_name in studios :
		print(f"Studio ID: {studio_id}\nStudio Name: {studio_name}\n")

	#Displaying the Genre Records Query
	print("-- DISPLAYING Genre RECORDS --")
	cursor.execute("SELECT genre_id, genre_name FROM genre") #selecting two fields
	film = cursor.fetchall()
	for genre_id, genre_name in film:
		print(f"Genre ID: {genre_id}\nGenre Name: {genre_name}\n")

	#Displaying the Short Film Records
	print("-- DISPLAYING Short Film RECORDS --")
	cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <= 120") #selecting two fileds where time is under or equal to 120 minutes
	time = cursor.fetchall()
	for film_name, film_runtime in time:
		print(f"Film Name: {film_name}\nRuntime: {film_runtime}\n")

	#Displaying film names ordered by a director name
	print("-- DISPLAYING Director RECORDS in Order --")
	cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director") #selecting two fields sorted by film_director name
	movie = cursor.fetchall()
	for film_name, film_director in movie:
		print(f"Film name: {film_name}\nDirector: {film_director}\n")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")

	else:
		print(err)

finally:
	db.close()


