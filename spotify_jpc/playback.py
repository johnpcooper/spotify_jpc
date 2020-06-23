from spotify_jpc.utilities import get_user_sp, get_clipboard_uri, set_env_vars

def play_clipboard(**kwargs):
    """
    Search spotify for whatever's on the clipboard and
    play the first resulting track
    """
    sp = kwargs.get('sp', get_user_sp('user-modify-playback-state'))
    track_uri = get_clipboard_uri()
    
    if track_uri:
        sp.start_playback(uris=[track_uri])
        print(f"Playing track")
    else:
        print("Couldn't find a track with this clipboard query")

def get_current_track(**kwargs):
    """
    Return the currently playing track (a dictionary)
    """
    sp = get_user_sp(scope='user-read-currently-playing')
    track = sp.current_user_playing_track()
    return track['item']