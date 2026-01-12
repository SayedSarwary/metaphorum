# MPH Conference Website - Data Management Guide

This website is designed to be static and data-driven. **No coding is required to update the content** for speakers, schedule, or basic site information.

## How to Update Data

All data is located in the `src/data/` folder.

### 1. Conference Details
Edit `src/data/config.json` to update:
- Conference Name & Year
- Dates & Location
- Contact Info
- External Links (Registration, Drive Folders)

### 2. Speakers
Edit `src/data/speakers.json`.
**Fields:**
- `id`: Unique identifier (e.g., "s1", "john-doe"). Used to link talks.
- `full_name`: Display name.
- `affiliation`: University or Organization.
- `bio`: Short biography.
- `photo_url`: URL to an image. Can be a hosted URL (public Google Drive link, Cloudinary, etc.) or a local path.

### 3. Talks
Edit `src/data/talks.json`.
**Fields:**
- `id`: Unique identifier.
- `title`: Title of the presentation.
- `abstract`: Description.
- `speaker_id`: Must match an `id` from `speakers.json`.
- `track_id`: Must match an `id` from `tracks.json`.
- `duration_minutes`: Length in minutes.

### 4. Schedule
Edit `src/data/schedule.json`.
This file links talks to specific times and rooms.
**Fields:**
- `id`: Unique ID for the schedule slot (e.g., "sch1").
- `talk_id`: Connects to `talks.json`.
- `day`: Format `YYYY-MM-DD` (e.g., "2026-10-12").
- `start_time`: 24-hour format `HH:MM`.
- `end_time`: 24-hour format `HH:MM`.
- `room`: Room Name.

### 5. Tracks
Edit `src/data/tracks.json` to define color-coded tracks (e.g., "Epidemiology", "Clinical").

## Duplicating for Next Year (MPH 2027)
1. Copy the entire project folder.
2. Update `src/data/config.json` with the new year and dates.
3. Clear out `speakers.json`, `talks.json`, and `schedule.json` (keep the brackets `[]`).
4. Fill in the new data.
5. Run `npm run build` and deploy.
