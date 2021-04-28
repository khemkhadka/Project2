# DTSC 2302 - Project 2
## Topic: Immigration
Group Members: Rishi Challa, Khem Khadka, Joshua Hernandez, Aryan Anerao, Beau Tate

Main R script file for analysis is located in `Project 2.r`

## Data
All data used for actual analysis is in the `CleanedData/project2CompleteDataset.csv`. Everything else was just used in cleaning. Correlates codebook is located within the `Data/` folder. We also are using stepwise regression in order to choose certain variables to keep and to remove.

## Variables
> Note: All variables and analysis was conducted on a state level

All variables listed below can be found in the file `CleanedData/project2CompleteDataset.csv`.

| Variable Name | CSV/Data Frame Variable Name | Included By Stepwise Regression? |
|---------------|------------------------------|----------------------------------|
| State | `State` | &check; |
| Year | `Year` | &check; |
| Mood Index | `mood` | &check; |
| Right to Work | `right2work` | &check; |
| Per Capital Annual Income | `pc_inc_ann` | &check; |
| State Poverty Rate | `povrate` | &check; |
| Consumer Price Index | `ccpi` | &check; |
| Evangelical Population | `evangelical_pop` | &check; |
| Non-White Population | `nonwhite` | &check; |
| Value added to Economy by Agriculture Sector | `valueofagsect` | &check; |
| U.S Region | `region` | &check; |
| Budget surplus as % of GSP | `budget_surplus_gsp` | &check; |
| Is there a unified Democratic Government? | `dem_unified` | &check; |
| Is there a unified Republican Government? | `rep_unified` | &check; |
| Percentage of Latino Legislators | `pctlatinoleg` | &check; |
| Number of Democratic Representatives | `hs_dem_in_sess` | &check; |
| Number of Republican Representatives | `hs_rep_in_sess` | &check; |
| Number of Nonmajor-Party Representatives | `hs_ind_in_sess` | &check; |
| Number of Democratic Senators | `sen_dem_in_sess` | &check; |
| Number of Republican Senators | `sen_rep_in_sess` | &check; |
| Number of Nonmajor-Party Senators | `sen_ind_in_sess` | &check; |
| Task Force Agreement | `Task.Force.Agreement` | &check; |
| Cooperation WIth Detainers | `Cooperation.With.Detainers` | &check; |
| EVerify Mandates | `EVerify.Mandates` | &check; |
| Year English Was Declared as Official Lang | `Year.English.Declared` | &check; |
| Is English Declared as the Official Lang? | `English.Declared` | &check; |
| Insurance for Unauthorized Children | `Insurance.for.Unauth.Kids` | &check; |
| Insurance for Unauthorized Adults | `Insurance.for.Unauth.Adults` | &check; |
| Food Assistance for Unauthorized Children | `Food.Assist.for.Immigrant.Kids` | &check; |
| Food Assistance for Unauthorized Adults | `Food.Assist.for.Immigrant.Adults` | &check; |

## Hypotheses

