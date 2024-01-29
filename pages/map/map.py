import pandas
import numpy
from taipy.gui import Gui
from taipy.gui import Markdown

cities = [
    {"name": "Tokyo", "lat": 35.6839, "lon": 139.7744, "population": 39105000},
    {"name": "Jakarta", "lat": -6.2146, "lon": 106.8451, "population": 35362000},
    {  "name": "Xinyang", "lat": 32.1264, "lon": 114.0672, "population": 6109106},
]


# Convert to Pandas DataFrame
data = pandas.DataFrame(cities)

# Add a column holding the bubble size:
#   Min(population) -> size =  5
#   Max(population) -> size = 60
solve = numpy.linalg.solve([[data["population"].min(), 1], [data["population"].max(), 1]],
                           [5, 60])
data["size"] = data["population"].apply(lambda p: p*solve[0]+solve[1])

# Add a column holding the bubble hover texts
# Format is "<city name> [<population>]"
data["text"] = data.apply(lambda row: f"{row['name']} [{row['population']}]", axis=1)

marker = {
    # Use the "size" column to set the bubble size
    "size": "size"
}

layout = {
    "geo": {
        "showland": True,
        "landcolor": "4A4"
    }
}

map_md = Markdown("pages/map/map.md")