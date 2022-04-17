-- Function and trigger for patient id.
CREATE OR REPLACE FUNCTION generate_patient_id (phone_no NUMBER)
RETURN INTEGER
IS
    next_seq INTEGER;

BEGIN
    SELECT MAX(patient_id) INTO next_seq FROM Patients 
    WHERE patient_phone_number = phone_no;

    IF next_seq != 0 THEN
        next_seq := next_seq + 1;
    ELSE
        
        next_seq := 1;

        next_seq := TO_NUMBER(
            TO_CHAR(phone_no) ||
            TO_CHAR(next_seq)
        );
    END IF;

    RETURN next_seq;

END;
/

CREATE OR REPLACE TRIGGER generate_patient_id BEFORE INSERT 
ON Patients FOR EACH ROW 
BEGIN
    :NEW.patient_id := generate_patient_id(:NEW.patient_phone_number);
END;
/

-- Function and trigger for doctor id.
CREATE OR REPLACE FUNCTION generate_doctor_id (license_number NUMBER)
RETURN INTEGER
IS
    next_seq INTEGER;

BEGIN
    SELECT MAX(doctor_id) INTO next_seq FROM Doctors 
    WHERE doctor_license_no = license_number;

    IF next_seq != 0 THEN
        next_seq := next_seq + 1;
    ELSE
        
        next_seq := 1;

        next_seq := TO_NUMBER(
            TO_CHAR(license_number) ||
            TO_CHAR(next_seq)
        );
    END IF;

    RETURN next_seq;

END;
/

CREATE OR REPLACE TRIGGER generate_doctor_id 
BEFORE INSERT ON Doctors 
FOR EACH ROW 
BEGIN
    :NEW.doctor_id := generate_doctor_id(:NEW.doctor_license_no);
END;
/

-- Function and trigger for diagnosis id.
CREATE OR REPLACE FUNCTION generate_diag_id(diagnostics_date DATE, diag_patient_id INTEGER)
RETURN INTEGER
IS 

    diag_day INTEGER := EXTRACT (DAY FROM diagnostics_date);
    diag_month INTEGER := EXTRACT (MONTH FROM diagnostics_date);
    diag_year INTEGER := EXTRACT (YEAR FROM diagnostics_date);


BEGIN 

    RETURN TO_NUMBER(
    TO_CHAR(diag_day) || 
    TO_CHAR(diag_month) || 
    TO_CHAR (diag_year) || 
    TO_CHAR(diag_patient_id)
    );

END;
/

CREATE OR REPLACE TRIGGER generate_diag_id 
BEFORE INSERT ON Diagnostics
FOR EACH ROW
BEGIN
    :NEW.diag_id := generate_diag_id(:NEW.diag_date, :NEW.patient_id);
END; 
/

-- Function and trigger for appintment ID.
CREATE OR REPLACE FUNCTION generate_app_id(app_date DATE, app_doctor_id INTEGER)
RETURN INTEGER
IS 

    app_day INTEGER := EXTRACT (DAY FROM app_date);
    app_month INTEGER := EXTRACT (MONTH FROM app_date);
    app_year INTEGER := EXTRACT (YEAR FROM app_date);


BEGIN 

    RETURN TO_NUMBER(
    TO_CHAR(app_day) || 
    TO_CHAR(app_month) || 
    TO_CHAR (app_year) || 
    TO_CHAR(app_doctor_id)
    );

END;
/

CREATE OR REPLACE TRIGGER generate_app_id 
BEFORE INSERT ON Appointments
FOR EACH ROW
BEGIN
    :NEW.app_id := generate_app_id(:NEW.app_date, :NEW.doctor_id);
END; 
/