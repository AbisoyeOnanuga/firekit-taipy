import taipy.gui.builder as tgb
from pages.data.data import fetch_data

# Fetch the data
data = fetch_data()

# Define a function to create the table page using Taipy GUI Builder
def create_table_page():
    with tgb.Page() as page:
        # Create a table element
        tgb.table(data, page_size=10, page_size_options=[10, 50, 100], filter=True, group_by='Fire Centre', apply='Estimated Size (Ha)')

    return page

# Create the table page object
table_page = create_table_page()
