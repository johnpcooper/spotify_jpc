import pandas as pd
from spotify_jpc import playback, utilities, constants
from importlib import reload
from datetime import datetime
import calendar
from textwrap import dedent

def get_playlist(playlist_id='7Gr9kNeQNwapj3KYaAIhCu', **kwargs):
    """
    Return playlist (a dictionary). playlist_id can be looked up by name
    in in the DataFrame returned by playlist.database()

    This function does instantiate a user spotipy object (utilities.get_user_sp())
    """
    sp = kwargs.get('sp', utilities.get_user_sp())
    try:
        playlist = sp.playlist(playlist_id, fields="tracks,next")
    except Exception as e:
        playlist = None
        print(f"Couldn't find playlist with id: {playlist_id}\nSpotipy error:\n{e}")
        print(f'You can look up playlist ids in playlist.database()')
    
    return playlist


def get_playlist_tracks(playlist_id='7Gr9kNeQNwapj3KYaAIhCu', **kwargs):
    """
    Return a list of dictionaries, one for each track in the playlist 
    found using <playlist_id>.
    
    Keys of each dict are 'name' for track name, etc:    
    
    dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms',
               'episode', 'explicit', 'external_ids', 'external_urls', 'href', 'id',
               'is_local', 'name', 'popularity', 'preview_url', 'track', 'track_number',
               'type', 'uri'])
    """
    results = get_playlist(playlist_id)
    # I'm limited to only grabbing up to 100 tracks from the playlist
    tracks = results['tracks']
    tracks_list = [tracks['items'][i]['track'] for i in range(len(tracks['items']))]
    
    return tracks_list

def get_track_artist_names(track_dict):
    # best to get track_dict from get_playlist_tracks()[i]
    artists = track_dict['artists']
    names = [artist['name'] for artist in artists]
    
    return names

def get_track_artist_ids(track_dict):
    artists = track_dict['artists']
    ids = [artist['id'] for artist in artists]
    
    return ids

def make_playlist_tracks_df(playlist_id='7Gr9kNeQNwapj3KYaAIhCu', allkeys=False, **kwargs):
    # need to add functinality to get song release date and my add date
    # to make_playlist_tracks_df()
    keys = kwargs.get('fields', ['name', 'uri',
                                 'id', 'artist_name',
                                 'artist_id', 'release_date'])
    tracks_list = get_playlist_tracks(playlist_id)
    columns_dict = {}
    
    track_dfs = []
    for i, track in enumerate(tracks_list):
        # Add some custom extracted fields. Sometimes 
        track['artist_name'] = get_track_artist_names(track)[0]
        track['artist_id'] = get_track_artist_ids(track)[0]
        track['release_date'] = utilities.get_track_release_dt(track)
        if allkeys:            
            for key in track.keys():
                columns_dict[key] = track[key]
            try:
                track_df = pd.DataFrame(columns_dict, index=[i])
                track_dfs.append(track_df)
            except:
                pass
        else:
            # Only get keys from shorter list above
            for key in keys:
                columns_dict[key] = track[key]
            track_df = pd.DataFrame(columns_dict, index=[i])
            track_dfs.append(track_df)

    tracks_df = pd.concat(track_dfs)
    
    return tracks_df

def make_playlists_df():
    
    utilities.set_env_vars()
    sp = utilities.get_user_sp()
    username = constants.user_vars['username']
    playlists = sp.user_playlists(username, limit=50)
    playlist_dfs = []

    keys = ['name',
            'uri',
            'id']
    
    for i, playlist_dict in enumerate(playlists['items']):
        print(f"Making playlist DataFrame {i+1} of {len(playlists['items'])}", end='\r')
        columns_dict = {}
        for key in keys:
            columns_dict[key] = playlist_dict[key]
            if key == 'id':
                tracks_df = make_playlist_tracks_df(playlist_id=playlist_dict[key], sp=sp)
                # need to add functinality to get song release date and my add date
                # to make_playlist_tracks_df()
                for col in tracks_df.columns:
                    columns_dict[f'track_{col}'] = tracks_df.loc[:, col]
                    
        playlist_df = pd.DataFrame(columns_dict)
        playlist_dfs.append(playlist_df)

    playlists_df = pd.concat(playlist_dfs)
    
    return playlists_df

def make_playlists_db():
    
    sp = utilities.get_user_sp()
    username = constants.user_vars['username']
    playlists = sp.user_playlists(username, limit=50)
    playlist_dfs = []

    keys = ['name',
            'uri',
            'id']
    
    for i, playlist_dict in enumerate(playlists['items']):
        columns_dict = {}
        for key in keys:
            columns_dict[key] = playlist_dict[key]                    
        playlist_df = pd.DataFrame(columns_dict, index=[i])
        playlist_dfs.append(playlist_df)

    playlists_df = pd.concat(playlist_dfs)
    
    return playlists_df

def database(**kwargs):
    """
    Return the dataframe containing a database
    of playlists in the user's library

    If no file found at path, return None
    """
    path = kwargs.get('path', constants.user_vars['playlist_db_path'])
    try:
        db = pd.read_csv(path)
    except FileNotFoundError:
        db = None
        print(f'No file at path: {path}')
        if kwargs.get('path') == None:
            print(dedent("""\
                   Either create a refreshed database using playlist.update_database()
                   or update the value of constants.user_vars['playlist_db_path']
                   """))
        else:
            print(dedent("""\
                   Pass an existing path keyword argument
                   """))
        
    return db

def update_database():
    """
    Refresh the playlist database .csv. 
    Check spotify_jpc.constants.user_vars['playlist_db_path'] and make sure
    there is an existing .csv at that path
    """
    path = constants.user_vars['playlist_db_path']
    new_db = make_playlists_db()
    old_db = database()
    # Check if there's a .csv at the path. If not,
    # just create an empty one with the same cols
    # as the new database
    try:   
        # Get information for playlists in the new
        # database that aren't already in the pre-existing one
        new_db = new_db[~new_db.id.isin(old_db.id)]
        final_db = pd.concat([old_db, new_db], ignore_index=True)
        # Save the updated database
        final_db.to_csv(path, index=False)
    except:        
        old_db = pd.DataFrame(columns=new_db.columns)
        old_db.to_csv(path, index=False)

def get_playlist_by_name(playlist_name='2020 June'):
    """
    Look up playlist_name in playlist.database() to get id.
    Get playlist with playlist.get_playlist(id)
    
    get_playlist() returns None if no playlist found
    """
    db = database()
    assert playlist_name in db.name.values, "'{playlist_name}' not recorded in playlist.database()"
    playlist_id = db.set_index('name').loc[playlist_name, 'id']
    playlist = get_playlist(playlist_id=playlist_id)
    
    return playlist

def add_track_to_playlist(track, playlist_name, **kwargs):
    """
    Look up the playlist id corresponding to palylist_name
    in the dataframe returned by database()
    """
    db = database()
    sp = kwargs.get('sp', utilities.get_user_sp())
    user = constants.user_vars['username']
    assert playlist_name in db.name.values, "playlist name not recored in playlist.database()"
    
    playlist_id = db.set_index('name').loc[playlist_name, 'id']
    track_ids = [track['id']]

    sp.user_playlist_add_tracks(user, playlist_id, tracks=track_ids, position=None)

def add_single_to_playlist(track, **kwargs):

    date = track['album']['release_date']
    date = datetime.fromisoformat(date)
    year = date.year
    month = calendar.month_name[date.month]
    name = f'{year} {month}'

    try:
        add_track_to_playlist(track, name)
    except:
        print(f"Couldn't find playlist with name {name}")


def add_current_track_to_playlist(ask_name=False, **kwargs):

    db = database()
    track = playback.get_current_track()

    if ask_name:
        name = input("Enter name of target playlist> ")
        while name not in db.name.values:
            name = input(f"No playlist with name {name}, try again> ")
        add_track_to_playlist(track, name)

    # Otherwise, add track to the singles playlists for 
    # that song's release month
    else:
        add_single_to_playlist(track)
