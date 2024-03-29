import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=psql')

cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
CREATE TABLE table2(
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT false
);
''')

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 2,
    'completed': False
}

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))
cursor.execute(SQL, data)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (3, True))



cursor.execute('select * from table2;')
result = cursor.fetchall()
print(result)

result2 = cursor.fetchone()
print('fectone', result2)

result3 = cursor.fetchmany(2)
print('fetchmany', result3)

connection.commit()

connection.close()
cursor.close()