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
    # Use the mapped 'color' column for the marker color
    "color": "color",
    "text": "text",
    "label": "label",  # Assuming 'Location' is a column in your map_data
    "textposition": "bottom center",
    # Use the "hoverlabel" parameter to customize the hover text box
    "hoverinfo": "text",  # Ensure this is set to display the hover text
    "hoverlabel": {
        "bgcolor": "rgba(128, 128, 128, 0.5)",
        "bordercolor": "black",
        "font": {"color": "black", "size": 12},
        "align": "left"
    }
}

layout = {
    "title": "Estimated Wildfire sizes in BC<br>(Hover for details)",
    "geo": {
        "showland": True,
        "showocean": False,
        "scope": "canada",
        "subunitcolor": "lightgrey",
        "landcolor": "lightgrey",
        "subunitwidth": 2,
        "coastlinewidth": 1,
        "center": {"lat": 54.5, "lon": -125.5},
        "fitbounds": "locations",
        "showcountries": True,
        "countrycolor": "darkgrey",
        "countrywidth": 2,
        "showsubunits": True,
        "showcoastlines": True,
        "showlakes": True,
        "showrivers": True,
        "resolution": 100,
        "projection_type": "van der grinten"
    },
    "annotations": [
        {
            "x": 1.0,
            "y": 1,
            "xref": "paper",
            "yref": "paper",
            "text": "Stage Of Control",
            "showarrow": False,
            "font": {"size": 24}
        },
        {
            "x": 0.96,
            "y": 0.8,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Out of Control",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "red"}
        },
        {
            "x": 0.94,
            "y": 0.7,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Being Held",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "orange"}
        },
        {
            "x": 0.96,
            "y": 0.55,  # Adjusted for more spacing
            "xref": "paper",
            "yref": "paper",
            "text": "● Under Control",  # Larger bullet point using Unicode
            "showarrow": False,
            "font": {"size": 16, "color": "green"}
        }
    ]
}

map_md = Markdown("pages/map/map.md")
