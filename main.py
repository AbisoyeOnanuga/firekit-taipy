from taipy.gui import Gui
import taipy as tp

# Import the Markdown pages
from pages.root import root
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

# Create the Gui instance with the Markdown pages
gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="BC Wildfires List")
