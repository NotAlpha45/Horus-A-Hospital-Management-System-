CREATE TABLE Patients (
    patient_id NUMBER PRIMARY KEY NOT NULL,
    patient_name VARCHAR2(255) NOT NULL,
    patient_gender VARCHAR2(7) NOT NULL,
    patient_blood_group VARCHAR2(5) NOT NULL,
    patient_dob DATE NOT NULL,
    patient_phone_number NUMBER(11,0) NOT NULL,
    patient_address VARCHAR2(255)
);

CREATE TABLE Doctors (
    doctor_id NUMBER PRIMARY KEY NOT NULL,
    doctor_name VARCHAR2(255) NOT NULL,
    doctor_designation VARCHAR2(255) NOT NULL,
    doctor_license_no NUMBER NOT NULL,
    doctor_phone_number NUMBER NOT NULL,
    doctor_address VARCHAR2(255) NOT NULL
);

CREATE TABLE Appointments (
    app_id NUMBER PRIMARY KEY NOT NULL,
    patient_id NUMBER,
    patient_name VARCHAR2(255) NOT NULL,
    doctor_id NUMBER,
    doctor_name VARCHAR2(255) NOT NULL,
    app_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients (patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors (doctor_id) ON DELETE CASCADE
);

CREATE TABLE Diagnostics (
    diag_id NUMBER PRIMARY KEY NOT NULL,
    patient_id NUMBER NOT NULL,
    patient_name VARCHAR2(255) NOT NULL,
    doctor_id NUMBER NOT NULL,
    doctor_name VARCHAR2(255) NOT NULL,
    diag_details VARCHAR2(3000) NOT NULL,
    diag_remarks VARCHAR2(3000) NOT NULL,
    diag_date DATE NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients (Patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors (doctor_id)
);