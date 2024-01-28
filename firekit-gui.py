from taipy import Gui
import pandas as pd

df = pd.read_csv('data/wildfire_data_clean.csv')

page = """
# BC Wildfires List

DataFrame: <|{data}|table|>
<|{df}|table|page_size=10|page_size_options=[10, 20, 50, 100]|filter=True|group_by[Category]=True|apply[Calories]=sum|>

"""

Gui(page=page).run()
