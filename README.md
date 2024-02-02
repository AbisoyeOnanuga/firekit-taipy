# Firekit
A wildfire data dashboard for BC made with Taipy and Python <br/>
![Dashboard](https://github.com/AbisoyeOnanuga/firekit-taipy/assets/102636953/e62145cc-8430-498a-907c-f35694da413a)

## Usage
- [Usage](#usage)
- [Firekit](#what-is-Firekit)
- [Directory Structure](#directory-structure)
- [License](#license)
- [Installation](#installation)

## What is Firekit

[Firekit](https://github.com/AbisoyeOnanuga/firekit-taipy) is a multi-page application showing how Taipy can build a minimalist but useful application.
This app visualizes BC Wildfire Services active fires. Pages shows active fires in different formats - as a table, a dashboard and on a map.

### Demo Type
- **Topic**: Taipy-GUI
- **Components/Controls**: 
  - Taipy GUI: table, map, dashboard, toggle, multi-pages

## How to run

- This app works with a Python version 3.11.5. 
- run `git clone https://github.com/AbisoyeOnanuga/firekit-taipy.git` from your editor
- `cd firekit-taipy`
- run `pip install -r requirements.txt`
- run the *main.py* in the `root/` folder with `python main.py`

### Table

The table page show a list of all active wildfires in BC. the list can be filtered with a control at the top left by applying multiple filters for any column.


### Map

A map can be found on this page to explore the data. Colors and sizes are dependent on the Stage of Control and incident size(Ha) in each location.

### Dashboard

The dashboard page shows wildfire status on a specific location. The location can be changed. It will update the cards provided on this page.


## Directory Structure


- `root/`: Contains the demo source code.
  - `root/data`: Contains the application data files.
  - `root/pages`: Contains the page definition files.
- `INSTALLATION.md`: Instructions to install _firekit-taipy_.
- `LICENSE`: MIT License.
- `README.md`: Current file.

## License
Copyright 2024 Firekit

## Installation

Want to install _firekit-taipy_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.
