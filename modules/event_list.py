from modules.event import *
import datetime

event1 = Event("party", datetime.date(2020, 5, 17), "EDI1", 35,  "All staff meeting")
event2 = Event("boiler-plate party", datetime.date(2020, 6, 18), "GITHUB", 2, "why are we typing this again?!")

events = [event1, event2]
# from modules.event_list import add_new_event, events
# ImportError: cannot import name 'events' from 'modules.event_list' (/Users/mackmillar/codeclan_work/week_03/day_4/lab_2/flask_calculator/modules/event_list.py)



def add_new_event():
    events.append(event)
# event1 = Event(datetime.date(2020, 5, 17), "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
# event2 = Event(datetime.date(2020, 6, 18), "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
# event3 = Event(datetime.date(2020, 7, 19), "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")