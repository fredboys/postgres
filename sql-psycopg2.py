import psycopg2 

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Selcts only the "Name" column from the Artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

#Query 3 - Select only "Queen" from the Artist table
# cursor.execute('SELECT *FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the Artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - Selct all tracks where the composer is "Queen" from the track table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"]) 

results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

for results in results:
    print(results)