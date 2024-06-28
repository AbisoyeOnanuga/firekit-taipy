from taipy.gui import Gui
import taipy as tp

# Import the Markdown pages
from pages.root import root, selected_location, selector_location
from pages.table.table import table_md
from pages.dashboard.dashboard import dashboard_md
from pages.map.map import map_md

# Define the pages dictionary with the Markdown pages
pages = {
    '/': root,
    "List": table_md,
    "Dashboard": dashboard_md,
    "Map": map_md,
}

stylekit = {
    "color_primary": "rgb(0, 123, 255)",  # A blue-ish primary color
    "color_background_light": "rgb(240, 248, 255)",  # A light blue background for the light theme
    #"color_primary": "rgb(255, 87, 34)",  # Example primary color
    "color_secondary": "rgb(255, 193, 7)",  # Example secondary color
    #"color_background_light": "rgb(250, 250, 250)",  # Light grey for light theme background
    "color_background_dark": "rgb(33, 33, 33)",  # Dark grey for dark theme background
    "color_paper_dark": "rgb(55, 55, 55)",  # Darker grey for elevated elements in dark theme
    "color_paper_light": "rgb(255, 255, 255)",  # White for elevated elements in light theme
    "font_family": "'Roboto', sans-serif",  # Example font family
    "--border_radius": "10px",  # Example border radius
    # ... other style properties ...
}

# Create the Gui instance with the Markdown pages
gui_multi_pages = Gui(pages=pages, css_file="custom_styles.css")

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="BC Wildfires List", stylekit=stylekit)
