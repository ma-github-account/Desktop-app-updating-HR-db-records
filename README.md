This desktop application allows to upload employee information into the HR database. User fills the form and clicks "Upload_to_database" button.

Application uses object oriented code to subclass Tkinter widgets.
For that I have used the methodology explained by Alan D. Moore in his book Python GUI Programming with Tkinter (Chapter 4).

Prerequisites:

Python 3.9.7
tkinter
pyodbc

We are uploading the player information into database:

CREATE TABLE [dbo].[Employee]( 
[FirstName] varchar (50) NOT NULL, 
[LastName] varchar (50) NOT NULL,
[Age] [int] NOT NULL, 
[Nationality] varchar (50) NOT NULL, 
[JobTitle] varchar (50) NOT NULL, 
[Department] varchar (50) NOT NULL, 
[ContractType] varchar (50) NOT NULL, 
[FirmBranch] varchar (50) NOT NULL, 
[Country] varchar (50) NOT NULL, 
[City] varchar (50) NOT NULL, 
[Street] varchar (50) NOT NULL, 
[BuildingNumber] [int] NOT NULL, 
[ApartmentNumber] [int], 
[PostalCode] varchar (50) NOT NULL,
[ProfessionalPhone] varchar (50) NOT NULL,
[PersonalPhone] varchar (50) NOT NULL,
[ProfessionalMail] varchar (50) NOT NULL,
[PersonalMail] varchar (50) NOT NULL,
[EmergencyContactFirstName] varchar (50) NOT NULL,
[EmergencyContactLastName] varchar (50) NOT NULL,
[EmergencyContactPhone] varchar (50) NOT NULL,
[EmergencyContactEmail] varchar (50) NOT NULL)

How to run: python employee_info_registry.py








![1](https://user-images.githubusercontent.com/89083426/166502846-c0fc9b0b-baed-47e3-b22c-d78d2583b2db.png)

![2](https://user-images.githubusercontent.com/89083426/166502871-cd3ff076-f94f-4b28-99b4-76ef0eb6b9ff.png)






