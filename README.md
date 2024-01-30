# Firekit
A wildfire data dashboard for BC designed with Taipy GUI

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
- **Level**: Beginner-Intermediate
- **Topic**: Taipy-GUI
- **Components/Controls**: 
  - Taipy GUI: table, map, dashboard, toggle, multi-pages

## How to run

This app works with a Python version 3.11.5. run the *main.py* in the `root/` folder. You can also find a *requirements.txt* in the `root/` folder.

## Introduction

Firekit manages multiple pages.

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
- `docs/`: contains the images for the documentation
- `INSTALLATION.md`: Instructions to install _demo-covid-dashboard_.
- `LICENSE`: MIT License.
- `README.md`: Current file.

## License
Copyright 2024 Firekit

## Installation

Want to install _Demo Covid Dashboard_? Check out our [`INSTALLATION.md`](INSTALLATION.md) file.