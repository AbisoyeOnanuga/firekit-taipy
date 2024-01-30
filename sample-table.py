from taipy import Gui
import pandas as pd

df = pd.read_csv('data/wildfire_data_clean.csv')

page = """
# BC Wildfires List

Wildfires <|{data}|table|>
<|{df}|table|page_size=10|page_size_options=[10, 50, 100]|filter=True|group_by[fireCentreName]=True|apply[incidentSizeEstimatedHa]=sum|>

"""

Gui(page=page).run()
