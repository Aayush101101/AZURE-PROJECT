import pyodbc
import textwrap

# specify the driver
driver = '{SQL Server}'


#specify the server name and database name
server_name = 'database-server-name.database.windows.net'
database_name = 'database-name'


# create our server url.
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)


#define username and password.

username = 'Admin-name'
password= 'Password@123'

#create the full connection string.
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=database-server-name.database.windows.net;'
                      'Database=database-name;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE products (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')

conn.commit()