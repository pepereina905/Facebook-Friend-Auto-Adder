import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from read_json import lab_coat_secret

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('fb_auto.json', scope)

gc = gspread.authorize(credentials)

spreadsheet_url = lab_coat_secret

lab_coat_agents = gc.open_by_url(spreadsheet_url)

lab_sheet = lab_coat_agents.get_worksheet(0)

def cell_list(current_item):
    cell_item = lab_sheet.find(current_item)
    row = cell_item.row
    col = cell_item.col
    print row
    update_stat = lab_sheet.update_cell(row, col, 'Sent Friend Request')

def count_facebook_adds(update_stat):
    count_facebook_adds.counter += 1
    count_facebook_adds.counter = 0
    if count_facebook_adds == 99:
        print "Stop the function"
        ## Need to add code to actually stop the program after 100
    else:
        print "Function can continue to run"
