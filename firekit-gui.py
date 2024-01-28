from taipy.gui import Gui, Markdown
import pandas as pd

# read the cleaned data from the csv file
df = pd.read_csv('wildfire_data_clean.csv')

# create a markdown string with the table definition
md = f"<|{df}|table|page_size=10|page_size_options=[10, 20, 50, 100]|>"

# create a gui object with the markdown string
gui = Gui(page=Markdown(md))

# run the gui
gui.run()
