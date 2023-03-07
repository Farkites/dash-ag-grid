import dash_ag_grid as dag
from dash import Dash, html, Input, Output, State
from . import utils

def test_rm001_row_menu(dash_duo):
    app = Dash(__name__)

    row_menu_example = html.Div(
        [
            dag.AgGrid(
                id="grid",
                columnSize="sizeToFit",
                columnDefs=[
                    {"headerName": "Make", "field": "make", "sortable": True},
                    {"headerName": "Model", "field": "model"},
                    {"headerName": "Price", "field": "price"},
                    {"headerName": "Menu", "field": "menu", "cellRenderer": "rowMenu"},
                ],
                rowData=[
                    {
                        "make": "Toyota",
                        "model": "Celica",
                        "price": 35000,
                        "menu": [
                            {"label": "Option 1", "value": 1},
                            {"label": "Option 2", "value": 2},
                            {"label": "Option 3", "value": 3},
                        ],
                    },
                    {
                        "make": "Ford",
                        "model": "Mondeo",
                        "price": 32000,
                        "menu": [
                            {"label": "Option 4", "value": 4},
                            {"label": "Option 5", "value": 5},
                            {"label": "Option 6", "value": 6},
                        ],
                    },
                    {
                        "make": "Porsche",
                        "model": "Boxter",
                        "price": 72000,
                        "menu": [
                            {"label": "Option 7", "value": 7},
                            {"label": "Option 8", "value": 8},
                            {"label": "Option 9", "value": 9},
                        ],
                    },
                ],
            ),
            html.P(id="click-data"),
            html.Hr(),
        ]
    )

    app.layout = html.Div(
        row_menu_example,
        style={"flexWrap": "wrap"},
    )

    @app.callback(
        Output("click-data", "children"),
        Input("grid", "cellRendererData_timestamp"),
        State("grid", "cellRendererData"),
    )
    def show_click_data(ts, data):
        if ts:
            return "You selected option {} from the row with make {}, model {}, and price {}.".format(
                data["value"],
                data["data"]["make"],
                data["data"]["model"],
                data["data"]["price"],
            )
        return "No menu item selected."

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")

    grid.wait_for_cell_text(0, 0, "Toyota")

    ### testing components
    grid.element_click_cell_button(0, 3)
    assert 'opacity: 1' in dash_duo.find_element('.MuiPopover-root .MuiMenu-paper').get_attribute('style')
    dash_duo.find_elements('.MuiPopover-root .MuiMenu-paper .MuiMenu-list .MuiListItem-button')[1].click()
    dash_duo.wait_for_text_to_equal('#click-data',
                                    'You selected option 2 from the row with make Toyota, model Celica, and price 35000.')
