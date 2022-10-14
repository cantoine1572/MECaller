#This will take the information from ME API and create an email
#to send to NetAdmins as a calendar invite

import win32com.client as win32
from datetime import datetime
import pytz
tz = pytz.timezone("US/Pacific")

#here we need to import the manageengine dates from the API for the


start_time = tz.localize(datetime())
subject = 'ME Test'
duration = 30
location = ''

#Will need to change to netadmins after testing
recipient = 'cantoine@gscu.org'

outlook = win32.Dispatch('outlook.application')
# CreateItem: 1 -- Outlook Appointment Item
appt = outlook.CreateItem(1)

# set the parameters of the meeting
appt.Start = start_time
appt.Duration = duration
appt.Location = location
appt.Subject = subject

appt.MeetingStatus = 1 # this enables adding of recipients
appt.Recipients.Add(recipient)
appt.Organizer = sender
appt.ReminderMinutesBeforeStart = 15
appt.ResponseRequested = True
appt.Save()
appt.Send()