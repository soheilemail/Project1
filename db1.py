import psycopg2

def do ():
    con = psycopg2.connect(database='DB1', user='postgres', password='postgres')
    cur = con.cursor()
    cur.execute("insert into user1 (id, username) values (98911898, '214')")
    con.commit()
    con.close()

do()