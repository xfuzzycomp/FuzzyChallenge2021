import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as ex
import plotly.graph_objects as go


class SuperPlot:
    def __init__(self):
        self.app = dash.Dash(__name__)

from competition.plotter import Plotter

plotter = Plotter("../scripts/competition_data.json")
# plotter.winner()

app = dash.Dash(__name__)

# Specify page divs
app.layout = html.Div([

    # Floating header
    html.Div([

        html.P("UC Fuzzy Challenge 2021", style={"text-align": "center", "font-size": "24px", "font-weight": "bold"}),

        html.Div([
            html.Div([
                html.P("Teams:"),
                dcc.Dropdown(
                    id="dropdown-team",
                    options=[
                        {"label": x, "value": x} for x in plotter.teams
                    ],
                    value=plotter.teams,
                    multi=True,
                ),
            ], style={"width": "30%", "display": "inline-block"}),

            html.Div([
                html.P("Scenarios:"),
                dcc.Dropdown(
                    id="dropdown-scenario",
                    options=[{"label": x, "value": x} for x in plotter.scenarios],
                    value=plotter.scenarios[0],
                ),
            ], style={"width": "30%", "display": "inline-block"}),
        ], style={"display": "flex", "justify-content": "space-around"}),

        html.Div(style={"border-bottom": "3px solid #bbb", "height": 20, "width": "95%", "margin": "auto"}),

    ], style={"position": "sticky", "top": "0", "width":"100%", "z-index":"100", "background-color": "#FFFFFF", "margin": "0px"}),

    # Graphics which can slide under the header
    html.Div([
        html.Div([dcc.Graph(id="table")]),

            html.Div([
                html.Div([
                    dcc.Graph(id="num-asteroids")],
                    # style={"width": "49%", "display": "inline-block"},
                ),
                html.Div([
                    dcc.Graph(id="eval-times")],
                    # style={"width": "49%", "display": "inline-block"},
                ),
            ]),

    ], style={"background-color": "#F0F8FF"}),


])


@app.callback(
    Output("num-asteroids", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def num_asteroids_over_time(teams, scenarios):
    fig = go.Figure(
        data=[
            go.Scatter(x=np.linspace(0, plotter.data[team][scenarios]["time"], len(plotter.data[team][scenarios]["evaluation_times"])+1).tolist(),
                       y=plotter.data[team][scenarios]["num_asteroids"],
                       mode='lines',
                       name=team,
                       )

            for idx, team in enumerate(teams)])

    fig.update_layout(title="Number of Asteroids over Time",
                      title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Time (sec)",
                      yaxis_title="Num Asteroids",)

    return fig

@app.callback(
    Output("eval-times", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def graph_eval_times(teams, scenarios):
    fig = go.Figure(
        data=[
            go.Scatter(x=plotter.data[team][scenarios]["num_asteroids"],
                       y=plotter.data[team][scenarios]["evaluation_times"],
                       mode='markers',
                       name=team,
                       )

            for idx, team in enumerate(teams)])

    fig.update_layout(title="Evaluation Time Distributions",
                      title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Asteroids (#)",
                      yaxis_title="Evaluation Time (sec)",)

    return fig

@app.callback(
    Output("table", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def data_table(teams, scenarios):
    categories = ["asteroids_hit", "bullets_fired", "deaths", "stopping_condition", "exceptions", "time"]

    fig = go.Figure(
            go.Table(header=dict(values=["Team"] + [" ".join(c.capitalize() for c in cat.split("_")) for cat in categories]),
                     cells=dict(values=[teams] + [[plotter.data[team][scenarios][label] for idx, team in enumerate(teams)]  for label in categories] ))
            )

    fig.update_layout(title="Performance Summary", height=300)

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
