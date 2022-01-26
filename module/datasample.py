import pyodbc
import textwrap

# specify the driver
driver = '{ODBC Driver 17 for SQL Server}'


#specify the server name and database name
server_name = 'database-server-name'
database_name = 'database-name'


# create our server url.
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)


#define username and password.

username = 'Admin-name'
password= 'Password@123'

#create the full connection string.
connection_string = textwrap.dedent('''
    Driver={driver};
    server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
 '''.format(
     driver=driver,
     server=server,
     database=database_name,
     username=username,
     password=password
 ))

 # create a new PYOBDC Connection Object.
cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

# create a new cursor object from the connection
crsr: pyodbc.Cursor = cnxn.cursor()
create_table = 'CREATE TABLE products (product_id int primary key,product_name nvarchar(50),price int)'
insert_sql = "INSERT INTO products (product_id, product_name, price) VALUES (1,'Desktop Computer',800), (2,'Laptop',1200),(3,'Tablet',200),(4,'Monitor',350),(5,'Printer',150)"
select_sql = "SELECT * FROM [products] where product_name = 'Tablet'"

crsr.execute(create_table)
crsr.execute(insert_sql)
crsr.execute(select_sql)

print(crsr.fetchall())

#close the connection when we are done
cnxn.close()



