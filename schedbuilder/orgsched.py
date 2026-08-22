#!/usr/bin/python3

# Build  ./src/data/schedule.json  from a CSV file relaing the contents of
# - talks.json      directly
# - speakers.json   indirectly
# - tracks.json     indirectly

import json

DATAPATH = './data/'
schedsrc = DATAPATH + "MAN_2026_Schedule_DRAFT3_website_version.csv"


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










#with open(DATAPATH + 'speakers.json') as f:
#    speakers_list = json.load(f)
#speakers_dict = {}
#for speaker in speakers_list:
#    speakers_dict[speaker["id"]] = speaker["full_name"]
#print()
#print(speakers_dict)

#with open(DATAPATH + 'talks.json') as f:
#    talks_list = json.load(f)
#talks_dict = {}
#for talk in talks_list:
#    talks_dict[talk["id"]] = talk
#print()
#for k in talks_dict.keys():
#    print(
#        talks_dict[k]["id"] + " \t " \
#        + talks_dict[k]["speaker_id"] + " \t " \
#        + speakers_dict[talks_dict[k]["speaker_id"]] + " \t " \
#        + talks_dict[k]["track_id"]
#    )


#print(talks_dict)

#with open(DATAPATH + 'tracks.json') as f:
#    tracks_list = json.load(f)
#print()
#print(tracks_list)


#themes = {}
#for k in tracks.keys():
#    themes["theme_name"] = tracks[

#with open(DATAPATH + 'allin.csv', "w") as f:
#for k in talks.keys():
#    talk_id = talks["id"]
#    speaker_id = talks["speaker_id"]
#    speaker_name = speakers[speaker_id]
#    track_id = talks["track_id"]
#    track_name = tracks[]
#    title = talks["title"]






#{
#    "id": "sch3",
#    "talk_id": "",
#    "day": "2026-09-18",
#    "start_time": "09:00",
#    "end_time": "17:00",
#    "room": "Conference Venue"
#},

