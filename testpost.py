# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
"""
Shows basic usage of the Sheets API. Prints values from a Google Spreadsheet.
"""
from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Sheets API
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
spreadsheet_id = '1-3p8bsYudw7nQryJEnTIace5YQX9TZVvr4IWr23sWA0'
range_name = 'test!A1:E'

value_input_option = 'USER_ENTERED'
# result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
#                                              range=RANGE_NAME).execute()
# values = result.get('values', [])
# if not values:
#     print('No data found.')
# else:
#     print('Name, Major:')
#     for row in values:
#         # Print columns A and E, which correspond to indices 0 and 4.
#         print('%s, %s' % (row[0], row[4]))


values = [
    [
        "test","x","y","z"
        # Cell values ...
    ],
    [
    	"1","2","3","4"
    ],
    # Additional rows ...
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=range_name,
    valueInputOption=value_input_option, body=body).execute()
print('{0} cells updated.'.format(result.get('updatedCells')));
# [END sheets_quickstart]