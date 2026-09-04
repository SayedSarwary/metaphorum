#!/usr/bin/python3

# This script is used to create a combined list from the JSON files in
# ./src/data/:
# - talks.json
# - speakers.json
# - tracks.json
#
# This is used primarily to simplify cross-checking agains the CSV file
# used to generate  ./src/data/schedule.json

import json

#SRCDATAPATH = "./src/data/" 	# JSON from ./src/data/
SRCDATAPATH = "./data/"			# JSON from ./src/data/
OUTDATAPATH = "./data/"




with open(SRCDATAPATH + 'speakers.json') as f:
    speakers_list = json.load(f)
speaker_names = {}
for speaker in speakers_list:
    speaker_names[speaker["id"]] = speaker["full_name"]
    
#with open(SRCDATAPATH + 'tracks.json') as f:
#    tracks_list = json.load(f)

with open(SRCDATAPATH + 'talks.json') as f:
    talks_list = json.load(f)
for talk in talks_list:
	talk_id = talk["id"]
	talk_title = talk["title"]
	track_id = talk["track_id"]
	speaker_id = talk["speaker_id"]
	speaker_name = speaker_names[speaker_id]
#    print(talk_id + " \t " + track_id + " \t " + speaker_id + " \t " + speaker_name + " \t " + talk_title)





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

