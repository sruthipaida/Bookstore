import psycopg2

def connect():
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id SERIAL PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT )")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO book (title,author,year,isbn) VALUES  ('%s', '%s','%s','%s') " % (title,author,year,isbn))
    conn.commit()
    conn.close()
def view():
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ORDER by id ASC")
    rows=cur.fetchall()
    conn.close()
    return rows
def search(title="",author="",year="",isbn=""):
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title='%s' OR author='%s' OR year='%s' OR isbn='%s'" % (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id):
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=%s" %(id))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = psycopg2.connect("dbname='Book_Database' user='postgres' password='123456' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE book SEt title='%s',author='%s',year=%s,isbn=%s WHERE id=%s" %(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()


