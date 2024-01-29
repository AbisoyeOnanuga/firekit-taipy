# import the necessary modules and libraries
from taipy.gui import Gui
from pages.table import table_md
from pages.dashboard import dashboard_md

pages = {"table": table_md, "dashboard": dashboard_md}

Gui(pages=pages).run()
