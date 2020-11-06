# import modules
# %% [Modules]
from config import *
import requests

# define functions here
# %% [Functions]


def pull_counties_data_from_api(county=None):
    '''
        county: - when set to None this function returns all the conties
               - to get one state set it to a county FIPS postal code e.g. Washtenaw = 
               - List of county FIPS codes (https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697)
    '''
    if county:
        return requests.get('https://api.covidactnow.org/v2/county/'+str(county)+'.json?apiKey='+api_token).json()
    return requests.get('https://api.covidactnow.org/v2/counties.json?apiKey='+api_token).json()


def pull_state_data_from_api(state=None):
    '''
        state: - when this function is set to None this function returns all the states
               - to get one state set it to a state postal code e.g. Michigan = MI
               - List of state postal codes (https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696)
    '''
    if state:
        return requests.get('https://api.covidactnow.org/v2/state/'+state+'.json?apiKey='+api_token).json()
    return requests.get('https://api.covidactnow.org/v2/states.json?apiKey='+api_token).json()

# implement main method
# %% [Main Method]
if __name__ == "__main__":
    pull_counties_data_from_api()
