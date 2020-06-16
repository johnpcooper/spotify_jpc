import pandas as pd
from spotify_jpc import playback, utilities, constants
from importlib import reload

def get_playlist_tracks(playlist_id='7Gr9kNeQNwapj3KYaAIhCu'):
    """
    Return a list of dictionaries, one for each track in the playlist 
    found using <playlist_id>.
    
    Keys of each dict are 'name' for track name, etc:    
    
    dict_keys(['album', 'artists', 'available_markets', 'disc_number', 'duration_ms',
               'episode', 'explicit', 'external_ids', 'external_urls', 'href', 'id',
               'is_local', 'name', 'popularity', 'preview_url', 'track', 'track_number',
               'type', 'uri'])
    """
    utilities.set_env_vars()
    sp = utilities.get_user_sp(scope='playlist-modify-private')
    results = sp.playlist(playlist_id, fields="tracks,next")
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

def make_playlist_tracks_df(playlist_id='7Gr9kNeQNwapj3KYaAIhCu', verbose=False, **kwargs):
    # need to add functinality to get song release date and my add date
    # to make_playlist_tracks_df()
    keys = kwargs.get('fields', ['name', 'uri',
                                 'id', 'artist_name',
                                 'artist_id'])
    tracks_list = get_playlist_tracks(playlist_id)
    columns_dict = {}
    
    track_dfs = []
    for i, track in enumerate(tracks_list):
        # Add some custom extracted fields
        track['artist_name'] = get_track_artist_names(track)[0]
        track['artist_id'] = get_track_artist_ids(track)[0]
        if verbose:            
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
    sp = utilities.get_user_sp(scope='playlist-modify-private')
    playlists = sp.user_playlists('anothergriningsoul', limit=50)
    playlist_dfs = []

    keys = ['name',
            'uri',
            'id']
    
    for i, playlist_dict in enumerate(playlists['items']):
        columns_dict = {}
        for key in keys:
            columns_dict[key] = playlist_dict[key]
            if key == 'id':
                tracks_df = make_playlist_tracks_df(playlist_id=playlist_dict[key])
                # need to add functinality to get song release date and my add date
                # to make_playlist_tracks_df()
                for col in tracks_df.columns:
                    columns_dict[f'track_{col}'] = tracks_df.loc[:, col]
                    
        playlist_df = pd.DataFrame(columns_dict)
        playlist_dfs.append(playlist_df)

    playlists_df = pd.concat(playlist_dfs)
    
    return playlists_df