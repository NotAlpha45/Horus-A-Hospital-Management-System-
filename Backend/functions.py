from connector import *

connection = get_connecetion("c##maheen", "maheen123")
# cursor = connection.cursor()


def get_all_patients(connection):
    cursor = connection.cursor()
    return cursor.execute(
        f'''SELECT * FROM PATIENTS'''
    ).fetchall()


def enter_patient_entry(connection, **kwargs):
    cursor = connection.cursor()
    print(kwargs)
    try:
        # Inserting with bind variables to protect from Injection attacks
        cursor.execute(
            '''
            INSERT INTO Patients(patient_name, patient_gender, patient_blood_group, patient_dob, patient_phone_number, patient_address) 
            VALUES (
                :p_n, :p_g, :p_bg, TO_DATE(:p_dob, 'DD-MON-YYYY'), TO_NUMBER(:p_phn), :p_addr
            )''',
            [
                kwargs["patient_name"],
                kwargs["patient_gender"],
                kwargs["patient_blood_group"],
                kwargs["patient_dob"],
                kwargs["patient_phone_number"],
                kwargs["patient_address"]
            ]
        )
        connection.commit()

    except KeyError:
        print("The attributes are not correct")
        return


def enter_doctor_entry(connection, **kwargs):
    cursor = connection.cursor()
    try:
        # Inserting with bind variables to protect from Injection attacks
        cursor.execute(
            '''
            INSERT INTO Doctors(doctor_name, doctor_designation, doctor_license_no, doctor_phone_number, doctor_address) 
            VALUES (
                :d_n, :d_desig, :d_lno, TO_NUMBER(:d_phn), :d_addr
            )''',
            [
                kwargs["doctor_name"],
                kwargs["doctor_designation"],
                kwargs["doctor_license_no"],
                kwargs["doctor_phone_number"],
                kwargs["doctor_address"]
            ]
        )
        connection.commit()

    except KeyError:
        print("The attributes are not correct")
        return "The attributes are not correct"


def get_patient_id(connection, patient_name, patient_dob, patient_phone):
    cursor = connection.cursor()

    query_result = cursor.execute(
        '''SELECT patient_id FROM Patients
        WHERE patient_name = :p_name AND patient_phone_number = TO_NUMBER(:p_number) AND patient_dob = :dob
        ''',
        [patient_name, patient_phone, patient_dob]
    ).fetchall()

    cursor.close()

    if query_result:
        return query_result[0][0]
    else:
        return 0


def get_doctor_id(connection, doctor_name, doctor_phone):
    cursor = connection.cursor()

    query_result = cursor.execute(
        '''SELECT doctor_id FROM Doctors
        WHERE doctor_name = :d_name AND doctor_phone_number = TO_NUMBER(:d_number)
        ''',
        [doctor_name, doctor_phone]
    ).fetchall()

    if query_result:
        return query_result[0][0]
    else:
        return 0


def enter_diagnostics_entry(connection, **kwargs):
    cursor = connection.cursor()
    try:
        # Inserting with bind variables to protect from Injection attacks
        cursor.execute(
            '''
            INSERT INTO Diagnostics(patient_id, doctor_id, diag_details, diag_remarks, diag_date) 
            VALUES (
                :p_id, :d_id, :d_det, :d_rem, TO_DATE(:d_addr)
            )''',
            [
                kwargs["patient_id"],
                kwargs["doctor_id"],
                kwargs["diag_details"],
                kwargs["diag_remarks"],
                kwargs["diag_date"]
            ]
        )
        connection.commit()

    except KeyError:
        print("The attributes are not correct")
        return "The attributes are not correct"


def get_diagnostics_id(connection, date, patient_id, doctor_id):
    cursor = connection.cursor()
    query_result = cursor.execute(
        '''
        SELECT diag_id FROM Diagnostics
        WHERE patient_id = :pid AND doctor_id = :d_id AND diag_date = TO_DATE(:d_date, \'DD-MON-YYYY\')
        ''',
        [patient_id, doctor_id, date]
    ).fetchall()
    cursor.close()

    if query_result:
        return query_result[0][0]
    else:
        return 0


def generate_diagnostics_report(connection, diag_id):
    cursor = connection.cursor()

    query_result = cursor.execute(
        f'''
        SELECT diag_date, diag_details, diag_remarks FROM Diagnostics 
        WHERE diag_id = :dia_id
        ''',
        [diag_id]
    ).fetchall()

    if query_result:
        return f'''
        Date : 
        ------
        {query_result[0][0]}
        ------------------------
        Diag remarks : 
        --------------
        {query_result[0][2]}
        --------------------------------
        Diag details : 
        {query_result[0][1]}
        '''
    else:
        return "No report found"


def make_appointment(connection, doctor_id, patient_id, date):
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO Appointments (patient_id, doctor_id, app_date)
            VALUES (:pid, :did, TO_DATE(:pdate, \'DD-MON-YYYY\'))
            ''',
            [patient_id, doctor_id, date]
        )
        connection.commit()

        print(f"Appointment created on {date}")
        return f"Appointment created on {date}"

    except cx_Oracle.IntegrityError:
        print("Appointment already exists")
        return "Appointment already exists"


def get_appointment_id(connection, doctor_id, patient_id, date):
    cursor = connection.cursor()

    query_result = cursor.execute(
        '''
        SELECT app_id FROM Appointments 
        WHERE doctor_id = :d_id AND patient_id = :p_id AND app_date = :a_date
        ''',
        [doctor_id, patient_id, date]
    ).fetchall()

    if query_result:
        return query_result[0][0]
    else:
        return 0


make_appointment(
    connection,
    get_doctor_id(connection, "Sadik", "01778654757"),
    get_patient_id(connection, "Sakibul", "15-DEC-00", "01798654757"),
    "16-APR-2022"
)

# print(get_patient_id(connection, "Sakibul", "15-DEC-00", "01798654757"))
# print(get_diagnostics_id(
#     connection,
#     "12-APR-2022",
#     get_patient_id(connection, "Sakibul", "15-DEC-2000", "01798654757"),
#     get_doctor_id(connection, "Sadik", "01778654757")
# ))

# print(
#     generate_diagnostics_report(
#         connection,
#         get_diagnostics_id(
#             connection,
#             "12-APR-2022",
#             get_patient_id(connection, "Sakibul",
#                            "15-DEC-2000", "01798654757"),
#             get_doctor_id(connection, "Sadik", "01778654757")
#         )
#     )
# )

# enter_patient_entry(
#     connection,
#     patient_name="Sakibul",
#     patient_gender="Male",
#     patient_blood_group="A+",
#     patient_dob='15-DEC-2000',
#     patient_phone_number='01798654757',
#     patient_address="Dhaka"
# )

# enter_doctor_entry(
#     connection,
#     doctor_designation="Surgeon",
#     doctor_license_no=42069,
#     doctor_phone_number="01778654757",
#     doctor_address="Mohammadpur",
#     doctor_name="Sadik"
# )


# print(get_doctor_id(connection, "Sadik", "01778654757"))
# enter_diagnostics_entry(
#     connection,
#     patient_id=get_patient_id(connection, "Sakibul",
#                               "15-DEC-00", "01798654757"),
#     doctor_id=get_doctor_id(connection, "Sadik", "01778654757"),
#     diag_details="Erectile dysfunction",
#     diag_remarks="baccha hobena",
#     diag_date="12-APR-2022"
# )

connection.close()
