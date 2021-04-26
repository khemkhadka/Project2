import csv
import openpyxl
import os

"""
This class can be used for cleaning any dataset
"""
class DataCleaner:

	"""
	Creates a new data Cleaner class instance given the file to clean.

	args:
		filename (str): The file to clean
		numSkippedRows (int): The number of rows to skip
		numFooterRows (int): The number of rows to skip at the bottom
		cols (array<tuple<int, str>>): An array of all the column names in the dataset with their index (OPTIONAL)
		colsToRows (dictionary<string, arguments>): A dictionary specifying necessary arguments in order to turn certain columns
			into rows. The dictionary must have the following elements:
			(OPTIONAL)
			"colName" => "The name of the column containing all of the cols titles",
			"dataColName" => "The name of the column containing all of the cols data",
			"cols" => [An array of the columns to turn into a column]
	"""
	def __init__(self, filename, numSkippedRows = 0, numFooterRows = 0, cols = None, colsToRows = None):
		self.filename = filename
		self.file = open(filename)
		self.csvReader = csv.reader(self.file)
		self.data = []
		self.cols = cols

		# If we need to skip rows at the bottom, we must know the length beforehand
		fileLength = 0
		if numFooterRows != 0:
			with open(filename) as f:
				fileLength = sum(1 for line in f)
		
		# Loop through csv
		for rowNum, row in enumerate(self.csvReader, start = 1):
			# Skip the row
			if numSkippedRows >= rowNum or (numFooterRows != 0 and fileLength-numFooterRows <= rowNum):
				continue

			# We need to convert certain columns into rows
			if colsToRows != None:
				dataRow = [row[index-1] for index in [col[0] for col in self.cols]]
				colsToRowsData = []

				for index, item in enumerate(row, start = 1):
					if index in [col[0] for col in colsToRows["cols"]]:
						colsToRowsData.append((index, item))
				
				for colNum, colData in colsToRowsData:
					newDataRow = dataRow.copy()
					newDataRow.append(list(filter(lambda x: x[0] == colNum, colsToRows["cols"]))[0][1])
					newDataRow.append(colData)
					self.data.append(newDataRow)
				
				continue

			# Normal data row - append to data
			if cols == None:
				self.data.append(row)
			# Select only the necessary columns
			else:
				self.data.append([row[index-1] for index in [col[0] for col in self.cols]])

		if colsToRows != None:
				if self.cols == None:
					self.cols = []
				self.cols.append((len(self.cols)+1, colsToRows["colName"]))
				self.cols.append((len(self.cols)+1, colsToRows["dataColName"]))
	
	"""
	Saves each tab of an excel file as a separate csv

	args:
		excelFile (str): The file path and extension of the excel file
	"""
	@staticmethod
	def saveExcelFileAsCsv(excelFile):
		workbook = openpyxl.load_workbook(excelFile)
		newFolderName = os.path.splitext(excelFile)[0] + "/"
		os.mkdir(newFolderName)
		for sheetName in workbook.sheetnames:
			worksheet = workbook.get_sheet_by_name(sheetName)
			file = open(newFolderName + "".join(x for x in sheetName if x.isalnum() or x == ' ') + ".csv", "w", newline='')
			csvWriter = csv.writer(file)
			csvWriter.writerows(worksheet.values)

	"""
	Gets the index of a column given the column name in the dataset

	args:
		colName (str): The column name to find the index of
	"""
	def __getitem__(self, colName):
		# Cols was not set - we cannot retrieve the column name
		if self.cols == None:
			raise Exception("Data Cleaner was never given the column names")
		
		for index, col in enumerate(self.cols):
			if col[1] == colName:
				return index

		raise Exception("Could not find column named `" + colName + "`")
	
	"""
	Filters the dataset given a lambda to run on each row to check whether or not the data passes the conditions.

	args:
		conditionLambda ((row) -> bool): A lambda to filter whether or not to include a given row
	"""
	def filter(self, conditionLambda):
		self.data = list(filter(conditionLambda, self.data))
		pass
	
	"""
	Maps occurrences to values (ie code every 0 as 1, every 1 as 2, etc)

	args:
		col (int): The index of the column to map
		mapValues (dictionary<string, string>): The values to map, the key of each dictionary entry
			must be the value to find, and the value of the dictionary must be the value to map to.
	"""
	def map(self, col, mapValues):
		mapVals = lambda x: mapValues[x] if x in mapValues.keys() else x
		for index, row in enumerate(self.data):
			self.data[index][col] = mapVals(row[col])

	"""
	Removes all commas from a certain column (Good for datasets which have numerical data with commas in them)

	args:
		col (int): The index of the column to remove
	"""
	def removeCommas(self, col):
		for index, row in enumerate(self.data):
			self.data[index][col] = row[col].replace(',', '')

	"""
	Removes a column from the dataset

	args:
		col (int): The index of the column to remove
	"""
	def dropColumn(self, col):
		for index in range(len(self.data)):
			self.data[index].pop(col)
		
		self.cols.pop(col)
		for index in range(len(self.cols)):
			if index >= col:
				self.cols[index] = (self.cols[index][0] - 1, self.cols[index][1]) # Recreate tuple - tuples are read only
	
	"""
	Saves the cleaned data to a specific file given the filename

	args:
		filename (str): The filename of the file to save to
		includeColumnRow (bool): Whether or not to include the column titles row (OPTIONAL)
	"""
	def saveData(self, filename, includeColumnTitleRow = False):
		file = open(filename, "w", newline='')
		csvWriter = csv.writer(file)
		if includeColumnTitleRow:
			csvWriter.writerows([[col for i,col in self.cols]] + self.data)
		else:
			csvWriter.writerows(self.data)


