# import the necessary modules and libraries
from taipy.gui import Gui
import taipy as tp

from pages.table.table import table_md #import table
from pages.dashboard.dashboard import dashboard_md #import dashboard
from pages.map.map import map_md #import map
from pages.root import root, selected_location, selector_location

pages = {
    '/':root,
    "List":table_md,
    "Dashboard":dashboard_md,
    "Map":map_md,
}


gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="BC Wildfires List")
    