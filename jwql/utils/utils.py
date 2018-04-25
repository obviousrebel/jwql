"""Various utility functions for the jwql project.

Authors
-------

    Matthew Bourque

Use
---

    This module can be imported as such:

    >>> import utils
    settings = get_config()
"""

import json


JWST_INSTRUMENTS = ['NIRISS', 'NIRCam', 'NIRSpec', 'MIRI', 'FGS']
JWST_DATAPRODUCTS = ['IMAGE', 'SPECTRUM', 'SED', 'TIMESERIES', 'VISIBILITY',
                     'EVENTLIST', 'CUBE', 'CATALOG', 'ENGINEERING', 'NULL']

def get_config():
    """Return a dictionary that holds the contents of the jwql config
    file.

    Returns
    -------
    settings : dict
        A dictionary that holds the contents of the config file.
    """

    with open('config.json', 'r') as config_file:
        settings = json.load(config_file)

    return settings
