from access_drive import values_list
from fb_login import login, driver
from random_time import rest
from update_spreadsheet import cell_list
from fb_email_alert import start_growth, end_growth

## The code is running over and over again for no real reason
## Seems it logged into my facebook 10 times in 5 minutes.

def working_process(ok):
    rest()
    start_growth()
    login()
    for item in values_list:
        if item == 'Sent Friend Request':
            print "already sent"
        else:
            driver.get(item)
            print "Opening item"
            rest()
            link = driver.find_elements_by_id('u_ps_0_0_2')
            print "This is link"
            print link
            cell_list(item)
            for x in range(0,len(link)):
                if link[x].is_displayed():
                    link[x].click()
                    rest()
end_growth()
