import taipy.gui.builder as tgb
import numpy as np
from pages.data.data import fetch_data, prepare_map_data
import plotly.express as px

# Fetch the data and prepare the map data
data = fetch_data()
map_data = prepare_map_data(data)

# Define the function to create the map page using Taipy GUI Builder with scattergeo_mapbox
def create_map_page():
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
    map_data['size'] = np.interp(map_data["Estimated Size (Ha)"], [map_data["Estimated Size (Ha)"].min(), map_data["Estimated Size (Ha)"].max()], [10, 60])

    # Create the scatter mapbox with the updated color map and sizes
    fig = px.scatter_mapbox(map_data,
                            lat='Latitude',
                            lon='Longitude',
                            size='size',
                            color='Stage of Control',
                            color_discrete_map=color_discrete_map,
                            size_max=15,
                            zoom=5,
                            mapbox_style='open-street-map',
                            hover_name='Incident Name',
                            hover_data=['Location', 'Estimated Size (Ha)', 'Stage of Control', 'Last Updated', 'Discovery Date'])

    # Update the layout if needed
    fig.update_layout(
        margin={'r':0, 't':0, 'l':0, 'b':0},
        mapbox=dict(
            center=dict(lat=54.5, lon=-125.5),
            style='carto-positron',
        ),
        hoverlabel=hoverlabel
    )

    # Convert the Plotly figure to JSON for Taipy GUI Builder
    fig_json = fig.to_json()

    with tgb.Page() as page:
        # Use the JSON figure in the Taipy GUI Builder chart element
        tgb.chart(type='scattergeo_mapbox', figure=fig_json)

    return page

# Create the map page object
map_page = create_map_page()
