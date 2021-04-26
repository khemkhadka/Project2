# DTSC 2302 - Project 2
# Topic: Immigration
# Group Members: Rishi Challa, Khem Khadka, Joshua Hernandez, Aryan Anerao, Beau Tate

library(tidyverse)

# --------------------------------- Data Cleaning ---------------------------------

# Merge all the datasets together
datasets = read.csv("CleanedData/datasets.csv") # Contains a list of all datasets required to be merged

# First get the correlates data
mergedData = read.csv("Data/Project2CorrelatesData.csv")

# Rename the correlates year and state columns since correlates uses a different naming scheme
names(mergedData)[names(mergedData) == "year"] <- "Year"
names(mergedData)[names(mergedData) == "state"] <- "State"

# Loop through and merge all the datasets from the filenames
for (filename in datasets$Filename) {
	mergedData = merge(mergedData, read.csv(filename), by = c("State", "Year"))
}

# Save the completed merged dataset as a separate csv
write.csv(mergedData, file = "CleanedData/project2CompleteDataset.csv", row.names = FALSE)

# --------------------------------- Hypotheses ---------------------------------


# --------------------------------- Analysis ---------------------------------

