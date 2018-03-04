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
final_data = pd.DataFrame(data.groupby(['YEAR','LocationDesc']).count())
final_data.to_csv('./data/question2.csv', sep = ',', encoding='utf-8')
qn2data = pd.read_csv('./data/question2.csv')
qn2data['LocationDesc'] = qn2data['LocationDesc'].str.upper() 

x=0
state_names = list(qn2data['LocationDesc'].unique())
"""
String Operation to Convert the string in each column to upper case is used.
It is used as the columns names are inconsistant with the casing
"""
for i in state_names:
    state_names[x] = state_names[x].upper()
    x=x+1
years = list(qn2data['YEAR'].unique())
layout = html.Div(children=[
    
    html.Div([
            dcc.Dropdown(
                id='state_names',
                options=[{'label': i, 'value': i} for i in state_names],
                value='ARIZONA'    
            ),

        ],
        style={'width': '30%', 'display': 'inline-block'}),

     html.Div([
            dcc.Graph(id='line-chart'),
            ],style={'width': '49%'}),


])

@app.callback(
    dash.dependencies.Output('line-chart', 'figure'),
    [dash.dependencies.Input('state_names', 'value')])

def update_bar_chart(statename1):
     """
     Forms a Staced Bar Chart
     
     Keyword Arguments:
     statename1 -- Gets the first state name to compare
     The values of the states are fetched and compared using a line chart for the trend analysis
     Functions -  PandasDataFrame Operations Implemented
     """
         
     value_list = list(qn2data['LocationAbbr'][(qn2data['LocationDesc'] == statename1)])
     xvalues = list(qn2data['YEAR'][(qn2data['LocationDesc'] == statename1)])
     return {
                    'data': ([
                            {'x':xvalues , 'y': value_list, 'type': 'line', 'name': 'NB'},
                            ]),
                    'layout': go.Layout(
                            title = "Smoking Status Comarison by States",
                            xaxis={'title': 'Somking Status of Youth'},
                            yaxis={'title': 'Count of Youth Over the Years'}),
                
           }   
           
       





















