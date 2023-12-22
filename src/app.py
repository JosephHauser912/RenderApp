from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv('GHCND_sample_csv.csv', on_bad_lines='skip')
df['new_date'] = pd.to_datetime(df['DATE'].astype(str), format='%Y%m%d')
print(df.dtypes)

app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div(id='my-title', children='Weather in Seattle'),
    dcc.Dropdown(id='date-dropdown', options=df.new_date.unique(), value='20100101', multi=True),
    dcc.Graph(id='graph1')

])


@app.callback(
    Output('graph1', 'figure'),
    Input(component_id='date-dropdown', component_property='value')
)
def selek(date_selected):
    print(date_selected)
    df_date = df[df.new_date.isin(date_selected)]
    print(df_date)
    fig1 = px.scatter(df_date, x='TMAX', y='TMIN')
    return fig1


if __name__ == "__main__":
    app.run(debug=True)