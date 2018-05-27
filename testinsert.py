"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from pprint import pprint

from googleapiclient import discovery

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# # Call the Sheets API
# SPREADSHEET_ID = '1-3p8bsYudw7nQryJEnTIace5YQX9TZVvr4IWr23sWA0'
# RANGE_NAME = 'test!A1:E'
# spreadsheet_id = '1-3p8bsYudw7nQryJEnTIace5YQX9TZVvr4IWr23sWA0'
# range_name = 'test!A1:E'

# value_input_option = 'USER_ENTERED'



# credentials = 'credentials.json'

# service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1-3p8bsYudw7nQryJEnTIace5YQX9TZVvr4IWr23sWA0'  # TODO: Update placeholder value.

# The A1 notation of a range to search for a logical table of data.
# Values will be appended after the last row of the table.
range_ = 'test!A2:C'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'USER_ENTERED'  # TODO: Update placeholder value.

# How the input data should be inserted.
insert_data_option = 'INSERT_ROWS'  # TODO: Update placeholder value.

values = [
    [
        "test","x","y"
        # Cell values ...
    ],
    [
    	"1","2","3"
    ],
    # Additional rows ...
]
body = {
    'values': values
}

request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)