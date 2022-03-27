import csv
import json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath) as cf:
		csvReader = csv.DictReader(cf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Here you enter the name of the first column 
			key = rows['SUMLEV']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jf:
		jf.write(json.dumps(data, indent=4))
		

# Decide the two file paths according to your
# computer system
csvFilePath = r'DataProject/county_pop_data.csv'
jsonFilePath = r'DataProject/county_pop_data.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
