import dash
from dash import dcc
from dash import html
#import plotly.graph_objs as go
import plotly.graph_objects as go #Added by @MGB
#from app import app, gdf, phase_colors, phase_labels

from utils import Header, make_dash_table

import pathlib
#import additional libraries by @MGB
import geopandas as gpd
import json
from dash.dependencies import Input, Output
import pandas as pd
import pathlib
#import os
from pathlib import Path

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))
df_graph = pd.read_csv(DATA_PATH.joinpath("df_graph.csv")) # Added by @MGB
gdf2 = pd.read_json(DATA_PATH.joinpath("mozambique_acute_food_insecurity_november_2022.json"))

########################################################################################
######## Load the GDP data  ############################################################
########################################################################################
# Load GDP data from the CSV file


# Get the path to the 'data' directory relative to the current script's location
gdp_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'gdp' / 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855' / 'API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855.csv'

#df_gdp = pd.read_csv(r'Z:\Private\miguel.bambo\datascience\Dash\mais\data\1.economic\gdp\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855\API_NY.GDP.MKTP.CD_DS2_en_csv_v2_5728855.csv', skiprows=3)
df_gdp = pd.read_csv(gdp_file_path, skiprows=3)
# Filter the data to only include "Aruba" row
mozambique_data = df_gdp[df_gdp['Country Name'] == 'Mozambique']

# Extract the years and GDP values from the dataframe
years = list(mozambique_data.columns[4:])
gdp_values = list(mozambique_data.values[0][4:])
########################################################################################
######## END Load the GDP data  ############################################################
########################################################################################

# Adding code 

# Import the 'app' instance from app.py
#from app import app

# Create a new instance of the Dash app for the Economic page
app = dash.Dash(__name__)

########################################################################################
######## Load the GeoJSON data for FOOD INSECURITY #####################################
########################################################################################

# Replace 'your_file_path.json' with the actual file path of your JSON file.
#file_path = r'Z:\Private\miguel.bambo\datascience\Dash\mais\data\1.economic\food_insecurity\Mozambique-Acute Food Insecurity November 2022.json'

# Get the path to the 'data' directory relative to the current script's location
gdf_file_path = Path(__file__).parent.parent / 'data' / '1.economic' / 'food_insecurity' / 'Mozambique-Acute Food Insecurity November 2022.json'

# Open the GeoJSON data
with open(gdf_file_path) as f:
    data = json.load(f)

# Convert the GeoJSON data to a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(data['features'])


# Define custom colors and text labels for each phase
phase_colors = {
    1: '#fff7ec',
    2: '#fdd49e',
    3: '#fc8d59',
    4: '#d7301f',
    5: '#7f0000'
}

phase_labels = {
    1: '1-Minimal',
    2: '2-Stressed',
    3: '3-Crisis',
    4: '4-Emergency',
    5: '5-Famine'
}

# Map the phase values to colors and text labels in the GeoDataFrame
gdf['color'] = gdf['overall_phase_C'].map(phase_colors)
gdf['phase_label'] = gdf['overall_phase_C'].map(phase_labels)

###################################################################################################
######## END Load the GeoJSON data for FOOD INSECURITY ############################################
###################################################################################################

def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Summary"),
                                    html.Br([]),
                                    html.P(
                                        #"\
                                    "Mozambique faces multiple contextual factors that could be “game changers”.\
                                    Each has the potential to affect the CDCS in significantly positive or \
                                    negative ways.  As a result, the Mission started the intervention named \
                                    Mozambique Adaption Information System (MAIS) in 2021 with support from \
                                    the Mozambique Monitoring, Evaluation Mechanism and Services (MMEMS), to \
                                    identify an approach that must support effective context monitoring and \
                                    inform adaptive decision-making in a rapidly evolving environment. \
                                    MAIS is meant to be a practical and sustainable system over time."\
                                        #style={'marginRight': '20px'} 
                                    #html.Br(),
                                    #html.P(
                                    "The MAIS system is an innovative initiative that aims to provide \
                                    USAID/Mozambique with a platform for data visualization and analysis for \
                                    USAID/Mozambique’s development programs. However, the system was never \
                                    fully implemented due to various challenges and constraints. Currently, \
                                    USAID decided to reactivate the system with the support of MozMEL.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 3.1 #Added by @MGB
                    #####
                    #####


                    #####
                    #####    
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Food Insecurity: November 2022 - March 2023", className="subtitle padded"),
                                    dcc.Graph(
                                        id="choropleth-map", # Assign a unique id to the graph
                                        figure=update_map(None),  # Call the update_map function to initialize the map
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                        #style={"height": "450px", "margin-bottom": "0px"}  # Set/Adjust the height and margin-bottom of the choropleth map as needed  
                                    ),
                                    html.P("Source: Integrated Food Security Phase Classification. Last Updated Date: March, 28th 2023.", style={"font-size": "10px", "color": "#888"}),
                                ],
                                className="twelve columns",
                                #style={"margin-bottom": "10px"}  # Adjust the margin-bottom to reduce the empty space
                                ),
                        ],
                        className="row ",
                    ),
                    # Row 4
                    html.Div(
                        [
                            #####Insert Hypothetical growth#######
                            html.Div(
                                [
                                    html.H6(
                                        "GDP (current US$)",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        # figure=update_graph_2(),  # Call the update_graph_2 function to initialize the linechart/scatter plot
                                        figure={
                                             "data": [
                                                 go.Scatter(
                                                    x=years,
                                                    y=gdp_values,
                                                    mode='lines',
                                                    marker=dict(size=8),
                                        #             x=[
                                        #                 "2008",
                                        #                 "2009",
                                        #                 "2010",
                                        #                 "2011",
                                        #                 "2012",
                                        #                 "2013",
                                        #                 "2014",
                                        #                 "2015",
                                        #                 "2016",
                                        #                 "2017",
                                        #                 "2018",
                                        #             ],
                                        #             y=[
                                        #                 "10000",
                                        #                 "7500",
                                        #                 "9000",
                                        #                 "10000",
                                        #                 "10500",
                                        #                 "11000",
                                        #                 "14000",
                                        #                 "18000",
                                        #                 "19000",
                                        #                 "20500",
                                        #                 "24000",
                                        #             ],
                                                    line={"color": "#97151c"},
                                        #             mode="lines",
                                        #             name="Calibre Index Fund Inv",
                                                 )
                                             ],
                                             "layout": go.Layout(
                                                 autosize=True,
                                        #         title="",
                                                 font={"family": "Raleway", "size": 10},
                                               height=200,
                                               width=340,
                                                 hovermode="closest",
                                        #         legend={
                                        #             "x": -0.0277108433735,
                                        #             "y": -0.142606516291,
                                        #             "orientation": "h",
                                        #         },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                        #         showlegend=True,
                                        #         xaxis={
                                        #             "autorange": True,
                                        #             "linecolor": "rgb(0, 0, 0)",
                                        #             "linewidth": 1,
                                        #             "range": [2008, 2018],
                                        #             "showgrid": False,
                                        #             "showline": True,
                                        #             "title": "",
                                        #             "type": "linear",
                                        #         },
                                        #         yaxis={
                                        #             "autorange": False,
                                        #             "gridcolor": "rgba(127, 127, 127, 0.2)",
                                        #             "mirror": False,
                                        #             "nticks": 4,
                                        #             "range": [0, 30000],
                                        #             "showgrid": True,
                                        #             "showline": True,
                                        #             "ticklen": 10,
                                        #             "ticks": "outside",
                                        #             "title": "$",
                                        #             "type": "linear",
                                        #             "zeroline": False,
                                        #             "zerolinewidth": 4,
                                        #         },
                                             ),
                                         },
                                         config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                    html.P("Source: The World Bank. Last Updated Date: July, 25th 2023.", style={"font-size": "10px", "color": "#888"}),
                                ],
                                className="six columns",
                            ),

                            #####End Hypothetical growth#######
                            
                            html.Div(
                                [
                                    html.H6(
                                        "Average annual performance",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "41 Year",
                                                    ],
                                                    y=[
                                                        "21.67",
                                                        "11.26",
                                                        "15.62",
                                                        "8.37",
                                                        "11.11",
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Calibre Index Fund",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "1 Year",
                                                        "3 Year",
                                                        "5 Year",
                                                        "10 Year",
                                                        "41 Year",
                                                    ],
                                                    y=[
                                                        "21.83",
                                                        "11.41",
                                                        "15.79",
                                                        "8.50",
                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="S&P 500 Index",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 20,
                                                    "b": 10,
                                                    "l": 10,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": True, "displaylogo": False},  # Enable the display mode bar and hide the logo
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5

                    html.Div(
                        [
                            ###### Hypothetical growth was here###########
                            html.Div(
                                [
                                    html.H6(
                                        ["Fund Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_fund_facts)),
                                ],
                                className="six columns",
                            ),
                            ##### Ended Hypothetical growth was here #####

                            html.Div(
                                [
                                    html.H6(
                                        "Price & Performance (%)",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_price_perf)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Risk Potential", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("risk_reward.png"),
                                        className="risk-reward",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
             #],         
            #],
                className="sub_page",
            ),
        ],
        className="page",
    )


################################################################################
###### UPDATING CHOROPLETH MAP #################################################
################################################################################

# Define the callback for the Choropleth Map
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('choropleth-map', 'clickData')
)

######S#######
##############

def update_map(clickData):
    fig = go.Figure()

    for phase, color in phase_colors.items():
        phase_data = gdf[gdf['overall_phase_C'] == phase]
        # Convert GeoDataFrame to GeoJSON format
        geojson_data = phase_data.__geo_interface__
        fig.add_trace(go.Choroplethmapbox(
            geojson=geojson_data,
            locations=phase_data.index,
            z=phase_data['overall_phase_C'],
            colorscale=[[0, color], [1, color]],
            marker_opacity=0.7,
            marker_line_width=0,
            colorbar_title='Area Phase',
            name=phase_labels[phase],
            showscale=False
        ))

    fig.update_layout(mapbox_style="carto-positron",
                      mapbox_zoom=3.5,
                      mapbox_center={"lat": -18.665695, "lon": 35.529562},
                      mapbox_layers=[]  # Hide default base map layers
                      )

    # Add legend using annotations with a gray background
    legend_text = "<br>".join([f"<b><span style='color:{phase_colors[phase]}'>{phase_labels[phase]}</span></b>" for phase in phase_colors.keys()])
    fig.add_annotation(go.layout.Annotation(
        x=1.03,
        y=0.5,
        xanchor='left',
        yanchor='middle',
        text=legend_text,
        showarrow=False,
        font=dict(color='black', size=12),
        bgcolor='lightgray',  # Add a gray background
        bordercolor='gray',
        borderwidth=0.5,
        align='left'
    ))

    fig.update_layout(margin=dict(l=0, r=150, t=20, b=0))  # Adjust the right margin to accommodate the legend

    return fig

#########################################################################################
###### ENDING UPDATING CHOROPLETH MAP ###################################################
#########################################################################################

#########################################################################################
###### UPDATING GDP (current US$) MAP ###################################################
#########################################################################################

# # Define the callback for the Graph-2 ScatterPlot CHART
# @app.callback(
#     Output('graph-2', 'figure'),
#     #Input('graph-2', 'clickData')
# )

# # Function to update graph-2 with GDP data
# def update_graph_2():



#     fig = go.Figure()
    
#     fig.add_trace(go.Scatter(
#         x=years,
#         y=gdp_values,
#         line={"color": "#97151c"},
#         mode="lines",
#         name="GDP (current US$)",
#         # x=years,
#         # y=gdp_values,
#         # line={"color": "#97151c"},
#         # mode="lines",
#         # name="GDP (current US$)",
#     ))
    
#     fig.update_layout(
#         autosize=True,
#         title="",
#         font={"family": "Raleway", "size": 10},
#         height=200,
#         width=340,
#         hovermode="closest",
#         legend={
#             "x": -0.0277108433735,
#             "y": -0.142606516291,
#             "orientation": "h",
#         },
#         margin={
#             "r": 20,
#             "t": 20,
#             "b": 20,
#             "l": 50,
#         },
#         showlegend=True,
#         xaxis={
#             "autorange": True,
#             "linecolor": "rgb(0, 0, 0)",
#             "linewidth": 1,
#             "showgrid": False,
#             "showline": True,
#             "title": "",
#             "type": "linear",
#         },
#         yaxis={
#             "autorange": False,
#             "gridcolor": "rgba(127, 127, 127, 0.2)",
#             "mirror": False,
#             "nticks": 4,
#             "showgrid": True,
#             "showline": True,
#             "ticklen": 10,
#             "ticks": "outside",
#             "title": "GDP (current US$)",
#             "type": "linear",
#             "zeroline": False,
#             "zerolinewidth": 4,
#         },
#         # autosize=True,
#         # title="",
#         # font={"family": "Raleway", "size": 10},
#         # height=200,
#         # width=340,
#         # hovermode="closest",
#         # legend={
#         #     "x": -0.0277108433735,
#         #     "y": -0.142606516291,
#         #     "orientation": "h",
#         # },
#         # margin={
#         #     "r": 20,
#         #     "t": 20,
#         #     "b": 20,
#         #     "l": 50,
#         # },
#         # showlegend=True,
#         # xaxis={
#         #     "autorange": True,
#         #     "linecolor": "rgb(0, 0, 0)",
#         #     "linewidth": 1,
#         #     #"range": [df_gdp['Year'].min(), df_gdp['Year'].max()],
#         #     "showgrid": False,
#         #     "showline": True,
#         #     "title": "",
#         #     "type": "linear",
#         # },
#         # yaxis={
#         #     "autorange": False,
#         #     "gridcolor": "rgba(127, 127, 127, 0.2)",
#         #     "mirror": False,
#         #     "nticks": 4,
#         #     #"range": [0, df_gdp['GDP (current US$)'].max() * 1.1],  # Adjust the range to have some margin at the top
#         #     "showgrid": True,
#         #     "showline": True,
#         #     "ticklen": 10,
#         #     "ticks": "outside",
#         #     "title": "GDP (current US$)",
#         #     "type": "linear",
#         #     "zeroline": False,
#         #     "zerolinewidth": 4,
#         # },
#     )
    
#     return fig

#########################################################################################
###### ENDING UPDATING GDP (current US$) MAP ############################################
#########################################################################################