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
	def show_films(cursor, title):
		# method to execute an inner join on all tables,
		# iterate over the dataset and ouput the results to the terminal window.

		# inner join query
		cursor.execute(
			"select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film "
			"INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
		# gets the results from the cursor object
		films = cursor.fetchall()
		print("\n -- {} --".format(title))

		# iterate over the film data set and display the results
		seen_films = set()
		for film in films:
			if film[0] not in seen_films:
				seen_films.add(film[0])
				print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1],
																								 film[2],
																								 film[3]))

	db = mysql.connector.connect(**config)

	print("\n Database user {} connnected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	input("\n\nPress any key to continue... ")

	#Studio_id, and studio_name Query
	cursor = db.cursor()
	show_films(cursor, "DISPLAYING FILMS")
	sql = "INSERT INTO film(film_id, film_name, film_releaseDate, film_runtime, film_director, genre_id, studio_id) VALUES(%s,%s,%s,%s,%s,%s, %s)"
	values = (4,'Star Wars: Episode IV - A New Hope', '1977', '121', 'George Lucas', 2, 1)
	cursor.execute(sql,values)
	db.commit()

	show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

	cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
	show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - CHANGED ALIEN TO HORROR ")

	cursor.execute("DELETE FROM film WHERE film_id = 1")
	show_films(cursor, "DISPLAYING FILMS AFTER DELETE")




except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")

	else:
		print(err)

finally:
	db.close()







