import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds = pd.read_csv("~/Desktop/Ai & Ml/final/California_cities.csv", index_col=['city'])

#Checking the values of central tendancies
print(ds.describe())

#Q1.Checking for null values
print(ds.isnull().sum())

#Q2.Handling missing values replacing with a measure of central tendacy
ds['elevation_m'].fillna(ds['elevation_m'].mean(), inplace=True)
ds['elevation_ft'].fillna(ds['elevation_ft'].mode()[0], inplace=True)
ds['area_total_sq_mi'].fillna(ds['area_total_sq_mi'].median(), inplace=True)
ds['area_water_sq_mi'].fillna(ds['area_water_sq_mi'].mean(), inplace=True)
ds['area_total_km2'].fillna(ds['area_total_km2'].mode()[0], inplace=True)
ds['area_land_km2'].fillna(ds['area_land_km2'].median(), inplace=True)
ds['area_water_km2'].fillna(ds['area_water_km2'].mode()[0], inplace=True)
ds['area_water_percent'].fillna(ds['area_water_percent'].mode()[0], inplace=True)

#Q2.Checking if null values are filled 
print(ds.isnull().sum())

#Q3.Get the ten lowest values of latitude and stores in a variable
lats = ds['latd'].nsmallest(10)

#Q3.Prints the mean,max.min,std & median
print(lats)
print(lats.describe())

#Q4.Get the ten lowest values of elevation in metres and stores in a variable and prints them
mita = ds['elevation_m'].nsmallest(10)
print(mita)

#Q5.Cities with top ten highest populations
top = ds['population_total'].nlargest(10)
print(top)

#Q6.Area total in km2 to population totals
sita = ds[['area_total_km2', 'population_total']].nlargest(10, 'area_total_km2')
print(sita)

#sita plot
plt.plot('area_total_km2' , 'population_total', data=sita)
plt.xlabel('Area total km2')
plt.ylabel('Population Totals')
plt.title('Question 6')
plt.legend()
plt.show()

#Q7.Top ten cities in ft to their respective population totals
saba = ds[['elevation_ft', 'population_total']].nlargest(10, 'elevation_ft')
print(saba)

#saba plot
plt.plot('elevation_ft' , 'population_total', data=saba)
plt.xlabel('Elevation')
plt.ylabel('Population Totals')
plt.title('Question 7')
plt.legend()
plt.show()

#Q8.Hist of area total sq mi
x = ds['area_total_sq_mi']
print(x)
bins = [0, 20, 40, 60, 80, 100, 120,140,160,180,200,220,240,260,280,300,320,340,360,380,400]
plt.hist(x,bins)
plt.show()

