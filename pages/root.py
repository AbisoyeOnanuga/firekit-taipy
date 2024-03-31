from taipy.gui import Markdown 

import numpy as np

from pages.data.data import data

selector_location = list(np.sort(data['Location'].astype(str).unique()))
selected_location  = 'North Arm Stuart Lake'

root = Markdown("pages/root.md")