import os
from tkinter import Tk
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_jpc import constants

def set_env_vars():

    for key, value in constants.env_vars.items():
        os.environ[key] = value

def get_user_sp(scope='user-modify-playback-state', **kwargs):
    """
    Instantiate and return a spotipy.Spotify object using my
    credentials from spotify_jpc.constants by default

    scope is set to 'user-
    """
    set_env_vars()
    username = kwargs.get('username', constants.user_vars['username'])
    token = util.prompt_for_user_token(username=username, scope=scope)
    sp = spotipy.Spotify(auth=token)

    return sp

def get_client_sp(**kwargs):
    """
    Instantaite and return a spotipy.Spotify object using my client
    credentials (as long as they are set as environment variables)
    """
    set_env_vars()
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    return sp

def get_clipboard():
    """
    Return the contents of the OS clipboard
    using tkinter
    """
    root = Tk()
    root.withdraw()
    clipboard = root.clipboard_get()
    return clipboard

def get_clipboard_uri(**kwargs):
    """
    Search spotify for whatever's on the clipboard and
    return the uri of the first track in search results.

    If no results, return None
    """
    
    set_env_vars()
    sp = get_user_sp(scope='user-modify-playback-state')
    query = get_clipboard()
    results = sp.search(q=query, type='track')
    
    items = results['tracks']['items']
    # If there was a result of the search, get that track's 
    # spotify id and uri (more commonly used)
    if len(items) > 0:
        track = items[0]
        track_id = track['id']
        track_uri = track['uri']
        track_name = track['name']
        print(f'Found track_uri: {track_uri}\nTrack name: {track_name}\nfor query: {query}')
    else:
        print(f"Couldn't find a matching track for search:\n{query}")
        track_id = None
        track_uri = None
        track_name = None
        
    return track_uri