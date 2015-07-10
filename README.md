# TCIAExplorer 
[![Build Status](https://travis-ci.org/lastlegion/TCIAExplorer.svg?branch=master)](https://travis-ci.org/lastlegion/TCIAExplorer)

Easy to use Python wrapper around TCIA's REST API.

### Installation
Run `python setup.py install` to install.


### Usage
Add TCIA_API_KEY environment variable.
Run `python scripts/explorer.py` to follow this sequential work flow for downloading images:
* Select a collection
* Select a patient 
* Select a patient study
* Select a series
* Select images to download
