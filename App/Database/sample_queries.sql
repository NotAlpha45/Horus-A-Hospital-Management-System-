INSERT INTO Patients(patient_name, patient_gender, patient_blood_group, patient_dob, patient_phone_number, patient_address) VALUES
('a', 'male', 'a+', TO_DATE('12-12-2021', 'DD-MM-YYYY'), 01712181229, 'c');
-- Patient ID generated : 17121812291

INSERT INTO Doctors(doctor_name, doctor_designation, doctor_license_no, doctor_phone_number, doctor_address) VALUES
('a', 'surgeon', 42069, 01712181229, 'csa');
-- Doctor ID generated : 420691

DECLARE
    dt DATE := SYSDATE;
BEGIN
    DBMS_OUTPUT.PUT_LINE(dt);
END;

INSERT INTO Diagnostics (patient_id, doctor_id, diag_details, diag_remarks, diag_date) 
VALUES (17121812291, 420691, 'uwieryuiqweu', 'zxcgxzbcvcx', TO_DATE('15-APR-2022', 'DD-MON-YYYY'));

INSERT INTO Appointments (patient_id, doctor_id, app_date)
VALUES (17121812291, 420691, TO_DATE('15-APR-2022', 'DD-MON-YYYY'));