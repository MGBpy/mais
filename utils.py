#import dash_html_components as html #Deprecated
from dash import html
#import dash_core_components as dcc #Deprecated
from dash import dcc
###S###
#######
import geopandas as gpd
import json
import plotly.graph_objects as go
#######
###E###



def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.A(
                        html.Img(
                            src=app.get_asset_url("usaid.png"),
                            className="logo",
                        ),
                        # href="https://plotly.com/dash",
                    ),
                    # html.A(
                    #     html.Button(
                    #         "Enterprise Demo",
                    #         id="learn-more-button",
                    #         style={"margin-left": "-10px"},
                    #     ),
                    #     href="https://plotly.com/get-demo/",
                    # ),
                    # html.A(
                    #     html.Button("Source Code", id="learn-more-button"),
                    #     href="https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-financial-report",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Mozambique Context Monitoring")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/mais/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Economic",
                href="/mais/economic",
                className="tab first",
            ),
            dcc.Link(
                "Social",
                href="/mais/social",
                className="tab",
            ),
            dcc.Link(
                "Political",
                href="/mais/political",
                className="tab",
            ),
            dcc.Link(
                "Environmental", href="/mais/environmental", className="tab"
            ),
            dcc.Link(
                "Infrastructure",
                href="/mais/infrastructure",
                className="tab",
            ),
            dcc.Link(
                "Security",
                href="/mais/security",
                className="tab",
            ),
            dcc.Link(
                "Decentralization",
                href="/mais/decentralization",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
