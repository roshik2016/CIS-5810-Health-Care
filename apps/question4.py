# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 03:45:51 2017

@author: roshi
"""

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
final_data = (data.groupby(['YEAR','Gender'])['Sample_Size'].agg(['sum','count']))
final_data.to_csv('./data/question4.csv', sep = ',', encoding='utf-8')
qn1data = pd.read_csv('./data/question4.csv')

layout = html.Div(children=[

     html.Div([
           dcc.RadioItems(
                id='gender-type',
                options=[{'label': i, 'value': i} for i in ['Male', 'Female']],
                value='Male',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '100%','align':'centre'}),

     html.Div([
            dcc.Graph(id='bar-line-chart'),
            ],style={'display': 'full', 'width': '100%'}),


])

@app.callback(
    dash.dependencies.Output('bar-line-chart', 'figure'),
    [dash.dependencies.Input('gender-type', 'value')])

def update_bar_chart(gendername):
     """
     Forms a Staced Bar Chart
     
     Keyword Arguments:
     statename1 -- Gets the first state name to compare
     statename2 -- Gets the second state name to compare
     The values of the states are fetched and compared using a stacked Bar chart
     List Operation - Functions -  PandasDataFrame Operations Implemented
     """
     value_list = list(qn1data['sum'][(qn1data['Gender'] == gendername)])
     name_list = list(qn1data['YEAR'][(qn1data['Gender'] == gendername)])
     overall_value = list(qn1data['sum'][(qn1data['Gender'] == "Overall")])
     
     return {
                    'data': ([
                            {'x': name_list, 'y': overall_value, 'type': 'bar', 'name': 'Overall'},
                            {'x': name_list, 'y': value_list, 'type': 'line', 'name': gendername},
                            ]),
                    'layout': go.Layout(
                            title = "Male / Female Comparison to Overall Youth Smokers",
                            xaxis={'title': 'Years'},
                            yaxis={'title': 'Count of Smokers'}),
                
           }   
           
       





















