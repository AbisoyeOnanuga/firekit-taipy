# import the necessary modules and libraries
from taipy.gui import Markdown
from ..data.data import fetch_data

# define data functions for the table page
# Fetch the data
data = fetch_data()

# create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
