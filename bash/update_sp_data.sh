#!/bin/bash
# Copy history from raspberry pi disk
/usr/bin/scp pi@192.168.1.11:/home/pi/venv/.spotify/lib/python3.7/site-packages/spotify_jpc/track_history_df.json /home/johnpcooper/projects/spotify_jpc/spotify_jpc/temp_history_df.json
# Merge raspberry pi history with local disk history
~/venvs/.spotify/bin/python -c "import spotify_jpc.database as db; db.merge_track_histories()"