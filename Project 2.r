# DTSC 2302 - Project 2
# Topic: Immigration
# Group Members: Rishi Challa, Khem Khadka, Joshua Hernandez, Aryan Anerao, Beau Tate
# NOTE: Information regarding variables, and hypotheses can be found in README.md

library(tidyverse)

# --------------------------------- Setup Variables ---------------------------------
# Review over these variables manually and set them when running the script

# Whether or not to merge the datasets - set to true only if CleanedData/project2CompleteDataset.csv
# does not already exist. If you do set this to true, make sure you've already ran `dataCleaning.py`
performCleaning = FALSE;

# --------------------------------- Data Cleaning ---------------------------------

# We should perform the data cleaning
if (performCleaning) {
	# Merge all the datasets together
	datasets = read.csv("CleanedData/datasets.csv") # Contains a list of all datasets required to be merged

	# First get the correlates data
	dataset = read.csv("Data/Project2CorrelatesData.csv")

	# Remove all columns except the following who's variables we will use:
	correlateCols = c("year", "state", "mood", "right2work", "pc_inc_ann", "povrate", "ccpi", "evangelical_pop", "nonwhite", "valueofagsect",
		"region", "budget_surplus_gsp", "dem_unified", "rep_unified", "pctlatinoleg", "hs_dem_in_sess", "hs_rep_in_sess",
		"hs_ind_in_sess", "sen_dem_in_sess", "sen_rep_in_sess", "sen_ind_in_sess")

	dataset = dataset[correlateCols]

	# Rename the correlates year and state columns since correlates uses a different naming scheme
	names(dataset)[names(dataset) == "year"] <- "Year"
	names(dataset)[names(dataset) == "state"] <- "State"

	# Loop through and merge all the datasets from the filenames
	for (filename in datasets$Filename) {
		dataset = merge(dataset, read.csv(filename), by = c("State", "Year"))
	}

	# Save the completed merged dataset as a separate csv
	write.csv(dataset, file = "CleanedData/project2CompleteDataset.csv", row.names = FALSE)
} else {
	# Cleaning has already been performed, just read in the already cleaned file
	dataset = read.csv("CleanedData/project2CompleteDataset.csv");
}

# --------------------------------- Stepwise Regression ---------------------------------



# --------------------------------- Analysis ---------------------------------

