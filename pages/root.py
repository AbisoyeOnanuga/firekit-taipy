import taipy.gui.builder as tgb
import numpy as np
from pages.data.data import fetch_data

# Fetch the data and prepare the selector options
raw_data = fetch_data()
selector_location = list(np.sort(raw_data['Location'].astype(str).unique()))
selected_location = 'North Arm Stuart Lake'

# Define a function to create the root page using Taipy GUI Builder
def create_root_page():
    with tgb.Page() as page:
        # Add an HTML element for the title and logo
        tgb.html("h1", "", style={"vertical-align": "middle", "font-size": "100px", "margin-left": "500px"},
                 children=[
                     tgb.html("img", "", src="./image/Firekit-logo.png", width="200", height="200", style={"vertical-align": "middle"}),
                     "Firekit"
                 ])
        
        # Add a theme toggle element
        tgb.toggle(theme=True)
        
        # Add a navbar element (you'll need to define the navigation structure)
        tgb.navbar()
        
    return page

# Create the root page object
root_page = create_root_page()
