import numpy
from taipy.gui import Markdown
import plotly.express as px

from data.data import fetch_data, prepare_map_data

# Fetch the data
data = fetch_data()

# Prepare the data specifically for the map
map_data = prepare_map_data(data)

# Define the function to create the Plotly map figure
def create_map_figure(data):
    # Define hoverlabel and marker inside the function to ensure they use the latest data
    hoverlabel = {
        "bgcolor": "rgba(128, 128, 128, 0.5)",
        "bordercolor": "black",
        "font": {"color": "black", "size": 12},
        "align": "left"
    }

    color_discrete_map = {
        'Out Of Control': 'red',
        'Being Held': 'orange',
        'Under Control': 'green'
    }

    # Update the bubble sizes by applying a different scaling factor
    data['size'] = numpy.interp(data["Size (Ha)"], [data["Size (Ha)"].min(), data["Size (Ha)"].max()], [10, 60])

    # Create the scatter mapbox with the updated color map and sizes
    fig = px.scatter_mapbox(data,
                            lat='lat',
                            lon='lon',
                            size='size',
                            color='Stage of Control',
                            color_discrete_map=color_discrete_map,
                            size_max=15,
                            zoom=5,
                            mapbox_style='open-street-map',
                            hover_name='Incident Name',
                            hover_data=['Location', 'Size (Ha)', 'Stage of Control', 'Last Updated', 'Discovery Date'])

    # Update the layout if needed
    fig.update_layout(
        margin={'r':0, 't':0, 'l':0, 'b':0},
        mapbox=dict(
            center=dict(lat=54.5, lon=-125.5),
            style='carto-positron',
        )
    )
    return fig

map_md = Markdown("pages/map/map.md")
