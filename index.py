from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import os 

from app import app
from apps import question1
from apps import question2
from apps import question3
from apps import question4
from apps import question5
from apps import question6
from apps import testapp

# header 
app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Question1', href='/question1'),
    html.Br(),
    dcc.Link('Question2', href='/question2'),
    html.Br(),
    dcc.Link('Question3', href='/question3'),
    html.Br(),
    dcc.Link('Question4', href='/question4'),
    html.Br(),
    dcc.Link('Question5', href='/question5'),
    html.Br(),
    dcc.Link('Question6', href='/question6'),
    html.Br(),
    # content will be rendered in this element
    html.Div(id='page-content')

])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    """
    Forms a Dropdown Menu.
    
    Keyword arguments:
    pathname -- input from user
    """
    if pathname == '/question1':
         return question1.layout
    elif pathname == '/question2':
         return question2.layout
    elif pathname == '/question3':
         return question3.layout
    elif pathname == '/question4':
         return question4.layout
    elif pathname == '/question5':
        return question5.layout
    elif pathname == '/question6':
        return question6.layout
    elif pathname == '/testapp':
        return testapp.layout
    else:
        return 404 #app.layout

server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')

if __name__ == '__main__':
    app.run_server(debug=True)
