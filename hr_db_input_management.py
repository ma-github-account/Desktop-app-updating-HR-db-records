
import pyodbc

server = "server"
database = "database"
username = "username"
password = "password"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

def insert_employee_into_database(FirstName, LastName, Age, Nationality, JobTitle, Department, ContractType, FirmBranch, Country, City, Street, BuildingNumber, ApartmentNumber, PostalCode, ProfessionalPhone, PersonalPhone, ProfessionalMail, PersonalMail, EmergencyContactFirstName, EmergencyContactLastName, EmergencyContactPhone, EmergencyContactEmail):

	count = cursor.execute("""
	INSERT INTO Employee (FirstName, LastName, Age, Nationality, JobTitle, Department, ContractType, FirmBranch, Country, City, Street, BuildingNumber, ApartmentNumber, PostalCode, ProfessionalPhone, PersonalPhone, ProfessionalMail, PersonalMail, EmergencyContactFirstName, EmergencyContactLastName, EmergencyContactPhone, EmergencyContactEmail) 
	VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
	FirstName, LastName, Age, Nationality, JobTitle, Department, ContractType, FirmBranch, Country, City, Street, BuildingNumber, ApartmentNumber, PostalCode, ProfessionalPhone, PersonalPhone, ProfessionalMail, PersonalMail, EmergencyContactFirstName, EmergencyContactLastName, EmergencyContactPhone, EmergencyContactEmail).rowcount

	cnxn.commit()














