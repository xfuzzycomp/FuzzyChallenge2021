import os
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as ex
import plotly.graph_objects as go

from competition.plotter import Plotter

environment_frequency = 60  # Hz
plotter = Plotter(os.path.join(os.path.dirname(__file__), "competition_data.json"))
# plotter.winner()

app = dash.Dash(__name__)

# Specify page divs
app.layout = html.Div([

    # Floating header
    html.Div([

        html.H1("UC Fuzzy Challenge 2021", style={"text-align": "center"}),

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
            ], style={"width": "40%", "display": "inline-block"}),

            html.Div([
                html.P("Scenarios:"),
                dcc.Dropdown(
                    id="dropdown-scenario",
                    options=[{"label": x, "value": x} for x in ["summary"] + plotter.scenarios],
                    value="summary",
                ),
            ], style={"width": "40%", "display": "inline-block"}),
        ], style={"display": "flex", "justify-content": "space-around"}),

    ], style={"border-bottom": "3px solid #bbb", "position": "sticky", "top": "0", "width":"100%", "z-index":"100", "background-color": "#F0F8FF", "margin-bottom": 10, "padding-bottom": 10}),

    # Summary plots (only shown during "summary" scenario)
    html.Div([
        html.Div([
            dcc.Graph(id="summary-asteroids-destroyed"),
            dcc.Graph(id="summary-deaths"),
            dcc.Graph(id="summary-accuracy"),
            dcc.Graph(id="summary-distance-travelled"),
            dcc.Graph(id="summary-mean-evaluation-time"),
            dcc.Graph(id="summary-shots-fired"),
            dcc.Graph(id="summary-time"),
        ]),
    ], id="summary-div", style={"display": "block"}),

    # Graphics Shown on a per scenario basis
    html.Div([
        html.Div([
            dcc.Graph(id="table"),
            dcc.Graph(id="asteroids-destroyed"),
            dcc.Graph(id="num-asteroids"),
            dcc.Graph(id="accuracy"),
            dcc.Graph(id="eval-times-series"),
            dcc.Graph(id="eval-times"),
        ]),
    ], id="scenario-div", style={"display": "none"}),

], style={"background-color": "#FFFFFF", "margin": "0", "padding": "0", "top": "0",})


@app.callback(
    Output(component_id="summary-div", component_property="style"), Output(component_id="scenario-div", component_property="style"),
    [Input("dropdown-scenario", "value")])
def toggle_summary_div_visibility(scenarios):
    if scenarios == "summary":
        return {"display": "block"}, {"display": "none"}
    else:
        return {"display": "none"}, {"display": "block"}


# # summary callbacks
# @app.callback(
#     Output("summary-table", "figure"),
#     [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
# def summary_score(teams, scenarios):
#     if scenarios != "summary":
#         return go.Figure()
#     fig = go.Figure(
#         data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["asteroids_hit"][idx], name=team)
#               for idx, team in enumerate(teams)])
#
#     fig.update_layout(title="Asteroids Destroyed per Scenario", title_x=0.5,
#                       legend_title_text="Team",
#                       xaxis_title="Scenario",
#                       yaxis_title="Asteroids Destroyed",
#                       barmode="group")
#
#     return fig

# summary callbacks
@app.callback(
    Output("summary-asteroids-destroyed", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_score(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["asteroids_hit"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Asteroids Destroyed per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Asteroids Destroyed",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-deaths", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_deaths(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["deaths"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Deaths per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Deaths",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-accuracy", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_accuracy(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["accuracy"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Accuracy per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Accuracy",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-distance-travelled", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_distance_travelled(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["distance_travelled"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Distance Travelled per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Distance Travelled",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-mean-evaluation-time", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_mean_eval_time(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["mean_evaluation_time"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Mean Evaluation Time per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Mean Evaluation Time (s)",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-shots-fired", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_shots_fired(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["shots_fired"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Shots Fired per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Shots Fired",
                      barmode="group")

    return fig

@app.callback(
    Output("summary-time", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def summary_time(teams, scenarios):
    if scenarios != "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Bar(x=plotter.scenarios, y=plotter.metrics["time"][idx], name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Sim Time per Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Scenario",
                      yaxis_title="Sim Time (s)",
                      barmode="group")

    return fig

@app.callback(
    Output("asteroids-destroyed", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def num_asteroids_over_time(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Scatter(x=np.linspace(0, plotter.data[team][scenarios]["time"], len(plotter.data[team][scenarios]["asteroids_over_time"])+1).tolist(),
                         y=plotter.data[team][scenarios]["asteroids_over_time"],
                         mode="lines", name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Asteroids Destroyed Over Time", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Time (sec)",
                      yaxis_title="Num Asteroids",)

    return fig


@app.callback(
    Output("num-asteroids", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def num_asteroids_over_time(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Scatter(x=np.linspace(0, plotter.data[team][scenarios]["time"], len(plotter.data[team][scenarios]["evaluation_times"])+1).tolist(),
                         y=plotter.data[team][scenarios]["num_asteroids"],
                         mode="lines", name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Number of Active Asteroids over Time",
                      title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Time (sec)",
                      yaxis_title="Num Asteroids")

    return fig


@app.callback(
    Output("accuracy", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def num_asteroids_over_time(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Scatter(x=np.linspace(0, plotter.data[team][scenarios]["time"], len(plotter.data[team][scenarios]["accuracy_over_time"])+1).tolist(),
                         y=[val * 100.0  for val in plotter.data[team][scenarios]["accuracy_over_time"]],
                         mode="lines", name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Accuracy over Time", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Time (sec)",
                      yaxis_title="Accuracy (%)")
    return fig


@app.callback(
    Output("eval-times", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def graph_eval_times(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Scatter(x=plotter.data[team][scenarios]["num_asteroids"],
                         y=plotter.data[team][scenarios]["evaluation_times"],
                         mode="markers", name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Controller Complexity (Scalability)",
                      title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Asteroids (#)",
                      yaxis_title="Evaluation Time (sec)")

    max_x = max(max(plotter.data[team][scenarios]["num_asteroids"]) for idx, team in enumerate(teams))
    fig.add_trace(go.Scatter(x=[0, max_x], y=[1 / environment_frequency, 1 / environment_frequency],
                             name=f"{environment_frequency} Hz Limit", mode="lines",
                             marker_color="rgba(0, 0, 0, .8)"))

    return fig


@app.callback(
    Output("eval-times-series", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def graph_eval_times_series(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    fig = go.Figure(
        data=[go.Scatter(x=np.linspace(0, plotter.data[team][scenarios]["time"],
                                       len(plotter.data[team][scenarios]["evaluation_times"]) + 1).tolist(),
                         y=plotter.data[team][scenarios]["evaluation_times"],
                         mode="lines", name=team)
              for idx, team in enumerate(teams)])

    fig.update_layout(title="Evaluation Time over Scenario", title_x=0.5,
                      legend_title_text="Team",
                      xaxis_title="Time (sec)",
                      yaxis_title="Evaluation Time (sec)")

    max_x = max(plotter.data[team][scenarios]["time"] for idx, team in enumerate(teams))
    fig.add_trace(go.Scatter(x=[0, max_x], y=[1 / environment_frequency, 1 / environment_frequency],
                             name=f"{environment_frequency} Hz Limit", mode="lines",
                             marker_color="rgba(0, 0, 0, .8)"))
    return fig

@app.callback(
    Output("table", "figure"),
    [Input("dropdown-team", "value"), Input("dropdown-scenario", "value")])
def data_table(teams, scenarios):
    if scenarios == "summary":
        return go.Figure()

    categories = ["stopping_condition", "time", "asteroids_hit", "bullets_fired", "deaths", "exceptions",
                  "distance_travelled", "mean_eval_time", "median_eval_time", "min_eval_time", "max_eval_time"]

    data = [[plotter.data[team][scenarios][label] for idx, team in enumerate(teams)] for label in categories]

    table = go.Table(header=dict(values=["Team"] + [" ".join(c.capitalize() for c in cat.split("_")) for cat in categories]),
                     cells=dict(values=[teams] + data))
    table.cells.format = [[None], [None], [".2f"], [None], [None], [None], [None], [".2f"], [".4f"], [".4f"], [".4f"], [".4f"]]

    fig = go.Figure(table)

    fig.update_layout(title="Performance Summary")

    return fig


# Summary Plots
if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)
