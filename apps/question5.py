# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 04:32:08 2017

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
final_data = (data.groupby(['YEAR','LocationDesc'])['Sample_Size'].agg(['sum']))
final_data.to_csv('./data/question5.csv', sep = ',', encoding='utf-8')
qn5data = pd.read_csv('./data/question5.csv')
years = list(qn5data['YEAR'].unique())
state_names = list(qn5data['LocationDesc'].unique())


layout = html.Div(children=[

    html.Div([
            dcc.Dropdown(
                id='years1',
                options=[{'label': i, 'value': i} for i in years],
                value=1999
            ),
            dcc.Dropdown(
                id='years2',
                options=[{'label': i, 'value': i} for i in years],
                value=2013
            ),

        ],

        style={'margin-top': '20','width':'70%'}
        ), 

     html.Div([
            dcc.Graph(id='last-line-chart'),
            ],style={'display': 'full', 'width': '100%'}),


])

@app.callback(
    dash.dependencies.Output('last-line-chart', 'figure'),
    [dash.dependencies.Input('years1', 'value'),
    dash.dependencies.Input('years2', 'value')])

def update_bar_chart(yearvalue1,yearvalue2):
     """
     Forms a Staced Bar Chart
     
     Keyword Arguments:
     statename1 -- Gets the first state name to compare
     statename2 -- Gets the second state name to compare
     The values of the states are fetched and compared using a stacked Bar chart
     List Operation - Functions -  PandasDataFrame Operations Implemented
     """
#     new_list = []
#     x = 0
#     for i in qn5data['LocationDesc']:
#         if i == "Alabama":
#             new_list.append(qn5data['sum'])
        
             
             
             
     value_list1 = list(qn5data['sum'][(qn5data['YEAR'] == yearvalue1)])
     print(value_list1)
     value_list2 = list(qn5data['sum'][(qn5data['YEAR'] == yearvalue2)])
     name_list1 = list(qn5data['LocationDesc'][(qn5data['YEAR'] == yearvalue1)])
     name_list2 = list(qn5data['LocationDesc'][(qn5data['YEAR'] == yearvalue2)])
     
     return {
                    'data': ([
                            {'x': name_list1, 'y': value_list1, 'type': 'line', 'name': yearvalue1},
                            {'x': name_list1, 'y': value_list2, 'type': 'line', 'name': yearvalue2},
                            ]),
                    'layout': go.Layout(
                            title = "Smoking Trend Comparison Between the years",
                            xaxis={'title': 'Years'},
                            yaxis={'title': 'Count of Smokers'}),
                
           }   
           
       





















