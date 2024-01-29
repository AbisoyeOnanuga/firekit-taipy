from taipy.gui import Markdown 

import numpy as np

from data.data import data

selector_location = list(np.sort(data['incidentLocation'].astype(str).unique()))
selected_location  = 'North Arm Stuart Lake'

root = Markdown("pages/root.md")