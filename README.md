# Group Project 5

**By Isaiah Westphalen, Daniel McBride, Tony Tedesco, Shweta Agrawal**
<br>
*DSIR 2-8*

---

## Background & Problem Statement

Whether you are an established business leader or have the potential to be one in the future, we have devised a special place to help assist you with your decision making for not only your business' success but also for the benefit of your employees.

It's not surprising to know the Covid-19 pandemic has effected almost every single aspect of existence for individuals, businesses, and governments around the globe.  More specifically, the levels of employment in nearly every single job market has taken massive hits due to layoffs, illness, and business closures, causing major disruptions to profits but also, most importantly, our well-being.

The future is indeed still uncertain, but history can also enlighten us on how we can move forward.

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

[complete_final_data.csv](alt_data/complete_final_data.csv) - This dataset contains a sample of 554 rows of monthly data with 30 feature columns.
<br><br>


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
[Merged Data Cleaning Notebook File](code/eda_merged_monthly_targets.ipynb)
<br>
<br>
[EDA & Visualization Notebook File](code/eda.ipynb)
<br>
<br>
[Modeling Notebook File](code/model.ipynb)

---

## Exploratory Data Analysis

To gain a deeper understanding of our data, we developed some visualizations to actually see how our data has changed over time and how certain features related to each other.  The extraordinarily brilliant Shweta took charge utilizing Tableau for our exploratory data analysis.



In one example, U.S. government paid out unemployment benefits of roughly 1.4 trillion in March of 2020.  The recession of 2008 in comparison only saw a payout of roughly 200 billion.  At the same time in March of 2020, the unemployment rate went to an all time of around 15% but shortly came down to roughly 6% afterwards.



Retail has had a fairly decent recovery following March 2020 while leisure and hospitality, which saw around a 50% drop in employment levels, is still struggling to return to a familiar trend in employment levels at a time before March of 2020.



Mining and logging saw a peak in employment levels way back in the early to mid 80s but has not seen that kind of employment since then, with only a slight boom coming after the 2008 recession.  The road to recovery after Covid-19 does not seem to be trending very well either.  Manufacturing seemed to be pretty consistent up until the early 2000s, in which a significant drop in employment levels has been prevalent since then, regardless of the effects of the pandemic.



Our final visual shows our remaining target categories that we will be forecasting, all of which follow a similar upward trend with slight disruptions to employment levels occuring at roughly the same point in time.

---

## Modeling

After exploring our data and determining our goals, we decided that a Time Series model would align with our objectives the best.  The incredibly talented Tony Tedesco headed up our modeling efforts with the discovery of the Vector Autoregression model, that would allow us have a multivariate output as opposed to a univariate output.  This would allow us pull out forecasts for all 8 of our targets with one model, saving us from creating 8 different models for each variable.

Once the model is fitted on our endogenous and exogenous data, we are able to specify the amount of time we want to forecast into the future, also known as our steps.  Because our data was originally filtered monthly, each step indicates one month into the future.  After playing with the code a little bit, we can actually visualize our forecasted predictions for each target category with ease.

Being a regression model, we utilized mean squared error as our metric to determine how well our model was potentially performing at predicting the future.

---

## Application

We created a online destination accessible to anyone to better understand both the historical trends of how employment levels have changeed in some major job markets as well as look in to the crystal ball and see how those same employment levels will shift up or down based on what has come before.  We believe it is important to understand what these job markets will not only shape our economic future, but also the future of those hit with occupational hardships recently and are looking for a path that moves them past and beyond.

With the unrivaled genius of Isaiah leading the charge, we were able to build out our web app utilizing Flask, a web framework written in python that can utilize code along with html, css, and javascript for design and functionality of our application.

In order to make our web app accessible to anyone around the globe, we used Heroku, which is a platform as a service that enables developers to build, run, and operate applications entirely in the cloud.  This allows our model to exist in an online space while still allowing us to make updates, upgrades, or debug at anytime in real time.

You can access our page right now and explore a specific job market, such as retail, construction, or mining, and visually see how employment levels have fluxuated in the past, either by an actual number of employees per job market or the month by month rate of change in employment levels.  Here you can notice how historical events, such as market crashes, recessions, and even global pandemics have shaped the day to day lives of both employees and employers.  Using a machine learning model, you can also see how those employment levels are forecasted to change in the future, both if the coronavirus potentially never existed and also taking in to account the major disruption caused by Covid-19.



---

## Conclusion

Covid-19 has been an unexpected outlier in both our data and our daily lives.  We did decided to also truncated our data to omit the turbulence caused by the pandemic, primarily out of our own curiosity, to see how our forecasts would react.  We determined that even with the majority of the data breaking most trend lines around March of 2020, our model still performed as a good indicator of the future.

We would like to further refine our application by testing out different types of models and their potential outputs, such as the potential implementation of neural networks.  Also, creating a scheduled, automated ETL data pipeline to bring in new data as it becomes available can help ensure the future functionality of our application by consistently bringing that new data into the model.

The natural passage of time will ultimately be the best test of our performance, but we hope that with the forecasted findings created by our model and the accessibility to you through our web app for which ever field of business you seek to thrive in, you can gain better insight into the business decisions you make and direction you take for any specific point in your future, particularly when it comes to recovering from the disruption caused by Covid-19 and helping to get individuals back to work and building our futures together again.