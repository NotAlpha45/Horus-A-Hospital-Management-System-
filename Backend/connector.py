import cx_Oracle

try:
    connection = cx_Oracle.connect(
        "c##maheen/maheen123@//localhost:1521/orclpdb"
    )
    print(connection.version)
    connection.close()

except cx_Oracle.DatabaseError:
    print("Connection not possible")
    exit()

# To connect as that user in PDB : connect <username>@orclpdb;
# format : <username>/<password>@//localhost:<port_number>/<container_name>
cursor = cx_Oracle.connect(
    "c##maheen/maheen123@//localhost:1521/orclpdb"
).cursor()

cursor.execute(
    f'''
    SELECT * FROM Patients
    '''
)

print(cursor.fetchall())
