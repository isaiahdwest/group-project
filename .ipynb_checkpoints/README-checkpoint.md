# Group Project 5

**By Isaiah Westphalen, Daniel McBride, Tony Tedesco, Shweta Agrawal**
<br>
*DSIR 2-8*

---

## Background & Problem Statement

It's not surprising to know the Covid-19 pandemic has effected almost every single aspect of existence for individuals, businesses, and governments around the globe.  More specifically, the levels of employment in nearly every single job market has taken massive hits due to layoffs, illness, and business closures, causing major disruptions to profits but also, most importantly, our well-being.

The future is indeed still uncertain, but history can also enlighten us on how we can move forward.

Whether you are an established business leader or have the potential to be one in the future, we have devised a special place to help assist you with your decision making for not only your business' success but also for the benefit of your employees.

With that being said, our team decided to embark on a journey to discover how we can peer in to the future and determine how employment levels in various job markets will recover or further suffer from the pandemic as more and more vaccines go out to hopefully help bring us back to some sense of normalcy once again.

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

> Data sourced from: https://fred.stlouisfed.org/

[complete_final_data.csv](data/complete_final_data.csv) - This dataset contains a sample of 554 rows of monthly data with 30 feature columns.
<br>
<br>

### ***Data dictionary***

[Click here for Full Data Dictionary](data_dict.md)

*Data Dictionary Sample...*

|Feature|Type|Dataset|Description|Url|
|---|---|---|---|---|
| avg_weeks_unemployed | *float* | complete_final_data.csv | Average Weeks Unemployed (Units: Number of Weeks, Seasonally Adjusted) | https://fred.stlouisfed.org/series/UEMPMEAN |
| cont_claims_insur_unemploy | *float* | complete_final_data.csv | Continued Claims - Insured Unemployment (Units: Number Count, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CCSA#0 |
| full_employ_level | *float* | complete_final_data.csv | Employment Level - Full-Time, All Industries (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/CE16OV |
| part_employ_level | *float* | complete_final_data.csv | Employment Level - Part-Time for Economic Reasons, All Industries (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS12032194 |
| not_in_labor_force | *float* | complete_final_data.csv | Not in Labor Force (Units: Thousands of Persons, Seasonally Adjusted) | https://fred.stlouisfed.org/series/LNS15000000 |
| ... | ... | ... | ... | ... |

---

## Jupyter Lab Notebook Files

[Monthly Data Cleaning Notebook File](code/cleaning_month_data.ipynb)
<br>
[Target Data Cleaning Notebook File](code/cleaning_target_data.ipynb)
<br>
[Merged Data Cleaning Notebook File](code/cleaning_merged_month_target.ipynb)
<br>
<br>
[EDA & Visualization Notebook File](code/EDA_GroupProject_Shweta.ipynb)
<br>
<br>
[Modeling Notebook File](code/Final_model.ipynb)

---

## Exploratory Data Analysis

To gain a deeper understanding of our data, we developed some visualizations to actually see how our data has changed over time and how certain features related to each other.  The extraordinarily brilliant Shweta took charge utilizing Tableau for our exploratory data analysis.

---

## Modeling

After exploring our data and determining our goals, we decided that a Time Series model would align with our objectives the best.  The incredibly talented Tony Tedesco headed up our modeling efforts with the discovery of the Vector Autoregression model, that would allow us have a multivariate output as opposed to a univariate output.  This would allow us pull out forecasts for all 8 of our targets with one model, saving us from creating 8 different models for each variable.

Once the model is fitted on our endogenous and exogenous data, we are able to specify the amount of time we want to forecast into the future, also known as our steps.  Because our data was originally filtered monthly, each step indicates one month into the future.  After playing with the code a little bit, we can actually visualize our forecasted predictions for each target category with ease.

---

## Application

Now that we had a working model, we discussed how best we could package this model to our audience in an interactive and interpretable way.  With the unrivaled genius of Isaiah leading the charge, we were able to build out our web app utilizing Flask, a web framework written in python that can utilize code along with html, css, and javascript for design and functionality of our application.

We created a private web app for business leaders to better understand both the historical trends of how employment levels have changeed in some major job markets as well as look in to the crystal ball and see how those same employment levels will shift up or down based on what has come before.  We believe it is important to understand how these job markets will not only shape our economic future, but also the future of those hit with occupational hardships recently and are looking for a path that moves them past and beyond.

Our web app explores specific job markets, such as retail, construction, or mining, where you can visually see how employment levels have fluxuated in the past.  Here you will notice how historical events, such as market crashes, recessions, and even global pandemics have shaped the day to day lives of both employees and employers.  Using our machine learning model, you can also see how those employment levels are forecasted to change in the future by the numbers and by the percent rate of change, both if the coronavirus potentially never existed and also taking in to account the major disruption caused by Covid-19.

In order to make our web app accessible to anyone around the globe in the future, we plan to use Heroku, which is a platform as a service that enables developers to build, run, and operate applications entirely in the cloud.  This allows our model to exist in an online space while still allowing us to make updates, upgrades, or debug at anytime in real time.


---

## Conclusion

Covid-19 has been an unexpected outlier in both our data and our daily lives.  We did decided to also truncated our data to omit the turbulence caused by the pandemic, primarily out of our own curiosity, to see how our forecasts would react.  We determined that even with the majority of the data breaking most trend lines around March of 2020, our model still performed as a good indicator of the future.

We would like to further refine our application by testing out different types of models and their potential outputs, such as the potential implementation of neural networks.  Also, creating a scheduled, automated ETL data pipeline to bring in new data as it becomes available can help ensure the future functionality of our application by consistently bringing that new data into the model.

The natural passage of time will ultimately be the best test of our performance, but we hope that with the forecasted findings created by our model and the accessibility to you through our web app for which ever field of business you seek to thrive in, you can gain better insight into the business decisions you make and direction you take for any specific point in your future.  Specifically, if you are in the market of construction, education, hospitality, or business services, then you can expect an increase in employment levels to meet the demands of your markets respectively, while the mining, logging, and manufacturing markets are projected to see a decrease in employment levels, prompting more conservative spending and business practices.  This is particularly true when it comes to recovering from the disruption caused by Covid-19 and helping to get individuals back to work and building our futures together again.