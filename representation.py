
from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('filtered_data.csv')
fig = px.line(df, x="Date", y="Sales")

app.layout = html.Div([
    dcc.Graph(
        id='Date-vs-Sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)