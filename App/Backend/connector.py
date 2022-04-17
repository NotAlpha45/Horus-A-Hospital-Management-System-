import cx_Oracle

print("Hello from connector!")


def get_connecetion(username, password):
    try:
        connection = cx_Oracle.connect(
            username+'/'+password+"@//localhost:1521/orclpdb"
        )
        print(connection.version)
        connection.close()

    except cx_Oracle.DatabaseError:
        print("Connection not possible")
        exit()

    # To connect as that user in PDB : connect <username>@orclpdb;
    # format : <username>/<password>@//localhost:<port_number>/<container_name>
    connection = cx_Oracle.connect(
        username+'/'+password+"@//localhost:1521/orclpdb"
    )

    return connection

# cursor = connection.cursor()

# cursor.execute(
#     f'''
#     INSERT INTO Patients(patient_name, patient_gender, patient_blood_group, patient_dob, patient_phone_number, patient_address) VALUES
#     ('a', 'male', 'a+', TO_DATE('12-12-2021', 'DD-MM-YYYY'), 01712181229, 'c')
#     '''
# )
# connection.commit()

# cursor.execute(
#     '''
#     SELECT * FROM Patients
#     '''
# )

# print(cursor.fetchall())

# cursor.close()
# connection.close()
# print(cursor.fetchall())
