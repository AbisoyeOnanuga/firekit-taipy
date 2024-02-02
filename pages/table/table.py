# import the necessary modules and libraries
import requests
import pandas as pd
from taipy import Gui
from taipy.gui import Markdown
import datetime
import json

# define the base URL of the API
base_url = 'https://wildfiresituation-api.nrs.gov.bc.ca/publicPublishedIncident'

# define the parameters for the GET request
page_number = 1
page_row_count = 20
stage_of_control_list = ['OUT_CNTRL', 'HOLDING', 'UNDR_CNTRL']
new_fires = False
order_by = 'lastUpdatedTimestamp DESC'

# create an empty list to store the data
data = []

# loop through all the possible pages
while True:
    # define the parameters for the GET request
    params = {
        'pageNumber': page_number,
        'pageRowCount': page_row_count,
        'stageOfControlList': stage_of_control_list,
        'newFires': new_fires,
        'orderBy': order_by
    }
    # make a GET request to the API with the parameters
    try:
        response = requests.get(base_url, params=params)
        # parse the response as a JSON object
        json_data = json.loads(response.text)
        # get the total number of rows and pages from the JSON object
        total_rows = json_data['totalRowCount']
        total_pages = json_data['totalPageCount']
        # get the content of the JSON object, which is a list of wildfires
        content = json_data['collection']
        # append the content to the data list
        data.extend(content)
        # check if there are more pages to fetch
        if page_number < total_pages:
            # increment the page number by 1
            page_number += 1
        else:
            # break the loop if there are no more pages to fetch
            break
    except Exception as e:
        # handle any errors that might occur during the request
        print(f'Error: {e}')
        break

# convert the list of data to a pandas DataFrame
data = pd.DataFrame(data)

# select only the desired columns in order
data = data.loc[:, ['incidentName', 'lastUpdatedTimestamp', 'incidentLocation', 'stageOfControlCode', 'incidentSizeEstimatedHa', 'discoveryDate', 'fireCentreName']]

# rename the columns to make them more readable
data.columns = ['Incident Name', 'Last Updated', 'Location', 'Stage of Control', 'Size (Ha)', 'Discovery Date', 'Fire Centre']

# define a custom function that converts milliseconds to a datetime object
def ms_to_datetime(ms):
    # divide milliseconds by 1000 to get seconds
    seconds = ms / 1000
    # use datetime.fromtimestamp to get a datetime object
    dt = datetime.datetime.fromtimestamp(seconds)
    # return the datetime object
    return dt

# apply the custom function to the 'lastUpdatedTimestamp' and 'discoveryDate' columns
data['Last Updated'] = data['Last Updated'].apply(ms_to_datetime)
data['Discovery Date'] = data['Discovery Date'].apply(ms_to_datetime)

# define a format string for the datetime objects
format = '%m/%d/%Y %H:%M:%S'

# format the datetime objects as strings using the format string
data['Last Updated'] = data['Last Updated'].dt.strftime(format)
data['Discovery Date'] = data['Discovery Date'].dt.strftime(format)

# make an edit to the data in the Stage of Control column by replacing the values
data['Stage of Control'] = data['Stage of Control'].replace({'OUT_CNTRL': 'Out Of Control', 'HOLDING': 'Being Held', 'UNDR_CNTRL': 'Under Control'})

# create a Markdown control and set the content to the Taipy table syntax
table_md = Markdown("pages/table/table.md")
