# DTSC 2302 - Project 2
# Topic: Immigration
# Group Members: Rishi Challa, Khem Khadka, Joshua Hernandez, Aryan Anerao, Beau Tate
# NOTE: Information regarding variables, and hypotheses can be found in README.md

library(tidyverse)
library(ggthemes)
library(olsrr)
library(gganimate)

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
	correlateCols = c("year", "state", "mood", "right2work", "pc_inc_ann", "povrate", "ccpi", "evangelical_pop",
		"nonwhite", "valueofagsect", "region", "budget_surplus_gsp", "dem_unified", "rep_unified", "pctlatinoleg",
		"hs_dem_in_sess", "hs_rep_in_sess", "hs_ind_in_sess", "sen_dem_in_sess", "sen_rep_in_sess", "sen_ind_in_sess")

	dataset = dataset[correlateCols]

	# Rename the correlates year and state columns since correlates uses a different naming scheme
	names(dataset)[names(dataset) == "year"] <- "Year"
	names(dataset)[names(dataset) == "state"] <- "State"

	# Loop through and merge all the datasets from the filenames
	for (filename in datasets$Filename) {
		dataset = merge(dataset, read.csv(filename), by = c("State", "Year"))
	}

	# Sum up the dependent variables to make a compositeScore
	dataset$Immigration.Composite.Score = dataset$Task.Force.Agreement + dataset$Cooperation.With.Detainers +
		dataset$EVerify.Mandates + dataset$English.Declared + dataset$Insurance.for.Unauth.Kids +
		dataset$Insurance.for.Unauth.Adults + dataset$Food.Assist.for.Immigrant.Kids + dataset$Food.Assist.for.Immigrant.Adults

	# Save the completed merged dataset as a separate csv
	write.csv(dataset, file = "CleanedData/project2CompleteDataset.csv", row.names = FALSE)
} else {
	# Cleaning has already been performed, just read in the already cleaned file
	dataset = read.csv("CleanedData/project2CompleteDataset.csv");
}

# --------------------------------- Stepwise Regression ---------------------------------

stepwiseRegressionModel = lm(Immigration.Composite.Score ~ mood + right2work + pc_inc_ann + povrate + ccpi + 
	evangelical_pop + nonwhite + valueofagsect + region + budget_surplus_gsp + dem_unified + rep_unified +
	pctlatinoleg + hs_dem_in_sess + hs_rep_in_sess + hs_ind_in_sess + sen_dem_in_sess + sen_rep_in_sess + sen_ind_in_sess,
	data = dataset)
stepwiseRegressionResult = ols_step_both_p(stepwiseRegressionModel)
print(stepwiseRegressionResult)

"
| Step | Variable          | R-Square | Adj. R-Square | C(p)      | AIC       | RMSE   |
|------|-------------------|----------|---------------|-----------|-----------|--------|
| 1    | `evangelical_pop` | 0.191    | 0.189         | 1263.7780 | 1988.7664 | 0.9988 |
| 2    | `region`          | 0.233    | 0.231         | 1162.2700 | 1952.7828 | 0.9727 |
| 3    | `hs_rep_in_sess`  | 0.265    | 0.261         | 866.6940  | 1599.5557 | 0.9381 |
| 4    | `rep_unified`     | 0.291    | 0.287         | 816.5810  | 1579.9839 | 0.9219 |
| 5    | `valueofagsect`   | 0.300    | 0.294         | 801.3050  | 1574.6542 | 0.9169 |
| 6    | `dem_unified`     | 0.305    | 0.298         | 793.4080  | 1572.4138 | 0.9144 |
| 7    | `mood`            | 0.294    | 0.284         | 686.5870  | 1425.5100 | 0.8996 |
| 8    | `nonwhite`        | 0.299    | 0.289         | 679.1940  | 1424.3081 | 0.8970 |
"

# --------------------------------- Analysis ---------------------------------

