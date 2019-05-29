# Facebook Auto Adder

## Summary

I built this when my startup didn't have enough money to pay for lead generation tools. The code isn't pretty but it works. We use Python2.7, Welenium, Twilio API, Sendgrid + Heroku + more to automate the process of adding friends on Facebook.

This code will add about 100 people a day without you doing any manual work (once you get it set up)

I learned how to scrape, automate user actions and integrate external apis through this repo. I hope it is helpful.

**_ The code could be substantially improved but I am working on other projects at this time. Specifically, putting the code into folders and making it easier to understand would be the most helpful_**

I welcome all pull requests

---

###### Table Of Contents:

- [General Requirements](https://github.com/KameronKales/fb_auto_add#general-requirements)
- [Technology Used](https://github.com/KameronKales/fb_auto_add#technology-used)
- [About Project](https://github.com/KameronKales/fb_auto_add#about-project)
- [Google Sheets API](https://github.com/KameronKales/fb_auto_add#obtain-google-sheets-api-credentials)
- [Format Google Sheet](https://github.com/KameronKales/fb_auto_add#google-sheet-with-your-csv-data-in-it-no-headers)
- [Twilio Set Up](https://github.com/KameronKales/fb_auto_add#twilio-account-and-api-key)
- [Sendgrid Set Up](https://github.com/KameronKales/fb_auto_add#sendgrid-account-and-api-key)
- [Heroku Set Up](https://github.com/KameronKales/fb_auto_add#heroku-account)
- [Github Set Up](https://github.com/KameronKales/fb_auto_add#github-account)

---

## General Requirements

- This project will require light technical knowledge + free tooling
- [iTerm2](https://www.iterm2.com/)
- Internet connection
- Patience
- Coffee

Seriously, go grab some coffee:
![alt text][coffee]

[coffee]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/coffee_meme.jpg "Coffee"

---

## Technology Used

- Python 2.7
- Bash
- Google Sheets API
- Twilio API
- Sendgrid API
- Iterm2
- Heroku
- Github

---

## About Project

###### I built this project when I had no money to run ads to acquire customers. I am very good at making content (and teach business owners how to do this well) and knew if I could get enough people into my world I would be able to grow my business.

###### Throughout the last 12 months I've used this software off and on and added improvements as I went. I build things like this + publish growth tips/hacks on my website and would appreciate you sharing it with anyone you think would be interested.

##### This combined with my knowledge of content became a killer way to grow.

---

## Obtain Google Sheets API Credentials

- If you have not yet done this, you will navigate to [Google Developer Console](http://console.developers.google.com "Google's Developer Console") and create a new project.

Google Developer Console:
![alt text][console view]

[console view]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/google_project.png "Console View"

- Next, you will add a new API "Google Sheets".

Add New API:
![alt text][add new api]

[add new api]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/new_api.png "Add New API"

Add New Sheets API:
![alt text][add new sheets api]

[add new sheets api]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/sheets_api.png "Add New Sheets API"

Enable New Sheets API:
![alt text][enable new sheets api]

[enable new sheets api]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/enable_sheets.png "Enable New Sheets API"

- After that you will see the create credentials button.

Create Credentials:
![alt text][create credentials]

[create credentials]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/create._credentials.png "Create Credentials"

Add Credentials:
![alt text][add credentials]

[add credentials]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/add_credentials.png "Add Credentials"

- When you click this make sure you have the following selected:

  - Google Sheets API
  - Other non-ui (eg.cronjob, daemon)
  - Application data
  - No, Im not using them and click what credentials do I need

  Select Credentials:
  ![alt text][select credentials]

  [Select Credentials]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/select_credentials.png "Select Credentials"

- The next portion will require you to title your service (just title it fbgrowth)
- Select role as project => owner
- And key type = JSON
- Once the file downloads to your computer please rename the file "fb_auto.json" (without the quotes)
- You will need to hold onto this file so don't lose it

Credits:
![alt text][credits]

[credits]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/credits.png "Credits"

Change Title Of File:
![alt text][change title of file]

[change title of file]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/file.png "Change Title Of File"

---

## Google Sheet With Your CSV Data In It (No Headers)

Lab Coat CSV:
![alt text][lab coat csv]

[lab coat csv]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/lab_coat_csv.png "Lab Coat CSV"

- You will upload the newly downloaded CSV into Google Sheets and ensure there are no headers.
- You will also navigate to the share section of the UI as shown below and add the email address that was issued when you created your credentials with google.

Share Email:
![alt text][share email]

[share email]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/share_email.png "Share Email"

---

## Twilio Account And Api Key

Twilio Home Page:
![alt text][twilio home page]

[twilio home page]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/twilio.png "Twilio Home Page"

- You will create an account with Twilio and verify your email.
- You will need to navigate to Programmable SMS to select a number to send from.
- It SHOULD prompt you to select a number. If it doesn't click around until you find one.
- It will be free.
- This enables you to get text messages from the code if it has an error!
- After doing this you will need your Account SID and Auth Token as shown below. Grab those and store them in a safe place.

Twilio Dashboard:
![alt text][twilio dashboard]

[twilio dashboard]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/twilio_dash.png "Twilio Dashboard"

---

## Sendgrid Account And Api Key

Sendgrid Home Page:
![alt text][sendgrid home page]

[sendgrid home page]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/sendgrid.png "Sendgrid Home Page"

- You will create an account with sendgrid and do the required verification.
- This should be relatively easy.
- Next, you will need to get an API key which I have shown how to do below.

Sendgrid API:
![alt text][sendgrid api]

[sendgrid api]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/sendgrid_api.png "Sendgrid API"

---

## Heroku Account

Heroku Home Page:
![alt text][heroku home page]

[heroku home page]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/heroku.png "Heroku Home Page"

- You will create an account with Heroku. It is very simple.
- Once you have that you will create an "app" as shown below.

Create App:
![alt text][create app]

[create app]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/create_app.png "Create App"

- Once you have selected new app you will title the new app like shown below.

Title App:
![alt text][title app]

[title app]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/title_new_app.png "Title App"

- Once the app is created you will see the below screen.

After Creating App:
![alt text][after creating app]

[after creating app]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/after_creating_app.png "After Creating App"

- After the above picture navigate to the connect github screen shown below. This will be the last step before we move on to Github.

Install Heroku On Your Computer:
![alt text][install heroku on your computer]

[install heroku on your computer]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/heroku_install.png "Install Heroku On Your Computer"

- Below you will find a link to install heroku on your computer. Please do that. Then, come back to this guide.

- [Click Here To Open The Heroku Installer](https://devcenter.heroku.com/articles/heroku-cli)

- Set the app to the stack Cedar-14 by running the below command in your terminal.
- You don't need to know what that means really. Technical mumbo jumbo.
- Substitute fbgrowth for your app name.
  `heroku stack:set cedar-14 -a fbgrowth`

- Include the following buildpacks from the Heroku dashboard.

  - heroku/python
  - https://github.com/heroku/heroku-buildpack-chromedriver
  - https://github.com/heroku/heroku-buildpack-xvfb-google-chrome

  Build Packs:
  ![alt text][build packs]

  [Build Packs]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/build_packs.png "Build Packs"

---

## Github Account

- Navigate to [Github](http://github.com) to create an account.

Github:
![alt text][github]

[github]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/github.png "Github"

- Once you have created an account you will select your plan. There is no way to avoid the \$7/month charge without being a student.

Github Plan:
![alt text][github plan]

[github plan]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/github_plans.png "Github Plan"

- Once you have selected a plan you will continue to the onboarding screen as shown below. Select the same options I have indicated.

Onboarding:
![alt text][onboarding]

[onboarding]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/github_onboarding.png "Github Onboarding"

- The next step is to navigate to my profile and select the Facebook Auto Adder Repo. It is not in this picture but should be available by the time you are reading this.

My Profile:
![alt text][my profile]

[my profile]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/kam_profile.png "My Profile"

- Once you have found the repo, you will hit the "fork" button in the top right corner as shown below.

Fork:
![alt text][fork]

[fork]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/fork.png "Fork"

- At this point you are 99% of the way there. You should be able to navigate back to your profile now and see the forked repo. We now need to make this repo private.

- You do this by selecting the repo and navigating to settings. Once in settings you will scroll down to the danger zone and select Make Private as shown below.

Make Private:
![alt text][make private]

[make private]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/private.png "Make Private"

- The next step is the last major step. Go back to the repo page. Open the variables.json file. You will update this file with your own data. Click on the pencil on the right side to do this.

Update with your data:
![alt text][update with your data]

[update with your data]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/variables_update.png "Update with your data"

- Fill in your own data as shown below.

Your Data Here:
![alt text][your data here]

[your data here]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/edit.png "Your Data Here"

- Scroll all the way down and fill in the text box as I have as shown below.

Commit Changes:
![alt text][commit changes]

[commit changes]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/commit_changes.png "Commit Changes"

- The last thing we need to do is pair our repo with heroku. Go back to heroku.com and click your app.
- Navigate to deploy and scroll down. Enter the name of your repo in the search bar.
- Click search.
- Complete the log in info and you are done. As shown below.

Add To Heroku:
![alt text][add to heroku]

[add to heroku]: https://github.com/KameronKales/fb_auto_add/blob/master/pictures/add_heroku.png "Add To Heroku"

- Congrats. Once you get this far your code should automatically do everything else for you each day. You now have a working Facebook Friend Auto Adder.

---

###### Future Features To Be Added:

- Auto canceling after 100 friend requests are sent.
- Auto start in cloud daily (when I am asleep). It currently starts but not sure it knows to stop.

###### Current Bugs:

- Doesn't stop after 100 requests
- Not sure it will run 100 in a row. Scheduler might be inadequate.

###### If You Like This Project:

###### Email kameronkales@gmail.com your feedback.
