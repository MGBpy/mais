#import dash_core_components as dcc #Deprecated
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd
import pathlib
from pathlib import Path

# get relative data folder
PATH = Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

#Military Expenditure Data
file_path = Path(__file__).parent.parent / 'data' / '6.security' / 'militaryExpenditure' / 'SIPRI-Milex-data-1949-2022.csv'
df_mExp = pd.read_csv(file_path,skiprows=0)
mozambique_data = df_mExp[df_mExp['Country'] == 'Mozambique']
# Extract the years and data values from the dataframe
years_mExp = list(mozambique_data.columns[0:])
mExp_values = list(mozambique_data.values[0][0:])
#End Maternal Mortality Rate Data

#Murder/Homicide Rate Data
file_path = Path(__file__).parent.parent / 'data' / '6.security' / 'homicideRate' / 'homicideRate.csv'
df_homRt = pd.read_csv(file_path,skiprows=0)
#mozambique_data = df_litr[df_litr['Country Name'] == 'Mozambique']
# Extract the years and GDP values from the dataframe
#years_litr = list(mozambique_data.columns[0:])
#litr_values = list(mozambique_data.values[0][0:])
# end Murder/Homicide Rate Data

    # df_current_prices = pd.read_csv(DATA_PATH.joinpath("df_current_prices.csv"))
    # df_hist_prices = pd.read_csv(DATA_PATH.joinpath("df_hist_prices.csv"))
    # df_avg_returns = pd.read_csv(DATA_PATH.joinpath("df_avg_returns.csv"))
    # df_after_tax = pd.read_csv(DATA_PATH.joinpath("df_after_tax.csv"))
    # df_recent_returns = pd.read_csv(DATA_PATH.joinpath("df_recent_returns.csv"))
    # df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    html.H6("Annual Reported Indicators", style={'margin-bottom': '0'}), # Header above Horizontal Line
                    html.Hr(style={'margin-top': '0', 'margin-bottom': '0'}), # Horizontal line with no top margin
                    # Row 1
                    html.Div(
                        [
                            html.Div([
                                        html.H6("Military Expenditure (MZN)", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-1",
                                            figure={
                                                "data": [
                                                    go.Scatter(
                                                        x=years_mExp,
                                                        y=mExp_values,
                                                        line={"color": "#97151c"},
                                                        mode="lines+markers",
                                                        name="",
                                                    ),
                                                    # go.Scatter(
                                                    #     x=df_graph["Date"],
                                                    #     y=df_graph[
                                                    #         "MSCI EAFE Index Fund (ETF)"
                                                    #     ],
                                                    #     line={"color": "#b5b5b5"},
                                                    #     mode="lines",
                                                    #     name="MSCI EAFE Index Fund (ETF)",
                                                    # ),
                                                ],
                                                "layout": go.Layout(
                                                    autosize=True,
                                                     width=340,
                                                     height=200,
                                                    font={"family": "Raleway", "size": 10},
                                                    margin={
                                                        "r": 30,
                                                        "t": 30,
                                                        "b": 30,
                                                        "l": 30,
                                                    },
                                                    showlegend=False,
                                                    titlefont={
                                                        "family": "Raleway",
                                                        "size": 10,
                                                    },
                                                    xaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            "2007-12-31",
                                                            "2018-03-06",
                                                        ],
                                                        "rangeselector": {
                                                            "buttons": [
                                                                {
                                                                    "count": 5,
                                                                    "label": "5Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 10,
                                                                    "label": "10Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 15,
                                                                    "label": "15Y",
                                                                    "step": "year",
                                                                },
                                                                {
                                                                    "count": 20,
                                                                    "label": "20Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "label": "All",
                                                                    "step": "all",
                                                                },
                                                            ]
                                                        },
                                                        "showline": False,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            18.6880162434,
                                                            278.431996757,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                    },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: https://www.sipri.org", href='https://www.sipri.org/databases/milex', target="_blank", style={"font-size": "10px", "color": "#888"})),
                                        
                                ],
                                        className = "six columns",
                            ),
                            html.Div([  
                                        html.H6("Murder/Homicide Rate", className="subtitle padded"),
                                        dcc.Graph(
                                            id="graph-2",
                                            figure={
                                                "data": [
                                                    go.Scatter(
                                                        x=df_homRt['Year'],
                                                        y=df_homRt['rate'],
                                                        line={"color": "#97151c"},
                                                        mode="lines+markers",
                                                        name="Rate",
                                                    ),
                                                    go.Bar(
                                                        x=df_homRt['Year'],
                                                        y=df_homRt['pct_change'],
                                                        marker={
                                                        "color": "#bbbbbb",
                                                        
                                                        # "line": {
                                                        #     "color": "rgb(255, 255, 255)",
                                                        #     "width": 2,
                                                        # },
                                                    },
                                                    name="% Change",
                                                    yaxis="y2",
                                                    ),
                                                ],
                                                "layout": go.Layout(
                                                    autosize=True,
                                                     width=340,
                                                     height=200,
                                                    font={"family": "Raleway", "size": 10},
                                                    margin={
                                                        "r": 30,
                                                        "t": 30,
                                                        "b": 30,
                                                        "l": 30,
                                                    },
                                                    legend={
                                                    "x": -0.0428945952895,
                                                    "y": -0.209563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                    },
                                                    showlegend=True,
                                                    titlefont={
                                                        "family": "Raleway",
                                                        "size": 10,
                                                    },
                                                    xaxis={
                                                        "autorange": True,
                                                        "range": [
                                                            "2007-12-31",
                                                            "2018-03-06",
                                                        ],
                                                        "rangeselector": {
                                                            "buttons": [
                                                                {
                                                                    "count": 5,
                                                                    "label": "5Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },
                                                                {
                                                                    "count": 10,
                                                                    "label": "10Y",
                                                                    "step": "year",
                                                                    "stepmode": "backward",
                                                                },                                                                
                                                                {
                                                                    "label": "All",
                                                                    "step": "all",
                                                                },
                                                            ]
                                                        },
                                                        "showline": False,
                                                        "type": "date",
                                                        "zeroline": False,
                                                    },
                                                    yaxis={
                                                        "autorange": False,
                                                        "range": [
                                                            3,
                                                            6.5,
                                                        ],
                                                        "showline": False,
                                                        "type": "linear",
                                                        "zeroline": False,
                                                        "overlaying": "y2",
                                                        "title": "Per 100k Population",
                                                    },
                                                    yaxis2={
                                                        "autorange": False,
                                                        "range": [-30, 10],
                                                        "showgrid": False,
                                                        "showline": False,
                                                        "title": "Annual % change",
                                                        "side": "right",
                                                        "type": "linear",
                                                        "zeroline": False,
                                                },
                                                ),
                                            },
                                            config={"displayModeBar": False},
                                        ),
                                        html.P(html.A("Source: Macrotrends", href='https://www.macrotrends.net/countries/MOZ/mozambique/murder-homicide-rate', target="_blank", style={"font-size": "10px", "color": "#888"})),

                                ],
                                    className="six columns"
                            ),

                        ],
                                #className="row",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Indicator 3", className="subtitle padded"),
                                    dcc.Graph(
                                        id="graph-4",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    #x=df_graph["Date"],
                                                    #y=df_graph["Calibre Index Fund"],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Calibre Index Fund",
                                                ),
                                                go.Scatter(
                                                    #x=df_graph["Date"],
                                                    # y=df_graph[
                                                    #     "MSCI EAFE Index Fund (ETF)"
                                                    # ],
                                                    line={"color": "#b5b5b5"},
                                                    mode="lines",
                                                    name="MSCI EAFE Index Fund (ETF)",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                width=340,
                                                height=200,
                                                font={"family": "Raleway", "size": 10},
                                                margin={
                                                    "r": 30,
                                                    "t": 30,
                                                    "b": 30,
                                                    "l": 30,
                                                },
                                                showlegend=True,
                                                titlefont={
                                                    "family": "Raleway",
                                                    "size": 10,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        "2007-12-31",
                                                        "2018-03-06",
                                                    ],
                                                    "rangeselector": {
                                                        "buttons": [
                                                            {
                                                                "count": 1,
                                                                "label": "1Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 3,
                                                                "label": "3Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "count": 5,
                                                                "label": "5Y",
                                                                "step": "year",
                                                            },
                                                            {
                                                                "count": 10,
                                                                "label": "10Y",
                                                                "step": "year",
                                                                "stepmode": "backward",
                                                            },
                                                            {
                                                                "label": "All",
                                                                "step": "all",
                                                            },
                                                        ]
                                                    },
                                                    "showline": True,
                                                    "type": "date",
                                                    "zeroline": False,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [
                                                        18.6880162434,
                                                        278.431996757,
                                                    ],
                                                    "showline": True,
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Indicator 4"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            # html.Table(
                                            #     make_dash_table(df_avg_returns),
                                            #     className="tiny-header",
                                            # )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        [
                                            "Indicator 5"
                                        ],
                                        className="subtitle padded",
                                    ),
                                    html.Div(
                                        [
                                            # html.Table(
                                            #     make_dash_table(df_after_tax),
                                            #     className="tiny-header",
                                            # )
                                        ],
                                        style={"overflow-x": "auto"},
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Indicator 6"],
                                        className="subtitle padded",
                                    ),
                                    # html.Table(
                                    #     make_dash_table(df_recent_returns),
                                    #     className="tiny-header",
                                    # ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
