# Codecademy Data Analyst Challenge Project 
# Langauge - Python
# Concepts - Python Dictionaries
# Prompt - You have been asked to create a program that organizes and updates 
# medical records efficiently.In this project, you will use your new knowledge of 
# Python dictionaries to create a database of medical records for patients.

medicalCosts = {}

# Populate dictionary
medicalCosts["Marina"] = 6607.0
medicalCosts["Vinay"]= 3225.0

# Use 1-line of code to update dictionary with multiple k/v pairs
medicalCosts.update({"Connie": 8886.0, "Isaac": 1644.0, "Valentina": 6420.0})
print(medicalCosts)

# update value in dictionary
medicalCosts['Vinay'] = 3325.0
print(medicalCosts)

# Calculate average medical costs
totalCost = 0
for cost in medicalCosts.values():
    totalCost += cost

averageCost = totalCost / len(medicalCosts)
print(f'Average Insurance Cost: {averageCost} dollars')

# List comprehension with Dictionaries Practice
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27,24,43,35,53]

zippedAges = zip(names, ages)

NamesToAges = {key:value for key,value in zippedAges}
print(NamesToAges)

marinaAge = NamesToAges.get("Marina", None)
print(f"Marina's age is {marinaAge}")

# Use Dictionary to create a medical DB
medicalRecords = {}

# Add people to dictionary using dictionary as the values
medicalRecords["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-Smoker", "InsuranceCost": 6607.0}
medicalRecords["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-Smoker", "InsuranceCost": 3225.0}
medicalRecords["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-Smoker", "InsuranceCost": 8886.0}
medicalRecords["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "InsuranceCost": 16444.0}
medicalRecords["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-Smoker", "InsuranceCost": 6420.0}

print(medicalRecords)

# Print Connies Insurance Cost
print("Connie's insurance cost is " + str(medicalRecords["Connie"]["InsuranceCost"]) + " dollars.")

# Remove an key from dictionary
medicalRecords.pop("Vinay")

for name, record in medicalRecords.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["InsuranceCost"]))
