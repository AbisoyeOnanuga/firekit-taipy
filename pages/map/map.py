from taipy.gui import Markdown
from ..data.data import fetch_data, prepare_map_data

# Fetch the data and prepare the map data
data = fetch_data()
map_data = prepare_map_data(data)

hoverlabel = {
    # Use a transparent grey color for the background
    "bgcolor": "rgba(128, 128, 128, 0.5)",
    # Use a black color for the border
    "bordercolor": "black",
    # Use a black color and a 12px size for the font
    "font": {"color": "black", "size": 12},
    # Use a left alignment for the text
    "align": "left"
}

marker = {
    # Use the "size" column to set the bubble size
    "size": "size",
    # Use the "stageOfControlCode" column to set the marker color
    "color": "stage of Control",
    # Use a discrete color map to assign different colors to different stages of control
    "color_discrete_map": {"Out of Control": "red", "Being Held": "orange", "Under Control": "green"},
    "text": "text",
    # Use the "hoverlabel" parameter to customize the hover text box
    "hoverlabel": "hoverlabel"
}

layout = {
    "geo": {
        "showland": False,
        "showocean": False,
        "scope": "canada",
        "subunitcolor": "lightgrey",
        "subunitwidth": 2,
        "coastlinewidth": 1,
        "center": {"lat": 54.5, "lon": -125.5},
        "fitbounds": "locations",
        "projection_scale": 1,
        "showcountries": True,
        "countrycolor": "white",
        "countrywidth": 2,
        "showsubunits": True,
        "showcoastlines": True,
        "showlakes": True,
        "showrivers": True,
        "resolution": 100,
        "projection": "van der grinten"
    }
}

map_md = Markdown("pages/map/map.md")
