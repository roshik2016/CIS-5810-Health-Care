# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:51:14 2017

@author: roshi
"""
""" Using Pandas DataFrame"""
import pandas as pd 
""" Using Numpy Array"""
import numpy as np

data = pd.read_csv('./data/Youth_Tobacco_Survey__YTS__Data.csv')

"""
Data Cleaning 1

Misfed Rows cleanup.
Removes rows where there is improper data value
"""
data = data[data.Data_Value_Footnote_Symbol != "*"]

""" 
Data Cleaning 2

Removing Unwanted Columns.
"""
data = data.drop(['Data_Value_Footnote','DataSource', 'Data_Value_Unit','TopicType','Data_Value_Footnote','Data_Value_Footnote_Symbol'],axis = 1)

"""
Data Cleaning 3

Checking and Removing Null values
"""
data = data.dropna(subset=['Data_Value','GeoLocation','Sample_Size'])

"""
Data Cleaning 4

Changing names of Improperly Named columns.
"""
new_data = data.rename(columns = {'Data_Value':'Data_Value_Rate'})
"""
Data Cleaning 5

Splitting Latitude and Longitute into 2 columns.
String Operations Used to Strip
List Operations Used
"""
lat = []
lon = []
new_data['GeoLocation'] = new_data['GeoLocation'].str.strip('()')
for row in new_data['GeoLocation']:
    # Try to,
    try:
        # Split the row by comma and append
        # everything before the comma to lat
        lat.append(row.split(',')[0])
        # Split the row by comma and append
        # everything after the comma to lon
        lon.append(row.split(',')[1])
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

new_data['latitude'] = lat
new_data['latitude'] = new_data['latitude'].astype(float)
new_data['longitude'] = lon
new_data['longitude'] = new_data['longitude'].astype(float)


new_data.to_csv('./data/youth_tobacco_analysis.csv', sep = ',', encoding='utf-8')


