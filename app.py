# -*- coding: utf-8 -*-
import dash
import dash_auth #Added by MGBpy
#import dash_core_components as dcc #Deprecated
from dash import dcc
#import dash_html_components as html #Deprecated
from dash import html
from dash.dependencies import Input, Output
#from utils import load_data, map_phase_to_colors_labels

#PRINTING

#PRINTING

from pages import (
    economic,
    social,
    political,
    environmental,
    infrastructure,
    security,
    decentralization,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}],
)
app.title = "Mozambique Context Monitoring"
server = app.server

# #############################################################################################################
# ################LOG IN#############
# VALID_USERNAME_PASSWORD_PAIRS = [
#     ['usaid', 'usaid']
# ]
# ###################################
# #### Authorizing the App ####################################################################################

# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
# #############################################################################################################

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

#####S#####
###########

#####E#####
###########

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")]

    )

# ######S#####
# ############

# ######E#####
# ############



def display_page(pathname):
    if pathname == "/mais/social":
        return social.create_layout(app)
    elif pathname == "/mais/political":
        return political.create_layout(app)
    elif pathname == "/mais/environmental":
        return environmental.create_layout(app)
    elif pathname == "/mais/infrastructure":
        return infrastructure.create_layout(app)
    elif pathname == "/mais/security":
        return security.create_layout(app)
    elif pathname == "/mais/decentralization":
        return decentralization.create_layout(app)
    elif pathname == "/mais/full-view":
        return (
            economic.create_layout(app),
            social.create_layout(app),
            political.create_layout(app),
            environmental.create_layout(app),
            infrastructure.create_layout(app),
            security.create_layout(app),
            decentralization.create_layout(app),
        )
    else:
        return economic.create_layout(app)

# START PRINTING

# END PRINTING




if __name__ == "__main__":
    app.run_server(port=8090, debug=True) #Set to True when Deploying the app


