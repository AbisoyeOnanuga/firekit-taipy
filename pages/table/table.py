from taipy.gui import Markdown

from ..data.data import fetch_data

# Fetch the data
data = fetch_data()

# Create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
