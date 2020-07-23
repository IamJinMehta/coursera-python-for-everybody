import sqlite3

conn = sqlite3.connect('trackdb1.sqlite')
cur = conn.cursor()

sqlstr='''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3 '''
for row in cur.execute(sqlstr):
    print (str(row[0]),str(row[1]),str(row[2]),str(row[3]))
cur.close()
