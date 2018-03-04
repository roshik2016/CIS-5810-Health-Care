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
final_data = pd.DataFrame(data.groupby(['LocationDesc','MeasureDesc']).count())
final_data.to_csv('./data/question1.csv', sep = ',', encoding='utf-8')
qn1data = pd.read_csv('./data/question1.csv')

state_names = list(qn1data['LocationDesc'].unique())
layout = html.Div(children=[
    
    html.Div([
            dcc.Dropdown(
                id='state_names',
                options=[{'label': i, 'value': i} for i in state_names],
                value='Arizona'    
            ),
            dcc.Dropdown(
                id='state_names2',
                options=[{'label': i, 'value': i} for i in state_names],
                value='Connecticut'    
            ),
        ],
        style={'width': '30%', 'display': 'inline-block'}),

     html.Div([
            dcc.Graph(id='simple-bar'),
            ],style={ 'width': '49%'}),


])

@app.callback(
    dash.dependencies.Output('simple-bar', 'figure'),
    [dash.dependencies.Input('state_names', 'value'),
     dash.dependencies.Input('state_names2', 'value')])

def update_bar_chart(statename1,statename2):
     """
     Forms a Stacked Bar Chart
     
     Keyword Arguments:
     statename1 -- Gets the first state name to compare
     statename2 -- Gets the second state name to compare
     The values of the states are fetched and compared using a stacked Bar chart
     List Operation - Functions -  PandasDataFrame - Dict Used Operations Implemented
     """
     value_list = list(qn1data['YEAR'][(qn1data['LocationDesc'] == statename1)])
     name_list = list(qn1data['MeasureDesc'][(qn1data['LocationDesc'] == statename1)])
     value_list2 = list(qn1data['YEAR'][(qn1data['LocationDesc'] == statename2)])
     name_list2 = list(qn1data['MeasureDesc'][(qn1data['LocationDesc'] == statename2)])

     return {
                    'data': ([
                            {'x': name_list, 'y': value_list, 'type': 'bar', 'name': statename1},
                            {'x': name_list2, 'y': value_list2, 'type': 'bar', 'name': statename2},
                            ]),
                    'layout': go.Layout(
                            title = "Smoking Status Comarison by States",
                            xaxis={'title': 'Somking Status of Youth'},
                            yaxis={'title': 'Count of Youth Over the Years'}),
                
           }   
           
       





















