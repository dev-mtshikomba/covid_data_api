# import modules
# %% [Modules]
import requests
import csv
import boto3
from datetime import datetime
from io import BytesIO
import os

# define functions here
# %% [Functions]


def pull_counties_data_from_api(county=None):
    '''
        county: - when set to None this function returns all the conties
               - to get one county set it to a county FIPS postal code e.g. Autauga = 01001
               - List of county FIPS codes (https://www.nrcs.usda.gov/wps/portal/nrcs/detail/national/home/?cid=nrcs143_013697)
    '''
    if county:
        return requests.get('https://api.covidactnow.org/v2/county/' + str(county) + '.json?apiKey='+os.environ['API_TOKEN'])
    return requests.get('https://api.covidactnow.org/v2/counties.timeseries.csv?apiKey='+os.environ['API_TOKEN'])



def write_data_to_csv_file():
    # now we will open a file for writing
    print("Entering Write Data Function")
    # properly call your s3 bucket

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('covid-data')
    
    with pull_counties_data_from_api() as r, BytesIO(r.content) as payload:
        try:
            r.raise_for_status()
            if r.ok:
                bucket.upload_fileobj(payload, 'counties_data.csv')
            return {
                'statusCode': 200,
                'body': f"File Update {'succeeded' if r.ok else 'failed'}, with status code {r.status_code}"
            }
        except requests.exceptions.HTTPError as err:
            return {
                'statusCode': 500,
                'body': f"File Update failed badly, with error response {error}"
            }
    print ('exiting function')

# AWS Lambda Function
# %% [Lambda Function]
def main(event=None, contex=None):
    print("Start @: ", datetime.now().strftime("%H:%M:%S"))
    write_data_to_csv_file()
    print("End @: ", datetime.now().strftime("%H:%M:%S"))
  


# implement main method
# %% [Main Method]
if __name__ == "__main__":
    main()
