#!/usr/bin/python3

# Build  ./src/data/schedule.json  from a CSV file relaing the contents of
# - talks.json      directly
# - speakers.json   indirectly
# - tracks.json     indirectly

import json

DATAPATH = './data/'
schedsrc = DATAPATH + "MAN_2026_Schedule_DRAFT11_website_version_2026-09-03.csv"


schedule = []

with open(schedsrc, "r") as f:
	rows = f.readlines()
	
for row in rows:
	record = {}
	field = row.split("\t")
	record["id"] = field[0]
	record["talk_id"] = field[5]
	record["day"] = field[1]
	record["start_time"] = field[2]
	record["end_time"] = field[3]
	record["room"] = field[4]
	schedule.append(record)
	
with open(DATAPATH + 'schedule.json', "w") as f:
    json.dump(schedule, f, indent=4)



#{
#    "id": "sch3",
#    "talk_id": "",
#    "day": "2026-09-18",
#    "start_time": "09:00",
#    "end_time": "17:00",
#    "room": "Conference Venue"
#},
