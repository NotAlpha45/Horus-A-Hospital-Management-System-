CREATE FUNCTION generate_patient_id (phone_no NUMBER)
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

CREATE TRIGGER generate_patient_id BEFORE INSERT 
ON Patients FOR EACH ROW 
BEGIN
    :NEW.patient_id := generate_patient_id(:NEW.patient_phone_number);
END;