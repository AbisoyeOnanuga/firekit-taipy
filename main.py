from taipy.gui import Gui
import taipy as tp

# Import the functions that create each page
from pages.root import create_root_page
from pages.table.table import create_table_page
from pages.dashboard.dashboard import create_dashboard_page
from pages.map.map import create_map_page

# Create the page objects using the functions
root_page = create_root_page()
table_page = create_table_page()
dashboard_page = create_dashboard_page()
map_page = create_map_page()

# Define the pages dictionary with the new page objects
pages = {
    '/': root_page,
    "List": table_page,
    "Dashboard": dashboard_page,
    "Map": map_page,
}

# Create the Gui instance with the new pages
gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Config.app.serve_static_files = True  # Enable serving static files if needed for assets like images

    tp.Core().run()
    
    gui_multi_pages.run(title="BC Wildfires List")
