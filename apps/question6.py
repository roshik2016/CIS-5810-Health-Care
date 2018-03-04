# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:17:22 2017

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
years = list(data['YEAR'].unique())
state_names = list(data['LocationDesc'].unique())


#app = dash.Dash()

layout = html.Div(
        [
    html.Div([
            dcc.Dropdown(
                id='years1',
                options=[{'label': i, 'value': i} for i in years],
                value=2000
            ),

        ],style={'width': '20%', 'display': 'inline-block'}),

    html.Div([
            dcc.Dropdown(
                id='state_names',
                value= "Arizona",
            )],style={'width': '20%', 'display': 'inline-block'}), 

     html.Div(id='table_chart'),

     html.Div([
            dcc.Graph(id='scatter-chart'),
            ],style={'display': 'full', 'width': '49%'}),

     


])

@app.callback(
    dash.dependencies.Output('state_names', 'options'),
    [dash.dependencies.Input('years1', 'value')])
def update_date_dropdown(yearvalue):
    """
    Populates the second dropdown
    Keyword Arguments:
    yearvalue -- Gets the value of the year to populate the child dropdown
    The specific values of each year is populated based on the year selected by the user
    """
    
    xvalue_list = data['LocationDesc'][(data['YEAR'] == yearvalue)]
    xvalue_list = xvalue_list.unique()
    return [{'label': i, 'value': i} for i in xvalue_list]

@app.callback(
    dash.dependencies.Output('scatter-chart', 'figure'),
    [dash.dependencies.Input('years1', 'value'),
    dash.dependencies.Input('state_names', 'value')])
def update_figure(yearvalue,statenames):
    """
    Forms a Scatter plot
    Keyword Arguments:
    yearvalue -- Gets the value of the year to be analyzed
    statenames -- Gets the value state to be analyzed
    The values of the states are fetched and compared using a stacked Bar chart
    List Operation - Functions -  PandasDataFrame Operations Implemented
    """
    
    xvalue_list = data['Low_Confidence_Limit'][(data['YEAR'] == yearvalue) & (data['LocationDesc'] == statenames)]
    yvalue_list = data['High_Confidence_Limit'][(data['YEAR'] == yearvalue) & (data['LocationDesc'] == statenames)]
    name_list = data['LocationDesc'][(data['YEAR'] == yearvalue) & (data['LocationDesc'] == statenames)]
    trace = go.Scatter(
                    x=xvalue_list,
                    y=yvalue_list,
                    text = name_list,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 10,
                        'line': {'width': 0.4, 'color': 'white'}
                    },
                ) 
    
    return {
        'data': [trace],
        'layout': go.Layout(dict(
            title = 'High Confidence and Low Confidence Comparison',
            xaxis={'title': 'Low Confidence Limit'},
            yaxis={'title': 'High Confidence Limit'}),
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }

@app.callback(
    dash.dependencies.Output('table_chart', 'children'),
    [dash.dependencies.Input('years1', 'value'),
    dash.dependencies.Input('state_names', 'value')])
                        
def update_table_chart(yearvalue,statenames):
    """
    Forms a table with Mean Standard Deviation, Minimumm and Maximum values
    
    yearvalue -- Gets the value of the year to be analyzed
    statenames -- Gets the value state to be analyzed.
    A table displaying the statistical data is obtained
    """

    xvalue_list = data['Low_Confidence_Limit'][(data['YEAR'] == yearvalue) & (data['LocationDesc'] == statenames)]
    yvalue_list = data['High_Confidence_Limit'][(data['YEAR'] == yearvalue) & (data['LocationDesc'] == statenames)]
    df = pd.DataFrame({'Low_Confidence': xvalue_list,'High_Confidence' : yvalue_list})
    lcmin = df['Low_Confidence'].min()
    lcmax = df['Low_Confidence'].max()
    hcmin = df['High_Confidence'].min()
    hcmax = df['High_Confidence'].max()
    lcstd = df['Low_Confidence'].std()
    hcstd = df['High_Confidence'].std()
    lcmean = df['Low_Confidence'].mean()
    hcmean = df['High_Confidence'].mean()
    lclist = [lcmin,lcmax,lcstd,lcmean]
    hclist = [hcmin,hcmax,hcstd,hcmean]
    new_df_name = ['Minimum','Maximum','Standard Deviation','Mean']
    new_df = pd.DataFrame({'Name':new_df_name,'LowConfidence':lclist,'High Confidence':hclist})
    print(new_df)
    max_rows = 4
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in new_df.columns])] +

        # Body
        [html.Tr([
            html.Td(new_df.iloc[i][col]) for col in new_df.columns
        ]) for i in range(min(len(new_df), max_rows))]
    )
  
    
    
    