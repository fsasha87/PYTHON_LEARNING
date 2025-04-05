# postgress: p_i_psycopg2->psycopg2.connect(dbname="ishop",host="localhost",user="postgres",password="...",port="5432")
# ->c=conn.cursor()->sql1="Select * from product"->c.execute(sql1)->print(c.fetchall())->c.close()->conn.close()
import psycopg2

conn = psycopg2.connect(dbname="ishop", host="localhost", user="postgres", password="!P@ssw0rd", port="5432")
cursor = conn.cursor()
sql1 = "Select * from product"

cursor.execute(sql1)
print(cursor.fetchall())

# conn.commit()  # реальное выполнение команд sql1

cursor.close()
conn.close()

# conn = pymssql.connect(host='localhost',server=servername,
# port='1433', database=my_database)
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM [DB].[dbo].[table]")
# row = cursor.fetchone()
# while row:
# print(row)
# row = cursor.fetchone()