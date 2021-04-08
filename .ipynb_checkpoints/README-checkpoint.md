# Group Project 5

**By Isaiah Westphalen, Daniel McBride, Tony Tedesco, Shweta Agrawal**
<br>
*DSIR 2-8*

---

## Background



---

## Problem Statement



---

## Contents:

- [The Data](#The-Data)
- [Jupyter Lab Notebook Files](#Jupyter-Lab-Notebook-Files)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Modeling](#Modeling)
- [Application](#Application)
- [Conclusion](#Conclusion)

---

## The Data

[complete_final_data.csv](data/complete_final_data.csv) - This dataset contains a sample of 554 rows of monthly data with 30 feature columns.
<br><br>


### ***Data dictionary***

|Feature|Type|Dataset|Description|Url|
|---|---|---|---|---|
| avg_weeks_unemployed | *float* | complete_final_data.csv | Average Weeks Unemployed (Units: Number of Weeks, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMPMEAN |
| cont_claims_insur_unemploy | *float* | complete_final_data.csv | Continued Claims - Insured Unemployment (Units: Number Count, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CCSA#0 |
| full_employ_level | *float* | complete_final_data.csv | Employment Level - Full-Time, All Industries (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CE16OV |
| part_employ_level | *float* | complete_final_data.csv | Employment Level - Part-Time for Economic Reasons, All Industries (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS12032194 |
| not_in_labor_force | *float* | complete_final_data.csv | Not in Labor Force (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS15000000 |
| gov_unemp_insur | *float* | complete_final_data.csv | Government social benefits to persons: Unemployment insurance (Units: Billions of Dollars, Seasonally Adjusted Annual Rate) | https://fred.stlouisfed.org/series/W825RC1 |
| labor_particip_women | *float* | complete_final_data.csv | Labor Force Participation Rate - Women (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS11300002 |
| labor_particip_men | *float* | complete_final_data.csv | Labor Force Participation Rate - Men (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS11300001 |
| labor_particip_total | *float* | complete_final_data.csv | Total Labor Force Participation Rate (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CIVPART |
| real_estate_loans | *float* | complete_final_data.csv | Real Estate Loans, All Commercial Banks (Units: Billions of U.S. Dollars, Seasonally Adjusted) | https://fred.stlouisfed.org/series/REALLN |
| consumer_loans | *float* | complete_final_data.csv | Consumer Loans, All Commercial Banks (Units: Billions of U.S. Dollars, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CONSUMER |
| commerc_indust_loans | *float* | complete_final_data.csv | Commercial and Industrial Loans, All Commercial Banks (Units: Billions of U.S. Dollars, Seasonally Adjusted) | https://fred.stlouisfed.org/series/BUSLOANS |
| m1_real | *float* | complete_final_data.csv | Real M1 Money Stock (Units: Billions of 1982-84 Dollars, Seasonally Adjusted) | https://fred.stlouisfed.org/series/M1REAL |
| unemp_less_5_wks | *float* | complete_final_data.csv | Number Unemployed for Less Than 5 Weeks (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMPLT5 |
| unemp_5_to_14_wks | *float* | complete_final_data.csv | Number Unemployed for 5-14 Weeks (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMP5TO14 |
| unemp_15_to_26_wks | *float* | complete_final_data.csv | Number Unemployed for 15-26 Weeks (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMP15T26 |
| unemp_over_27_wks | *float* | complete_final_data.csv | Number Unemployed for 27 Weeks & Over (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMP27OV |
| personal_consum_exp | *float* | complete_final_data.csv | Personal Consumption Expenditures (Units: Billions of Dollars, Seasonally Adjusted Annual Rate) | https://fred.stlouisfed.org/series/PCE |
| personal_save_rate | *float* | complete_final_data.csv | Personal Saving Rate (Units: Percent, Seasonally Adjusted Annual Rate) | https://fred.stlouisfed.org/series/PSAVERT |
| emp_pop_ratio | *float* | complete_final_data.csv | Employment-Population Ratio (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/EMRATIO |
| unemploy_rate | *float* | complete_final_data.csv | Unemployment Rate (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UNRATE |
| insured_unemploy_rate | *float* | complete_final_data.csv | Insured Unemployment Rate (Units: Percent, Seasonally Adjusted) | https://fred.stlouisfed.org/series/IURSA |
| target_retail | *float* | complete_final_data.csv | All Employees, Retail Trade (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USTRADE#0 |
| target_mining_logging | *integer* | complete_final_data.csv | All Employees, Mining and Logging (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USMINE |
| target_construction | *integer* | complete_final_data.csv | All Employees, Construction (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USCONS |
| target_edu_health | *integer* | complete_final_data.csv | All Employees, Education and Health Services (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USEHS |
| target_manufacturing | *integer* | complete_final_data.csv | All Employees, Manufacturing (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/MANEMP |
| target_prof_business | *integer* | complete_final_data.csv | All Employees, Professional and Business Services (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USPBS |
| target_gov | *integer* | complete_final_data.csv | All Employees, Government (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USGOVT |
| target_leisure_hospitality | *integer* | complete_final_data.csv | All Employees, Leisure and Hospitality (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/USLAH |

---

## Jupyter Lab Notebook Files

[Data Cleaning Notebook File](Untitled.ipynb)
<br>
[EDA & Visualization Notebook File](Untitled.ipynb)
<br>
[Modeling Notebook File](Untitled.ipynb)

---

## Exploratory Data Analysis

N/A

---

## Modeling

N/A

---

## Application

N/A

---

## Conclusion

N/A