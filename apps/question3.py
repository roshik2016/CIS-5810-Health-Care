# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:56:43 2017

@author: roshi
"""

import pandas as pd
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from app import app

data = pd.read_csv('./data/youth_tobacco_analysis.csv')
"""Pandas DataFrame Implemented"""
final_data = pd.DataFrame(data.groupby(['YEAR','Education']).count())
#final_data.to_csv('./data/question3.csv', sep = ',', encoding='utf-8')
qn3data = pd.read_csv('./data/question3.csv')

years = list(qn3data['YEAR'].unique())

layout = html.Div(children=[
    
    html.Div([
            dcc.Dropdown(
                id='years',
                options=[{'label': i, 'value': i} for i in years],
                value=2000
            ),

        ],
        style={'width': '30%', 'display': 'inline-block'}),

     html.Div([
            dcc.Graph(id='pie-chart'),
            ],style={'width': '49%'}),


])

@app.callback(
    dash.dependencies.Output('pie-chart', 'figure'),
    [dash.dependencies.Input('years', 'value')])

def update_bar_chart(yearvalue):
     """
     Forms a Pie Bar Chart
     
     Keyword Arguments:
     statename1 -- Gets the first state name to compare
     The values of the states are fetched and compared using a line chart for the trend analysis
     Functions -  Tuples Implemented
     """
     title_pie_Chart = ("Middle School - High School Comparison")
     labels_pie_chart = ("High School","Middle School")
     value_1 = qn3data['LocationAbbr'][(qn3data['YEAR'] == yearvalue) & (qn3data['Education'] == "High School") ]
     value1 = int(value_1)
     value_2 = qn3data['LocationAbbr'][(qn3data['YEAR'] == yearvalue) & (qn3data['Education'] == "Middle School") ]
     value2 = int(value_2)
     return {
                    'data': [go.Pie(labels=labels_pie_chart, values=[value1,value2])],
                        'layout': {
                                'title': title_pie_Chart
                                }
                                }
                
           
       




















