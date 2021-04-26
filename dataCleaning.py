from DataCleaner import DataCleaner
import os
import csv

# Save excels as csvs to create data cleaner instances
DataCleaner.saveExcelFileAsCsv("Data/Enforcement_Policies_Data.xlsx")
DataCleaner.saveExcelFileAsCsv("Data/Integration_Policies_Data.xlsx")
DataCleaner.saveExcelFileAsCsv("Data/Public_Benefits_Data.xlsx")

"""
Each variable has its own sheet within the excel file, after using
the data cleaner method each sheet is now its own csv.
These are the variables we need and how to recode them:

Enforcement:
287(g) task force- 0 = pro immigration, 1 and 2 = anti immigration
Limited co-op w/ detainers- 0 = anti immigration, 1 and 2 = pro immigration
E-verify- 0= pro immigration, 1 and 2 = anti immigration

Integration:
English as official language- 0 = pro immigration, 1 = anti immigration
Driver's license policies- 0 = anti immigration, 1 = pro immigration

Public Benefits:
Public ins unauth kids- 0 = anti immigration, 1 = pro immigration
Medicaid unauth adults- 0 = anti immigration, 1 = pro immigration
Food asst. LPR kids- 0 = anti immigration, 1 = pro immigration
Food asst. LPR adults- 0 = anti immigration, 1 = pro immigration

Each variable will be recoded to have 0 as anti immigration and 1 as pro immigration.
"""

# Create a new directory for all the cleaned final data
os.mkdir("CleanedData/")

batchCleaningData = [
	# ---------------------- Enforcement ----------------------

	# 287(g) task force- 0 = pro immigration, 1 and 2 = anti immigration
	{
		"filename": "Data/Enforcement_Policies_Data/287g Task Force 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 4,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Task Force Agreement",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": ["Task Force Agreement"],
		"mappedValues": [{"0": "1", "1": "0", "2": "0"}],
		"cleanedFilename": "CleanedData/enforcementTaskForce.csv"
	},

	# Limited co-op w/ detainers- 0 = anti immigration, 1 and 2 = pro immigration
	{
		"filename": "Data/Enforcement_Policies_Data/Limited Coop w Detainers 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 6,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Cooperation With Detainers",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": ["Cooperation With Detainers"],
		"mappedValues": [{"0": "0", "1": "1", "2": "1"}],
		"cleanedFilename": "CleanedData/enforcementCoopDetainers.csv"
	},

	# E-verify- 0 = pro immigration, 1 and 2 = anti immigration
	{
		"filename": "Data/Enforcement_Policies_Data/EVerify 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 5,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "EVerify Mandates",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": ["EVerify Mandates"],
		"mappedValues": [{"0": "1", "1": "0", "2": "0"}],
		"cleanedFilename": "CleanedData/enforcementEVerify.csv"
	},

	# ---------------------- Integration ----------------------

	# English as official language- 0 = pro immigration, 1 = anti immigration
	{
		"filename": "Data/Integration_Policies_Data/English as official lang 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 2,
		"cols": [(1, "State"), (19, "Year English Declared")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "English Declared",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": ["English Declared", "Year English Declared"],
		"mappedValues": [{"0": "1", "1": "0"}, {".": ""}],
		"cleanedFilename": "CleanedData/integrationEnglishLang.csv"
	},

	# Driver's license policies- 0 = anti immigration, 1 = pro immigration
	# Cleaning Failed - Was unable to find data regarding immigration, only data
	# regarding when certain license policy laws were passed was available.

	# ---------------------- Public Benefits ----------------------

	# Public ins unauth kids- 0 = anti immigration, 1 = pro immigration
	{
		"filename": "Data/Public_Benefits_Data/Pub ins unauth kids 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 6,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Insurance for Unauth Kids",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": [],
		"mappedValues": [],
		"cleanedFilename": "CleanedData/publicBenefitsUnauthKidsInsurance.csv"
	},

	# Medicaid unauth adults- 0 = anti immigration, 1 = pro immigration
	{
		"filename": "Data/Public_Benefits_Data/Medicaid unauth adult 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 7,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Insurance for Unauth Adults",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": [],
		"mappedValues": [],
		"cleanedFilename": "CleanedData/publicBenefitsMedicaidUnauthAdult.csv"
	},

	# Food asst. LPR kids- 0 = anti immigration, 1 = pro immigration
	{
		"filename": "Data/Public_Benefits_Data/Food asst LPR kids 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 6,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Food Assist for Immigrant Kids",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": [],
		"mappedValues": [],
		"cleanedFilename": "CleanedData/publicBenefitsfoodAssistKids.csv"
	},

	# Food asst. LPR adults- 0 = anti immigration, 1 = pro immigration
	{
		"filename": "Data/Public_Benefits_Data/Food asst LPR adults 01.csv",
		"numSkippedRows": 2,
		"numFooterRows": 9,
		"cols": [(1, "State")],
		"colsToRows": {
			"colName": "Year",
			"dataColName": "Food Assist for Immigrant Adults",
			"cols": [(2 + year - 2000, str(year)) for year in range(2000, 2016)]
		},
		"mappedCols": [],
		"mappedValues": [],
		"cleanedFilename": "CleanedData/publicBenefitsfoodAssistAdults.csv"
	}
]

# Run the batch data cleaning
for cleaningArguments in batchCleaningData:
	cleaner = DataCleaner(
		filename = cleaningArguments["filename"],
		numSkippedRows = cleaningArguments["numSkippedRows"],
		numFooterRows = cleaningArguments["numFooterRows"],
		cols = cleaningArguments["cols"],
		colsToRows = cleaningArguments["colsToRows"]
	)

	for index in range(len(cleaningArguments["mappedCols"])):
		cleaner.map(cleaner[cleaningArguments["mappedCols"][index]], cleaningArguments["mappedValues"][index])

	cleaner.saveData(cleaningArguments["cleanedFilename"], True)

# Create a separate csv with all the dataset names to read in from R when merging
with open("CleanedData/datasets.csv", "w", newline='') as file:
	csvWriter = csv.writer(file)
	csvWriter.writerows([["Filename"]] + [[x["cleanedFilename"]] for x in batchCleaningData])