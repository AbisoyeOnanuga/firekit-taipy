# main.py
from flask import Flask
from taipy.gui import Gui

from pages.table.table import table_md #import table
from pages.dashboard.dashboard import dashboard_md #import dashboard
from pages.map.map import map_md #import map

app = Flask(__name__)

# Define the pages
root_md = """ <h1 style="vertical-align: middle; font-size: 100px; margin-left: 500px;"><img style="vertical-align: middle;" src="./image/Firekit-logo.png" width="200" height="200" />Firekit</h1>
<|toggle|theme|><|navbar|>
"""

pages = {
    "/": root_md,
    "Wildfire-List": table_md,
    "Dashboard": dashboard_md,
    "Map": map_md
}

# Create the Gui object
gui = Gui(pages=pages)

# Register the Gui object with the Flask app
gui.run(app)

# Run the Flask app
if __name__ == "__main__":
    app.run()