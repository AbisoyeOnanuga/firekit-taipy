from taipy.gui import Markdown
from ..data.data import fetch_data, ms_to_datetime  # Import the necessary functions

# Fetch the data
data = fetch_data()

selected_location = 'North Arm Stuart Lake'
data_location = None


def initialize_case_evolution(data, selected_location='North Arm Stuart Lake'):
    # Aggregation of the dataframe to erase the regions that will not be used here
    data_location = data.groupby(["Incident Name",'Discovery Date'])\
                            .sum()\
                            .reset_index()
    
    # a location is selected, here North Arm Stuart Lake by default
    data_location = data_location.loc[data_location['Location']==selected_location]
    return data_location

data_location = initialize_case_evolution(data)


def on_change_location(state):
    # state contains all the Gui variables and this is through this state variable that we can update the Gui
    # state.selected_location, state.data_location, ...
    # update data_location with the right location (use initialize_case_evolution)
    print("Chosen location: ", state.selected_location)
    state.data_location = initialize_case_evolution(data, state.selected_location)
    

dashboard_md = Markdown("pages/dashboard/dashboard.md")
