
from hr_db_input_management import *

import tkinter as tk
from tkinter import ttk


class LabelInput(tk.Frame):

  def __init__(
    self, parent, label, var, input_class=ttk.Entry,
    input_args=None, label_args=None, **kwargs
  ):
    super().__init__(parent, **kwargs)
    input_args = input_args or {}
    label_args = label_args or {}
    self.variable = var
    self.variable.label_widget = self

    if input_class in (ttk.Checkbutton, ttk.Button):
      input_args["text"] = label
    else:
      self.label = ttk.Label(self, text=label, **label_args)
      self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))

    if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
      input_args["variable"] = self.variable
    else:
      input_args["textvariable"] = self.variable

    if input_class == ttk.Radiobutton:
      self.input = tk.Frame(self)
      for v in input_args.pop('values', []):
        button = ttk.Radiobutton(
          self.input, value=v, text=v, **input_args)
        button.pack(side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x')
    else:
      self.input = input_class(self, **input_args)

    self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
    self.columnconfigure(0, weight=1)

  def grid(self, sticky=(tk.E + tk.W), **kwargs):
    super().grid(sticky=sticky, **kwargs)

class DataRecordForm(tk.Frame):

	def _add_frame(self, label, cols=2):
	
		frame = ttk.LabelFrame(self, text=label)
		frame.grid(sticky=tk.W + tk.E)
		for i in range(cols):
			frame.columnconfigure(i, weight=1)
		return frame

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
		# Variables
		self._vars = {
		  'FirstName': tk.StringVar(),
		  'LastName': tk.StringVar(),
		  'Age': tk.IntVar(),
		  'Nationality': tk.StringVar(),
		  'JobTitle': tk.StringVar(),
		  'Department': tk.StringVar(),
		  'ContractType': tk.StringVar(),
		  'FirmBranch': tk.StringVar(),
		  'Country': tk.StringVar(),
		  'City': tk.StringVar(),
		  'Street': tk.StringVar(),
		  'BuildingNumber': tk.IntVar(),
		  'ApartmentNumber': tk.IntVar(),
		  'PostalCode': tk.StringVar(),
		  'ProfessionalPhone': tk.StringVar(),
		  'PersonalPhone': tk.StringVar(),
		  'ProfessionalMail': tk.StringVar(),
		  'PersonalMail': tk.StringVar(),
		  'EmergencyContactFirstName': tk.StringVar(),
		  'EmergencyContactLastName': tk.StringVar(),
		  'EmergencyContactPhone': tk.StringVar(),
		  'EmergencyContactEmail': tk.StringVar(),
		}
	
		# Build the form
		self.columnconfigure(0, weight=1)
	
		# Personal Information
		pi_info = self._add_frame("Personal Information")
	
		LabelInput(
		  pi_info, "First Name", var=self._vars['FirstName']
		).grid(row=0, column=0)
		LabelInput(
		  pi_info, "Last Name", var=self._vars['LastName']
		).grid(row=0, column=1)
		LabelInput(
		  pi_info, "Age", input_class=ttk.Spinbox,
		  var=self._vars['Age'],
		  input_args={"from_": 0, "to": 100, "increment": 1}
		).grid(row=1, column=0)
		LabelInput(
		  pi_info, "Nationality", input_class=ttk.Combobox, var=self._vars['Nationality'],
		  input_args={"values": list(["Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Antiguans", "Argentinean", "Armenian", "Australian", "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi", "Barbadian", "Barbudans", "Batswana", "Belarusian", "Belgian", "Belizean", "Beninese", "Bhutanese", "Bolivian", "Bosnian", "Brazilian", "British", "Bruneian", "Bulgarian", "Burkinabe", "Burmese", "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", "Central African", "Chadian", "Chilean", "Chinese", "Colombian", "Comoran", "Congolese", "Costa Rican", "Croatian", "Cuban", "Cypriot", "Czech", "Danish", "Djibouti", "Dominican", "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirian", "Equatorial Guinean", "Eritrean", "Estonian", "Ethiopian", "Fijian", "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German", "Ghanaian", "Greek", "Grenadian", "Guatemalan", "Guinea-Bissauan", "Guinean", "Guyanese", "Haitian", "Herzegovinian", "Honduran", "Hungarian", "I-Kiribati", "Icelander", "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakhstani", "Kenyan", "Kittian and Nevisian", "Kuwaiti", "Kyrgyz", "Laotian", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtensteiner", "Lithuanian", "Luxembourger", "Macedonian", "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese", "Marshallese", "Mauritanian", "Mauritian", "Mexican", "Micronesian", "Moldovan", "Monacan", "Mongolian", "Moroccan", "Mosotho", "Motswana", "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Ni-Vanuatu", "Nicaraguan", "Nigerian", "Nigerien", "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Polish", "Portuguese", "Qatari", "Romanian", "Russian", "Rwandan", "Saint Lucian", "Salvadoran", "Samoan", "San Marinese", "Sao Tomean", "Saudi", "Scottish", "Senegalese", "Serbian", "Seychellois", "Sierra Leonean", "Singaporean", "Slovakian", "Slovenian", "Solomon Islander", "Somali", "South African", "South Korean", "Spanish", "Sri Lankan", "Sudanese", "Surinamer", "Swazi", "Swedish", "Swiss", "Syrian", "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian", "Tunisian", "Turkish", "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbekistani", "Venezuelan", "Vietnamese", "Welsh", "Yemenite", "Zambian", "Zimbabwean" ])}
		).grid(row=1, column=1)
	
		# Employment Details
		ed_info = self._add_frame("Employment Details")
	
		LabelInput(
		  ed_info, "Job Title", var=self._vars['JobTitle']
		).grid(row=0, column=0)
		LabelInput(
		  ed_info, "Department", input_class=ttk.Combobox, var=self._vars['Department'],
		  input_args={"values": list(["Human Resources", "Legal", "Sales", "IT", "Customer Support", "Financial"])}
		).grid(row=0, column=1)
		LabelInput(
		  ed_info, "Contract Type", input_class=ttk.Combobox, var=self._vars['ContractType'],
		  input_args={"values": list(["Fixed-term employment", "Part-time employment", "Agency work employment", "B2B", "Other"])}
		).grid(row=1, column=0)
		LabelInput(
		  ed_info, "Firm Branch", input_class=ttk.Combobox, var=self._vars['FirmBranch'],
		  input_args={"values": list(["Amsterdam", "Bangalore", "London", "New York", "Prague", "Singapore", "Tokyo"])}
		).grid(row=1, column=1)
	
		# Address Details
		ad_info = self._add_frame("Address Details")
	
		LabelInput(
		  ad_info, "Country", var=self._vars['Country']
		).grid(row=0, column=0)
		LabelInput(
		  ad_info, "City", var=self._vars['City']
		).grid(row=0, column=1)
		LabelInput(
		  ad_info, "Street", var=self._vars['Street']
		).grid(row=1, column=0)
		LabelInput(
		  ad_info, "Building Number", input_class=ttk.Spinbox,
		  var=self._vars['BuildingNumber'],
		  input_args={"from_": 0, "to": 1000, "increment": 1}
		).grid(row=1, column=1)
		LabelInput(
		  ad_info, "Apartment Number", input_class=ttk.Spinbox,
		  var=self._vars['ApartmentNumber'],
		  input_args={"from_": 0, "to": 1000, "increment": 1}
		).grid(row=2, column=0)
		LabelInput(
		  ad_info, "Postal Code", var=self._vars['PostalCode']
		).grid(row=2, column=1)
	
		# Contact Information
		ci_info = self._add_frame("Contact Information")
	
		LabelInput(
		  ci_info, "Professional Phone", var=self._vars['ProfessionalPhone']
		).grid(row=0, column=0)
		LabelInput(
		  ci_info, "Personal Phone", var=self._vars['PersonalPhone']
		).grid(row=0, column=1)
		LabelInput(
		  ci_info, "Professional Mail", var=self._vars['ProfessionalMail']
		).grid(row=1, column=0)
		LabelInput(
		  ci_info, "Personal Mail", var=self._vars['PersonalMail']
		).grid(row=1, column=1)
	
		# Emergency Contact
		ec_info = self._add_frame("Emergency Contact Information")
	
		LabelInput(
		  ec_info, "First Name", var=self._vars['EmergencyContactFirstName']
		).grid(row=0, column=0)
		LabelInput(
		  ec_info, "Last Name", var=self._vars['EmergencyContactLastName']
		).grid(row=0, column=1)
		LabelInput(
		  ec_info, "Phone", var=self._vars['EmergencyContactPhone']
		).grid(row=1, column=0)
		LabelInput(
		  ec_info, "Email", var=self._vars['EmergencyContactEmail']
		).grid(row=1, column=1)
	
		# buttons
		buttons = ttk.Frame(self)
		buttons.grid(sticky=tk.W + tk.E, row=8)
		self.savebutton = ttk.Button(
		  buttons, text="Upload to database", command=self.master._on_save)
		self.savebutton.pack(side=tk.RIGHT)
	
		self.resetbutton = ttk.Button(
		  buttons, text="Reset", command=self.reset)
		self.resetbutton.pack(side=tk.LEFT)

		# default the form
		self.reset()

	def get(self):

		data = dict()
		for key, variable in self._vars.items():
		    try:
		      data[key] = variable.get()
		    except tk.TclError:
		      message = f'Error in field: {key}.  Data was not saved!'
		      raise ValueError(message)

		return data

	def reset(self):

		for var in self._vars.values():
		  if isinstance(var, tk.BooleanVar):
		    var.set(False)
		  else:
		    var.set('')

class Application(tk.Tk):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title("Employee Data Register")
		self.columnconfigure(0, weight=1)

		ttk.Label(
		  self, text="Employee Data Register",
		  font=("TkDefaultFont", 16)
		).grid(row=0)

		self.recordform = DataRecordForm(self)
		self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))

		self.status = tk.StringVar()
		ttk.Label(
		  self, textvariable=self.status
		).grid(sticky=(tk.W + tk.E), row=2, padx=10)

	def _on_save(self):
	
		print("Test")

		try:
			data = self.recordform.get()

			FirstName = data["FirstName"]
			LastName = data["LastName"]
			Age = data["Age"]
			Nationality = data["Nationality"]
			JobTitle = data["JobTitle"]
			Department = data["Department"]
			ContractType = data["ContractType"]
			FirmBranch = data["FirmBranch"]
			Country = data["Country"]
			City = data["City"]
			Street = data["Street"]
			BuildingNumber = data["BuildingNumber"]
			ApartmentNumber = data["ApartmentNumber"]
			PostalCode = data["PostalCode"]
			ProfessionalPhone = data["ProfessionalPhone"]
			PersonalPhone = data["PersonalPhone"]
			ProfessionalMail = data["ProfessionalMail"]
			PersonalMail = data["PersonalMail"]
			EmergencyContactFirstName = data["EmergencyContactFirstName"]
			EmergencyContactLastName = data["EmergencyContactLastName"]
			EmergencyContactPhone = data["EmergencyContactPhone"]
			EmergencyContactEmail = data["EmergencyContactEmail"]

			insert_employee_into_database(FirstName, LastName, Age, Nationality, JobTitle, Department, ContractType, FirmBranch, Country, City, Street, BuildingNumber, ApartmentNumber, PostalCode, ProfessionalPhone, PersonalPhone, ProfessionalMail, PersonalMail, EmergencyContactFirstName, EmergencyContactLastName, EmergencyContactPhone, EmergencyContactEmail)

		except ValueError as e:
			self.status.set(str(e))

if __name__ == "__main__":

  app = Application()
  app.mainloop()





