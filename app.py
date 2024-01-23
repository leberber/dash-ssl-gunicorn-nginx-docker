from dash import Dash, html, dcc, callback, Input, Output
import socket
app = Dash(__name__)

server = app.server
print('socket', socket.gethostname())

app.layout = html.Div(
  children = [
   html.Button('Submit', id='input', n_clicks=0),
   html.Div( id='output')
]
 
)

@callback(
    Output('output', 'children'),
    Input('input', 'n_clicks')
)
def update_output(n_clicks):
    return f" this content is serverd from container id : {socket.gethostname()}" 




