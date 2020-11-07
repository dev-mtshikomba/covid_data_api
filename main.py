# import modules
# %% [Modules]
from config import *
import requests
import csv
# define functions here
# %% [Functions]


def pull_counties_data_from_api(county=None):
    '''
        county: - when set to None this function returns all the conties
               - to get one county set it to a county FIPS postal code e.g. Autauga = 01001
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


def write_data_to_csv_file(json_object):
    # now we will open a file for writing
    data_file = open('counties_data_1.csv', 'w')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for e in json_object:
        if count == 0:
            # Writing headers of CSV file
            header = str(e.keys())
            print(header)
            csv_writer.writerow(e.keys())
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(e.values())

    data_file.close()

# AWS Lambda Function
# %% [Lambda Function]
def main(event=None, contex=None):
    write_data_to_csv_file(pull_counties_data_from_api())


# implement main method
# %% [Main Method]
if __name__ == "__main__":
    main()

# %%
