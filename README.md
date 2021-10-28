# Tridge_Assignment

## Calender
### Solution using Python

Just run Calender.py

In my case, using Windows 10 : `python Calender.py`

When you run `Calender.py`, the Instruction will be printed

Enter the start date and end date you want to explore. (YYYYMMDD)

The output includes all dates and the total number of dates satisfying the conditions. 


## Base_Converter

Just check my `Base_Converter.py`.

It contains `__convert` method and codes that I used for test


## Dataset

I think it'd be good to read it in the order that I write it down.

`Preprocess.ipynb` : Code and brief description of simple data cleansing and preprocessing.

Looking at the Dataset, it was found that the categorical attributes were the main attributes, and only the price of the date was the numerical attribute.

Since the nominal values are only the prices of each date, I think the additional values will be able to obtain additional information such as the average price of each period, the rate of increase or decrease of prices by period, and the location of the same item in the world market price.

If we proceed with the grouping, we will collect and use it for each period or purpose mainly used for data analysis or report. 

For example, if work is done frequently, such as looking at the price changes of avocados per year in a specific region on a weekly basis, I think we can take a method such as loading the average value of weekly prices by region.

Schema could be considered in several ways for isolation. `Schema.Drawio.pdf` is a file depicting Schema's example of subtracting and dealing with clearly dependent data to save storage space.

The Approach of the script that putting informations into DB, I'm not sure, I'll consider `pyspark` using some `SQL Queries`

