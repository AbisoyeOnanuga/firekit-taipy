import taipy.gui.builder as tgb
from pages.data.data import fetch_data, ms_to_datetime

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

# Define the callback function for the selector change event
def on_change_location(state):
    global data_location
    data_location = initialize_case_evolution(data, state.selected_location)
    print("Chosen location: ", state.selected_location)


# Define a function to create the dashboard page using Taipy GUI Builder
def create_dashboard_page():
    with tgb.Page() as page:
        # Add a selector element for location
        tgb.selector(location=selected_location, on_change=on_change_location)
        # Create a layout with two rows of three columns
        with tgb.layout(columns="1fr 1fr 1fr"):
            # Add a card element for the location
            with tgb.part():
                tgb.text(f"Location: {data_location.iloc[-1]['Location']}")
            # Add a card element for the stage of control
            with tgb.part():
                tgb.text(f"Stage of Control: {data_location.iloc[-1]['Stage of Control']}")
            # Add a card element for the estimated size
            with tgb.part():
                tgb.text(f"Estimated Size (Ha): {'{:,}'.format(int(data_location.iloc[-1]['Estimated Size (Ha)'])).replace(',', ' ')}")
            # Add a card element for the fire centre
            with tgb.part():
                tgb.text(f"Fire Centre: {data_location.iloc[-1]['Fire Centre']}")
            # Add a card element for the last updated date
            with tgb.part():
                tgb.text(f"Last Updated: {data_location.iloc[-1]['Last Updated']}")
            # Add a card element for the discovery date
            with tgb.part():
                tgb.text(f"Discovery Date: {data_location.iloc[-1]['Discovery Date']}")

    return page

# Create the dashboard page object
dashboard_page = create_dashboard_page()
