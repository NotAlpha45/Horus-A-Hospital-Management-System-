import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.uic import loadUi
from functions import *


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("App/UI/landingpage.ui", self)
        self.patientbutton.clicked.connect(self.gotopatient)
        self.doctorbutton.clicked.connect(self.gotodoctor)
        self.appointmentbutton.clicked.connect(self.gotoappointment)
        self.diagbutton.clicked.connect(self.gotodiag)
        self.showapp.clicked.connect(self.gotoshowapp)

    def gotoshowapp(self):
        widget.setCurrentIndex(widget.currentIndex()+5)

    def gotodiag(self):
        widget.setCurrentIndex(widget.currentIndex()+4)

    def gotoappointment(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

    def gotodoctor(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def gotopatient(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


class PatientScreen(QDialog):
    def __init__(self):
        super(PatientScreen, self).__init__()
        loadUi("App/UI/patient.ui", self)
        self.goback.clicked.connect(self.gobackfunction)
        self.patientsubmitbutton.clicked.connect(self.patientinformation)

    def patientinformation(self):
        patient_name = self.patientname.text()
        if self.radioButton.isChecked():
            patient_gender = self.radioButton.text()
        else:
            patient_gender = self.radioButton_2.text()
        patient_blood_group = self.BG.currentText()
        date_of_birth = self.dob.text()
        phone_number = self.phonenumber.text()
        address = self.address.toPlainText()

        print(patient_name)

        enter_patient_entry(
            connection,
            patient_name=patient_name,
            patient_gender=patient_gender,
            patient_blood_group=patient_blood_group,
            patient_dob=date_of_birth,
            patient_phone_number=phone_number,
            patient_address=address
        )
        # return {
        #     'patient_name': patient_name,
        #     'patient_gender': patient_gender,
        #     'patient_blood_group': patient_blood_group,
        #     'date_of_birth': date_of_birth,
        #     'phone_number': patient_gender,
        #     'address': address

        # }

    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


class DoctorScreen(QDialog):
    def __init__(self):
        super(DoctorScreen, self).__init__()
        loadUi("App/UI/doctor.ui", self)
        self.doctorsubmitbutton.clicked.connect(self.doctorinformation)
        self.gobackdoctor.clicked.connect(self.gobackfunction)

    def doctorinformation(self):
        doctor_name = self.doctorname.text()
        designation = self.designation.text()
        license = self.license.text()
        phone_number = self.phone_number.text()
        address = self.address.toPlainText()

        print(doctor_name)

        enter_doctor_entry(
            connection,
            doctor_name=doctor_name,
            doctor_designation=designation,
            doctor_license_no=license,
            doctor_phone_number=phone_number,
            doctor_address=address
        )
        # return {
        #     'doctor_name': doctor_name,
        #     'designation': designation,
        #     'license': license,
        #     'phone_number': phone_number,
        #     'address': address

        # }

    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-2)


class AppointmentScreen(QDialog):
    def __init__(self):
        super(AppointmentScreen, self).__init__()
        loadUi("App/UI/appointment.ui", self)
        self.goback.clicked.connect(self.gobackfunction)
        self.appointmentsubmitbutton.clicked.connect(
            self.appointmentinformation)

    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

    def appointmentinformation(self):
        patient_name = self.patientname.text()
        patient_phone_number = self.patientphonenumber.text()
        doctor_name = self.doctorname.text()
        doctor_phone_number = self.doctorphonenumber.text()
        appointment_date = self.dateEdit.text()

        make_appointment(
            connection,
            patient_id=get_patient_id(
                connection, patient_name, patient_phone_number),
            patient_name=patient_name,
            doctor_id=get_doctor_id(
                connection, doctor_name, doctor_phone_number),
            doctor_name=doctor_name,
            app_date=appointment_date
        )
        # return {
        #     'doctor_name': doctor_name,
        #     'patient_name': patient_name,
        #     'patient_phone_number': patient_phone_number,
        #     'doctor_phone_number': doctor_phone_number,
        #     'appointment_date': appointment_date,

        # }


class DiagScreen(QDialog):
    def __init__(self):
        super(DiagScreen, self).__init__()
        loadUi("App/UI/diagnostic.ui", self)
        self.goback.clicked.connect(self.gobackfunction)
        self.diagsubmitbutton.clicked.connect(self.diaginformation)

    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-4)

    def diaginformation(self):
        patient_name = self.patientname.text()
        patient_phone_number = self.patientphonenumber.text()
        doctor_name = self.doctorname.text()
        doctor_phone_number = self.doctorphonenumber.text()
        diag_details = self.diagdetails.toPlainText()
        diag_remarks = self.diagremarks.toPlainText()
        diag_date = self.diagdate.text()

        print(diag_date)

        try:
            enter_diagnostics_entry(
                connection,
                patient_name=patient_name,
                patient_id=get_patient_id(
                    connection, patient_name, patient_phone_number),
                doctor_name=doctor_name,
                doctor_id=get_doctor_id(
                    connection, doctor_name, doctor_phone_number),
                diag_details=diag_details,
                diag_remarks=diag_remarks,
                diag_date=diag_date
            )
        except cx_Oracle.IntegrityError:
            print("Entry already exists")
        # return{
        #     'patient_name': patient_name,
        #     'patient_phone_number': patient_phone_number,
        #     'doctor_name': doctor_name,
        #     'doctor_phone_number': doctor_phone_number,
        #     'diag_details': diag_details,
        #     'diag_remarks': diag_remarks,
        #     'diag_date': diag_date,
        # }


class AppointmentDisplay(QDialog):
    def __init__(self):
        super(AppointmentDisplay, self).__init__()
        loadUi("App/UI/appointdisplay.ui", self)
        self.goback.clicked.connect(self.gobackfunction)
        self.searchbutton.clicked.connect(self.searchoptions)

    def searchoptions(self):
        patient_name = self.pname.text()
        patient_phone_number = self.pnumber.text()
        doctor_name = self.dname.text()
        doctor_phone_number = self.dnumber.text()

        query_result = None
        if len(patient_name) > 0 and len(patient_phone_number) > 0:
            query_result = get_patient_appointments(
                connection,
                get_patient_id(
                    connection, patient_name, patient_phone_number)
            )
        elif len(doctor_name) > 0 and len(doctor_phone_number) > 0:
            query_result = get_doctor_appointments(
                connection,
                get_doctor_id(
                    connection, doctor_name, doctor_phone_number)
            )
        if query_result:
            self.loaddata(query_result)
        else:
            print("No such appointment")

    def gobackfunction(self):
        widget.setCurrentIndex(widget.currentIndex()-5)

    def loaddata(self, people):

        row = 0
        self.tableWidget.setRowCount(len(people))

        query_list = []

        for result in people:
            query_dict = dict()
            query_dict["appointment_id"] = str(result[0])
            query_dict["patient_name"] = result[2]
            query_dict["doctor_name"] = result[4]
            query_dict["patient_number"] = str(result[1])
            query_dict["date"] = result[5]

            query_list.append(query_dict)

        for person in query_list:
            self.tableWidget.setItem(
                row, 0, QtWidgets.QTableWidgetItem(person["appointment_id"]))
            self.tableWidget.setItem(
                row, 1, QtWidgets.QTableWidgetItem(str(person["patient_name"])))
            self.tableWidget.setItem(
                row, 2, QtWidgets.QTableWidgetItem(person["doctor_name"]))
            self.tableWidget.setItem(
                row, 3, QtWidgets.QTableWidgetItem(person["patient_number"]))
            self.tableWidget.setItem(
                row, 4, QtWidgets.QTableWidgetItem(person["date"]))
            row = row+1


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
patientscreen = PatientScreen()
doctorscreen = DoctorScreen()
appointmentscreen = AppointmentScreen()
diagscreen = DiagScreen()
showappoint = AppointmentDisplay()
widget.addWidget(mainwindow)
widget.addWidget(patientscreen)
widget.addWidget(doctorscreen)
widget.addWidget(appointmentscreen)
widget.addWidget(diagscreen)
widget.addWidget(showappoint)
widget.setFixedHeight(900)
widget.setFixedWidth(800)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
