CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY NOT NULL,
    patient_name VARCHAR(60) NOT NULL,
    patient_gender VARCHAR2(7) NOT NULL,
    patient_blood_group VARCHAR2(5) NOT NULL,
    patient_dob DATE NOT NULL NOT NULL,
    patient_phone_number NUMBER(11,0) NOT NULL,
    patient_address VARCHAR2(60)
)

CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY NOT NULL,

)