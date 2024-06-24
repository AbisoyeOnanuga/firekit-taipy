# import the necessary modules and libraries
from taipy.gui import Markdown

# Import the Markdown content from the .md file
from table import table_md_content

# Define a function to set the table content in the GUI
def set_table_content(gui, data):
    gui.set_variable("data", data)
    gui.set_page_content("List", Markdown(table_md_content))
