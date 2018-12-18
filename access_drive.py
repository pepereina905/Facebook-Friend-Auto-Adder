import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from read_json import lab_coat_secret

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

json_keyfile_location = 'fb_auto.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_location, scope)

gc = gspread.authorize(credentials)

spreadsheet_url = lab_coat_secret

lab_coat_agents = gc.open_by_url(spreadsheet_url)

lab_sheet = lab_coat_agents.get_worksheet(0)

values_list = lab_sheet.col_values(1)
