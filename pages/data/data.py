import requests
import pandas as pd
import datetime
import json
import numpy

def fetch_data():
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
    data = data.loc[:, ['incidentName', 'lastUpdatedTimestamp', 'incidentLocation', 'stageOfControlCode', 'incidentSizeEstimatedHa', 'discoveryDate', 'fireCentreName', 'longitude', 'latitude']]

    # rename the columns to make them more readable
    data.columns = ['Incident Name', 'Last Updated', 'Location', 'Stage of Control', 'Size (Ha)', 'Discovery Date', 'Fire Centre', 'lon', 'lat']
    
        # Apply the custom function to convert timestamps to datetime objects
    data['Last Updated'] = data['lastUpdatedTimestamp'].apply(ms_to_datetime)
    data['Discovery Date'] = data['discoveryDate'].apply(ms_to_datetime)

    # Format the datetime objects as strings
    format = '%m/%d/%Y %H:%M:%S'
    data['Last Updated'] = data['Last Updated'].dt.strftime(format)
    data['Discovery Date'] = data['Discovery Date'].dt.strftime(format)

    # Replace values in the Stage of Control column
    data['Stage of Control'] = data['stageOfControlCode'].replace({
        'OUT_CNTRL': 'Out Of Control',
        'HOLDING': 'Being Held',
        'UNDR_CNTRL': 'Under Control'
    })

    return data

# define a custom function that converts milliseconds to a datetime object
def ms_to_datetime(ms):
    # divide milliseconds by 1000 to get seconds
    seconds = ms / 1000
    # use datetime.fromtimestamp to get a datetime object
    dt = datetime.datetime.fromtimestamp(seconds)
    # return the datetime object
    return dt

# Specific processing for the map page
def prepare_map_data(data):
    # Ensure that the 'lat' and 'lon' columns are numeric
    data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
    data['lon'] = pd.to_numeric(data['lon'], errors='coerce')

    # Drop rows with NaN values that resulted from the conversion
    data = data.dropna(subset=['lat', 'lon'])

    # Add a column holding the bubble size and hover texts
    #   Min(incidentSizeEstimatedHa) -> size = 8
    #   Max(incidentSizeEstimatedHa) -> size = 60
    data["size"] = numpy.interp(data["Size (Ha)"], [data["Size (Ha)"].min(), data["Size (Ha)"].max()], [8, 60])
    # Add a column holding the bubble hover texts
    # Format is "<Location> [<Stage of Control>]"
    data["text"] = data.apply(lambda row: f"Location: {row['Location']}<br> Stage of Control: [{row['Stage of Control']}]<br> Size (Ha): {row['Size (Ha)']}<br> Fire Centre: {row['Fire Centre']}<br> Last Updated: {row['Last Updated']}<br> Discovery Date: {row['Discovery Date']}", axis=1)

    # Ensure that the 'lat' and 'lon' columns are numeric
    data['lat'] = pd.to_numeric(data['lat'], errors='coerce')
    data['lon'] = pd.to_numeric(data['lon'], errors='coerce')

    # Drop rows with NaN values that resulted from the conversion
    data = data.dropna(subset=['lat', 'lon'])

    # Update the bubble sizes by applying a different scaling factor
    # You can adjust the multiplier to scale the bubble sizes as needed
    # data['size'] = numpy.interp(data["Size (Ha)"], [data["Size (Ha)"].min(), data["Size (Ha)"].max()], [100, 100])
    # data['size'] = data['Size (Ha)'].apply(lambda x: max(x**1, 10))  # Replace 0.5 with your preferred exponent

    return data

# Define the CSV file name
# csv_file_name = 'wildfire_data.csv'

# Save the DataFrame to a CSV file
#data.to_csv(csv_file_name, index=False)

#print(f'Data saved to {csv_file_name}')